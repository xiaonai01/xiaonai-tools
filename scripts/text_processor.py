#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本处理工具
批量处理文本文件，支持多种操作
"""
import os
import re
from pathlib import Path

class TextProcessor:
    def __init__(self, directory):
        self.directory = Path(directory)
        self.text_files = []
        
    def find_text_files(self, extensions=None):
        """查找文本文件"""
        if extensions is None:
            extensions = ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml']
        
        self.text_files = []
        for ext in extensions:
            self.text_files.extend(self.directory.rglob(f"*{ext}"))
        
        print(f"找到 {len(self.text_files)} 个文本文件")
        return self.text_files
    
    def batch_replace(self, old_text, new_text, dry_run=False):
        """批量替换文本"""
        count = 0
        for file_path in self.text_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_text in content:
                    new_content = content.replace(old_text, new_text)
                    if not dry_run:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                    count += 1
                    print(f"替换: {file_path}")
            except Exception as e:
                print(f"处理 {file_path} 时出错: {e}")
        
        print(f"完成: 替换了 {count} 个文件")
        return count
    
    def find_and_replace_regex(self, pattern, replacement, dry_run=False):
        """使用正则表达式查找和替换"""
        count = 0
        regex = re.compile(pattern)
        
        for file_path in self.text_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content, num_subs = regex.subn(replacement, content)
                if num_subs > 0:
                    if not dry_run:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                    count += num_subs
                    print(f"替换 {num_subs} 处: {file_path}")
            except Exception as e:
                print(f"处理 {file_path} 时出错: {e}")
        
        print(f"完成: 共替换 {count} 处")
        return count
    
    def extract_emails(self):
        """提取所有邮箱地址"""
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = set()
        
        for file_path in self.text_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                found_emails = re.findall(email_pattern, content)
                emails.update(found_emails)
            except Exception as e:
                print(f"处理 {file_path} 时出错: {e}")
        
        print(f"找到 {len(emails)} 个邮箱地址:")
        for email in sorted(emails):
            print(f"  {email}")
        
        return list(emails)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="文本处理工具")
    parser.add_argument("directory", help="要处理的目录路径")
    parser.add_argument("--find-emails", action="store_true", help="提取邮箱地址")
    parser.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="批量替换文本")
    parser.add_argument("--dry-run", action="store_true", help="模拟运行")
    
    args = parser.parse_args()
    
    processor = TextProcessor(args.directory)
    processor.find_text_files()
    
    if args.find_emails:
        processor.extract_emails()
    
    if args.replace:
        old_text, new_text = args.replace
        processor.batch_replace(old_text, new_text, args.dry_run)