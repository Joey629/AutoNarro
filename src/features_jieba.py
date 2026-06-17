import jieba
import re

def split_sentences(text):
    """
    分句：句号/问号/叹号/换行/分号（转写稿常用换行表示话轮）。
    """
    sentences = re.split(r"[。？！\n；;]+", text)
    return [s for s in sentences if s.strip()]

def extract_calculable_features(text):
    """
    从一段原始叙事文本中提取所有可计算的语言学特征 (A类)。
    
    Args:
        text (str): 原始叙事文本。
        
    Returns:
        dict: 包含自动化特征的字典。
    """
    features = {}
    
    # 1. 分词
    words = jieba.lcut(text)
    
    # 2. 分句
    sentences = split_sentences(text)
    
    # --- 计算特征 ---
    
    # TNW (Total Number of Words) - 总词数
    features['TNW'] = len(words)
    
    # TDW (Total Different Words) - 总独立词数
    features['TDW'] = len(set(words))
    
    # TNU (Total Number of Units) - 总单元/句子数
    features['TNU'] = len(sentences)
    
    # MLU (Mean Length of Utterance) - 平均句长（词/句）
    features['MLU'] = features['TNW'] / features['TNU'] if features['TNU'] > 0 else 0

    # TTR (Type-Token Ratio) - 词型率 / 词汇多样性
    features['TTR'] = features['TDW'] / features['TNW'] if features['TNW'] > 0 else 0.0

    return features


# 中文标签（报告 / SaaS 展示）
LINGUISTIC_LABELS = {
    "TNW": ("总词数", "Total Number of Words"),
    "TDW": ("不同词数", "Total Different Words"),
    "TNU": ("句子数", "Total Number of Utterances"),
    "MLU": ("平均句长", "Mean Length of Utterance"),
    "TTR": ("词型率", "Type-Token Ratio"),
}

if __name__ == "__main__":
    # --- 演示 ---
    # 假设这是你的一段新叙事
    new_narrative_text = "小猫想抓蝴蝶。它跳了起来，但是没有抓到。小猫很难过。"
    
    print(f"正在分析文本: \"{new_narrative_text}\"")
    
    # 1. 自动提取 A 类特征
    calculable_features = extract_calculable_features(new_narrative_text)
    
    print("\n--- 自动提取的 A 类特征 ---")
    print(calculable_features)
    
    # 示例输出:
    # {'TNW': 16, 'TDW': 11, 'TNU': 3, 'MLU': 5.333333333333333}