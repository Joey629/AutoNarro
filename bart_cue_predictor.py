# bart_cue_predictor.py
# [目标]：加载训练好的 BART (Seq2Seq) 线索生成模型，并提供 predict_ist_words。
# [来自: 1] (基于 train_bart_cue_generator.py)

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import warnings
warnings.filterwarnings("ignore")

class BartPredictor:
    def __init__(self, model_dir="./bart_model"):
        """
        加载训练好的 BART 模型 和 tokenizer。
        
        Args:
            model_dir (str): [来自: 1] 包含 'pytorch_model.bin' 和 'config.json' 的文件夹路径。
        """
        print(f"--- [模块B] 正在从 '{model_dir}' 加载 BART 线索提取模型 ---")
        self.model_dir = model_dir
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        try:
            # [来自: 1]
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_dir).to(self.device)
            # [来自: 1]
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
            print("  [✓] BART 模型加载成功。")
        except Exception as e:
            print(f"❌ 错误: 加载 BART 模型失败。请确保 '{model_dir}' 路径正确。")
            print(f"  请先运行 'train_bart_cue_generator.py' 来训练并保存 BART 模型。")
            print(f"  {e}")
            raise

    def predict_ist_words(self, text):
        """
        为一段新文本自动生成 predicted_ist_words 字符串。
        """
        # [来自: 1] 遵循训练脚本中的预处理逻辑
        preprocess_text = f"线索提取：{text}" 
        
        self.model.eval()
        with torch.no_grad():
            inputs = self.tokenizer(preprocess_text, return_tensors='pt', max_length=512, truncation=True).to(self.device)
            
            # [来自: 1] 遵循训练脚本中的生成参数
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=64, 
                num_beams=4,
                early_stopping=True
            )
            
            predicted_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
        return predicted_text

if __name__ == "__main__":
    # --- 演示 ---
    new_narrative_text = "小猫想抓蝴蝶。它跳了起来，但是没有抓到。小猫很难过。"
    
    print("--- 演示 BART 预测器 (模块 B) ---")
    
    try:
        bart_model = BartPredictor(model_dir="./bart_model")
        predicted_clues = bart_model.predict_ist_words(new_narrative_text)
        print(f"\n输入文本: {new_narrative_text}")
        print(f"预测线索 (Predicted ist_words): {predicted_clues}")
    except Exception as e:
        print("\n--- 演示失败 ---")
        print(f"错误: {e}")