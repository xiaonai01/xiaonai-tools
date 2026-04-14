#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本工具函数
提供常用的文本处理功能
"""
import re
from collections import Counter

def count_words(text):
    """统计单词数量"""
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)

def count_characters(text, include_spaces=True):
    """统计字符数量"""
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(' ', ''))

def extract_keywords(text, min_length=3):
    """提取关键词"""
    # 移除标点符号
    text = re.sub(r'[^\w\s]', ' ', text)
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 过滤短词
    words = [word for word in words if len(word) >= min_length]
    
    # 统计词频
    word_counts = Counter(words)
    return word_counts.most_common(10)

def clean_text(text):
    """清理文本"""
    # 移除多余空白
    text = re.sub(r'\s+', ' ', text)
    # 移除特殊字符
    text = re.sub(r'[^\w\s.,!?;:]', '', text)
    return text.strip()

def format_table(data, headers=None):
    """格式化表格数据"""
    if not data:
        return ""
    
    # 计算列宽
    if headers:
        col_widths = [len(str(h)) for h in headers]
    else:
        col_widths = [0] * len(data[0])
    
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # 构建表格
    lines = []
    
    # 表头
    if headers:
        header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
        lines.append(header_line)
        lines.append("-" * len(header_line))
    
    # 数据行
    for row in data:
        row_line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        lines.append(row_line)
    
    return "\n".join(lines)

def generate_slug(text):
    """生成URL友好的slug"""
    # 转换为小写
    text = text.lower()
    # 替换空格和特殊字符为连字符
    text = re.sub(r'[^a-z0-9\u4e00-\u9fff]', '-', text)
    # 移除连续的连字符
    text = re.sub(r'-+', '-', text)
    # 移除首尾连字符
    text = text.strip('-')
    return text