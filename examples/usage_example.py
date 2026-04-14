#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小奈工具集使用示例
"""
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.file_organizer import organize_files
from scripts.text_processor import TextProcessor
from utils.file_utils import get_file_size, count_files
from utils.text_utils import count_words, extract_keywords

def example_file_organizer():
    """文件整理工具示例"""
    print("=== 文件整理工具示例 ===")
    
    # 模拟运行
    print("模拟运行（不实际移动文件）:")
    organize_files(".", dry_run=True)
    
    # 实际运行（取消注释以执行）
    # organize_files(".")

def example_text_processor():
    """文本处理工具示例"""
    print("\n=== 文本处理工具示例 ===")
    
    # 创建处理器
    processor = TextProcessor(".")
    processor.find_text_files()
    
    # 提取邮箱（如果有文本文件）
    if processor.text_files:
        print("提取邮箱地址:")
        processor.extract_emails()
    
    # 批量替换示例
    print("\n批量替换示例:")
    print("processor.batch_replace('旧文本', '新文本', dry_run=True)")

def example_file_utils():
    """文件工具函数示例"""
    print("\n=== 文件工具函数示例 ===")
    
    # 获取文件大小
    if os.path.exists("README.md"):
        size = get_file_size("README.md")
        print(f"README.md 文件大小: {size}")
    
    # 统计文件数量
    stats = count_files(".", recursive=False)
    print(f"当前目录文件统计: {stats}")

def example_text_utils():
    """文本工具函数示例"""
    print("\n=== 文本工具函数示例 ===")
    
    # 示例文本
    sample_text = """
    小奈工具集是一个实用的工具集合。
    包含文件整理、文本处理、网页抓取等功能。
    联系邮箱: xiaonai@example.com
    项目地址: https://github.com/xiaonai01/xiaonai-tools
    """
    
    # 统计单词
    word_count = count_words(sample_text)
    print(f"单词数量: {word_count}")
    
    # 提取关键词
    keywords = extract_keywords(sample_text, min_length=2)
    print("关键词:")
    for word, count in keywords:
        print(f"  {word}: {count}")

if __name__ == "__main__":
    print("小奈工具集使用示例")
    print("=" * 50)
    
    example_file_organizer()
    example_text_processor()
    example_file_utils()
    example_text_utils()
    
    print("\n" + "=" * 50)
    print("示例运行完成！")
    print("要实际使用工具，请取消注释相应的函数调用。")