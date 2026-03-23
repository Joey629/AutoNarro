import pandas as pd
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq
    # [!] [撤回] 不再需要 EarlyStoppingCallback
)
import re
import warnings
import pathlib
import argparse 
import sys

warnings.filterwarnings("ignore")

# ==============================================================================
# --- ( ! ) 全局配置 ( ! ) ---
# ==============================================================================
MODEL_CHECKPOINT = "fnlp/bart-base-chinese"
DATA_PATH = "narratives.csv" 
DEFAULT_MODEL_DIR = "./model_b_bart_structured_generator" 

# ==============================================================================
# --- ( ! ) 您的“标准答案” ( ! ) ---
# ==============================================================================
EXPERT_KEYWORD_DB = {
    # IS_Per: 感知状态词
    'IS_Per': ['看到', '看见', '听见', '听到', '闻到', '尝到', '看'],
    # IS_Phy: 生理状态词
    'IS_Phy': ['饿', '渴', '累', '困', '痛', '发抖','酸',],
    # IS_Con: 意识词
    'IS_Con': ['活着', '醒着', '睡着', '死了', '清醒', '昏迷'],
    # IS_Emo: 情感词
    'IS_Emo': ['高兴', '开心', '快乐', '兴奋', '得意', '笑', '有趣', 
               '难过', '伤心', '哭', '害怕', '紧张', '担心', '着急', 
               '生气', '惊讶', '奇怪', '无聊', '满意', '吓', '痛苦','失望',],
    # IS_Men: 心理动词
    'IS_Men': ['想', '想要','觉得', '感觉','认为', '惊奇', '忘记', '知道', '愿意', '决定','计划',],
    # IS_Ling: 语言动词/表达动词
    'IS_Ling': ['说', '告诉', '问', '回答', '喊', '叫', '警告', ],
}

def build_lookup_map(keyword_db):
    lookup_map = {}
    for category, keywords in keyword_db.items():
        for keyword in keywords:
            if keyword in lookup_map:
                print(f"警告: 关键词 '{keyword}' 在 {lookup_map[keyword]} 和 {category} 中重复！")
            lookup_map[keyword] = category
    return lookup_map

WORD_TO_CATEGORY_MAP = build_lookup_map(EXPERT_KEYWORD_DB)

# ==============================================================================
# --- ( ! ) 核心函数 ( ! ) ---
# ==============================================================================

def create_structured_target(ist_words_string):
    """
    将原始 ist_words 字符串（如 "看到（4） 想（1）"）
    转换为带标签的训练目标（如 "[IS_Per] 看到 (4) [IS_Men] 想 (1)"）。
    """
    if not isinstance(ist_words_string, str):
        return ""

    clean_str = ist_words_string.replace(' ', '') 
    
    matches = re.findall(r'([\u4e00-\u9fa5]+)（(\d+)）', clean_str)
    
    classified = {
        'IS_Per': [], 'IS_Phy': [], 'IS_Con': [],
        'IS_Emo': [], 'IS_Men': [], 'IS_Ling': []
    }
    unclassified = []

    for word, count in matches:
        category = WORD_TO_CATEGORY_MAP.get(word)
        result_entry = f"{word} ({count})" 
        
        if category:
            classified[category].append(result_entry)
        else:
            unclassified.append(result_entry)
            
    final_target_parts = []
    for category, items in classified.items():
        if items:
            final_target_parts.append(f"[{category}] {' '.join(items)}")
            
    if unclassified:
        final_target_parts.append(f"[Unclassified] {' '.join(unclassified)}")

    return " ".join(final_target_parts)


def run_training(data_path, model_checkpoint, output_dir):
    """
    完整的 "模型B" (BART-base) 训练流程
    [!] [撤回] 移除 use_validation 参数
    """
    
    print(f"开始加载分词器: {model_checkpoint}")
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    
    new_tokens = ['[IS_Per]', '[IS_Phy]', '[IS_Con]', '[IS_Emo]', '[IS_Men]', '[IS_Ling]', '[Unclassified]']
    tokenizer.add_special_tokens({'additional_special_tokens': new_tokens})
    print(f"已将 {len(new_tokens)} 个新类别标签添加到分词器中。")

    print(f"正在加载数据: {data_path}")
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"错误: '{data_path}' 文件未找到。请确保该文件在同一目录下。")
        return None 

    df = df[["Text", "ist_words"]].copy()
    df["ist_words"] = df["ist_words"].fillna("")
    
    print("开始构建新的“结构化”训练目标...")
    df["target_text"] = df["ist_words"].apply(create_structured_target)
    
    df.rename(columns={"Text": "input_text"}, inplace=True)
    print(f"数据加载完毕。共 {len(df)} 条样本。")

    raw_dataset = Dataset.from_pandas(df)

    max_input_length = 512
    max_target_length = 128 

    def preprocess_function(examples):
        model_inputs = tokenizer(
            examples["input_text"], 
            max_length=max_input_length, 
            truncation=True, 
            padding="max_length"
        )
        with tokenizer.as_target_tokenizer():
            labels = tokenizer(
                examples["target_text"], 
                max_length=max_target_length, 
                truncation=True,
                padding="max_length"
            )
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    print("开始对数据集进行分词和预处理...")
    
    # ==========================================================
    # --- ( ! ) [撤回] ( ! ) ---
    # 撤回到在 100% 数据上训练
    # ==========================================================
    print("在 100% 的数据上训练...")
    tokenized_train_dataset = raw_dataset.map(preprocess_function, batched=True, num_proc=4)
    tokenized_eval_dataset = None # [!] 无验证集
    # ==========================================================
    
    print("预处理完成。")


    print(f"开始加载预训练模型: {model_checkpoint}")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    model.resize_token_embeddings(len(tokenizer))
    
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    model.to(device)
    print(f"模型已加载到: {device}")

    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    training_args = Seq2SeqTrainingArguments(
        output_dir=f"{output_dir}_output", 
        
        # ==========================================================
        # --- ( ! ) [撤回] ( ! ) ---
        # 移除早停，使用固定的 20 周期
        # ==========================================================
        eval_strategy="no",
        save_strategy="steps", # 恢复默认
        load_best_model_at_end=False,
        num_train_epochs=20, # [!] [撤回] 固定为 20 周期
        # ==========================================================
        
        learning_rate=5e-5, 
        warmup_ratio=0.1, 
        
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        weight_decay=0.01,
        save_total_limit=2,
        predict_with_generate=True,
        logging_steps=50,
        fp16=torch.cuda.is_available(),
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_eval_dataset, # [!] 传入 None
        tokenizer=tokenizer,
        data_collator=data_collator,
        callbacks=None # [!] [撤回] 移除回调
    )

    print(f"\n--- [!] 优化: 开始训练 {training_args.num_train_epochs} 个周期 (在 100% 数据上) ---")
        
    trainer.train()
    print("--- 训练完成 ---")

    trainer.save_model(output_dir) # 保存到最终路径
    tokenizer.save_pretrained(output_dir)
    final_path = pathlib.Path(output_dir).resolve()
    print(f"\n最终的 '模型B' 已保存到: {final_path}")
    
    return final_path


class StructuredPredictor:
    """
    [!] 优化的预测器
    """
    def __init__(self, model_path):
        self.model_path = str(model_path) 
        print(f"\n--- 加载 '模型B' 从: {self.model_path} ---")
        
        try:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path, local_files_only=True)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, local_files_only=True)
        except OSError:
            print(f"错误: 找不到已训练的模型 '{self.model_path}'。")
            print("请先使用 --train 标志运行脚本来训练和保存模型。")
            sys.exit(1) 

        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
            
        self.model.to(self.device)
        self.model.eval()
        
        self.max_target_length = 128
        print(f"模型已成功加载到: {self.device}")
        
        self.special_tokens_to_remove = [
            self.tokenizer.pad_token, 
            self.tokenizer.sep_token, 
            self.tokenizer.cls_token,
            self.tokenizer.eos_token,
            self.tokenizer.bos_token
        ]
        self.special_tokens_to_remove = [tok for tok in self.special_tokens_to_remove if tok is not None]


    def _cleanup_output(self, raw_text):
        """
        [!] 优化的格式化修复
        """
        cleaned_text = raw_text
        for token in self.special_tokens_to_remove:
            cleaned_text = cleaned_text.replace(token, "")

        text = re.sub(r'\s+\]', ']', cleaned_text)
        text = re.sub(r'\[\s+', '[', text)
        
        # [!] [最终] 括号修复: 修复 (1 ）
        text = re.sub(r'\(\s*(\d+)\s*[)）]\s*', r'(\1)', text)
        
        text = re.sub(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])', r'\1\2', text)
        text = re.sub(r'([\u4e00-\u9fa5])\s+\(', r'\1(', text)
        text = re.sub(r'\]([\u4e00-\u9fa5])', r'] \1', text)
        text = re.sub(r'\)\[', r') [', text)
        
        return text.strip()


    def predict(self, text_input):
        """
        对单个文本输入进行预测
        """
        print(f"\n--- 正在预测新文本 ---")
        print(f"输入: {text_input[:100].replace(chr(10), ' ')}...") 
        
        inputs = self.tokenizer(
            text_input, 
            return_tensors="pt", 
            max_length=512, 
            truncation=True
        ).to(self.device)
        
        with torch.no_grad():
            output_sequences = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=self.max_target_length,
                num_beams=4,
                early_stopping=True
            )
        
        raw_prediction = self.tokenizer.decode(
            output_sequences[0], 
            skip_special_tokens=False 
        )
        
        predicted_structured_text = self._cleanup_output(raw_prediction)
        
        print("\n--- '模型B' 智能预测结果 ---")
        print(f"预测的结构化线索: {predicted_structured_text}")
        return predicted_structured_text


# ==============================================================================
# --- ( ! ) 主程序入口 ( ! ) ---
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="训练或运行 '模型B' (智能分类版)")
    
    parser.add_argument(
        "--train",
        action="store_true", 
        help="启用训练模式，开始训练模型。"
    )
    
    # ==========================================================
    # --- ( ! ) [撤回] ( ! ) ---
    # 移除了 --no_validation 标志
    # ==========================================================
    
    parser.add_argument(
        "--predict",
        type=str, 
        metavar="TEXT_TO_PREDICT",
        help="启用预测模式，并对提供的文本进行预测。"
    )
    
    parser.add_argument(
        "--model_dir",
        type=pathlib.Path, 
        default=DEFAULT_MODEL_DIR,
        help=f"模型保存或加载的文件夹路径 (默认: {DEFAULT_MODEL_DIR})"
    )
    
    parser.add_argument(
        "--data_path",
        type=pathlib.Path, 
        default=DATA_PATH,
        help=f"训练数据 .csv 文件的路径 (默认: {DATA_PATH})"
    )
    
    args = parser.parse_args()

    # --- 训练模式 ---
    if args.train:
        print(f"[!] 启动训练模式...")
        
        # [!] [撤回] 移除 use_validation 逻辑
        
        run_training(
            data_path=args.data_path,
            model_checkpoint=MODEL_CHECKPOINT,
            output_dir=args.model_dir
            # [!] [撤回] 移除 use_validation
        )
        print("[!] 训练完成。")
        
    # --- 预测模式 ---
    if args.predict:
        print(f"[!] 启动预测模式...")
        
        if not args.model_dir.exists():
            print(f"错误: 找不到模型目录 '{args.model_dir}'。")
            print("请先使用 --train 标志运行脚本来训练和保存模型。")
            sys.exit(1)
            
        predictor = StructuredPredictor(args.model_dir)
        predictor.predict(args.predict)
        
    # --- 无操作 ---
    if not args.train and not args.predict:
        print("未指定操作。")
        print("请使用 --train 来训练模型，或使用 --predict '您的文本' 来进行预测。")
        parser.print_help()


if __name__ == "__main__":
    main()