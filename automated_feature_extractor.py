# automated_feature_extractor.py
# [目标]: 
# 1. 自动化 A 类特征 (TNU, MLU...) [来自: 2]
# 2. [新] 自动化所有 6 种 B 类内部状态特征 (IS_Per, IS_Emo...) [来自: 1]
#    通过搜索 T5/BART 生成的线索字符串。

import jieba
import re

# --- 导入我们自己的模块 ---
try:
    # [来自: 2] 导入你的 Jieba 计算器
    from linguistic_feature_extractor import extract_calculable_features
except ImportError:
    print("❌ 错误: 找不到 linguistic_feature_extractor.py。")
    print("请确保 'linguistic_feature_extractor.py' [来自: 2] 在同一个文件夹中。")
    exit()

# ==============================================================================
# --- [新] 内置 B 类特征关键词数据库 (来自你的输入) ---
# [来自: 1]
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
# ==============================================================================


# --- 模块 B (扩展): 关键词计数器 ---
def extract_B_class_features(predicted_ist_words_string):
    """
    (B类) 自动计算 T5/BART 生成的线索中包含的所有 B 类关键词。
    """
    
    # [新] 我们将为每个类别分别计数
    feature_counts = {
        'auto_IS_Per_count': 0,
        'auto_IS_Phy_count': 0,
        'auto_IS_Con_count': 0,
        'auto_IS_Emo_count': 0,
        'auto_IS_Men_count': 0,
        'auto_IS_Ling_count': 0,
    }
    
    if not isinstance(predicted_ist_words_string, str):
        return feature_counts
        
    # 对 T5/BART 的输出进行分词，以进行精确匹配
    t5_words = set(jieba.lcut(predicted_ist_words_string))
    
    # 遍历我们的关键词数据库 [来自: 1]
    for key, keywords in EXPERT_KEYWORD_DB.items():
        feature_name = f"auto_{key}_count"
        count = 0
        for keyword in keywords:
            if keyword in t5_words:
                count += 1
        
        if feature_name in feature_counts:
            feature_counts[feature_name] = count
            
    return feature_counts

# --- 主函数 ---
def analyze_automated_features(text, predicted_ist_words):
    """
    为一段新文本自动提取所有 A 类和 B 类特征。
    这是“模块 A”和“模块 B”的组合器。
    """
    # 1. A 类: 来自 Jieba [来自: 2]
    calculable_features = extract_calculable_features(text)
    
    # 2. B 类: 来自 T5/BART [来自: 1]
    b_class_features = extract_B_class_features(predicted_ist_words)
    
    # [重要] 
    # 返回一个包含所有自动化特征的列表。
    # 这个顺序在训练 (脚本3) 和预测 (脚本4) 中必须严格一致。
    
    # 确保特征名称列表的顺序
    feature_names = [
        'auto_TNU',
        'auto_MLU',
        'auto_TNW',
        'auto_TDW',
        'auto_IS_Per_count',
        'auto_IS_Phy_count',
        'auto_IS_Con_count',
        'auto_IS_Emo_count',
        'auto_IS_Men_count',
        'auto_IS_Ling_count'
    ]
    
    feature_vector = [
        calculable_features.get('TNU', 0),
        calculable_features.get('MLU', 0),
        calculable_features.get('TNW', 0),
        calculable_features.get('TDW', 0),
        b_class_features.get('auto_IS_Per_count', 0),
        b_class_features.get('auto_IS_Phy_count', 0),
        b_class_features.get('auto_IS_Con_count', 0),
        b_class_features.get('auto_IS_Emo_count', 0),
        b_class_features.get('auto_IS_Men_count', 0),
        b_class_features.get('auto_IS_Ling_count', 0)
    ]
    
    return feature_vector, feature_names

if __name__ == "__main__":
    # --- 演示 (需要 bart_cue_predictor.py) ---
    try:
        from bart_cue_predictor import BartPredictor
        
        new_text = "小猫想抓蝴蝶。它跳了起来，但是没有抓到。小猫很难过。"
        
        # 1. 运行 模块 B (BART)
        bart_model = BartPredictor(model_dir="./bart_model")
        predicted_clues = bart_model.predict_ist_words(new_text) # e.g., "想 蝴蝶 难过"

        # 2. 运行 模块 A + B(扩展)
        auto_features, auto_names = analyze_automated_features(new_text, predicted_clues)
        
        print(f"分析文本: \"{new_text}\"")
        print(f"BART 预测线索: \"{predicted_clues}\"")
        print("\n--- 自动提取的特征 (A类 + B类) ---")
        print(list(zip(auto_names, auto_features)))
        
        # 预期输出 (基于 IS_MEN_KEYWORDS 中的 '想' 和 '难过'):
        # [('auto_TNU', 3), ('auto_MLU', 5.33...), ('auto_TNW', 16), ('auto_TDW', 11), 
        #  ('auto_IS_Per_count', 0), ('auto_IS_Phy_count', 0), ('auto_IS_Con_count', 0), 
        #  ('auto_IS_Emo_count', 1), ('auto_IS_Men_count', 1), ('auto_IS_Ling_count', 0)]
    
    except ImportError:
        print("❌ 错误: 找不到 bart_cue_predictor.py。请先完成步骤一。")
    except Exception as e:
        print("\n--- 演示失败 ---")
        print(f"错误: {e}")
        print("请确保 './bart_model' 文件夹存在，且 'train_bart_cue_generator.py' [来自: 1] 已成功运行。")