#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件整理工具
按文件类型自动整理指定目录下的文件
"""
import os
import shutil
from pathlib import Path

def organize_files(directory, dry_run=False):
    """
    按文件类型整理文件
    
    Args:
        directory: 要整理的目录
        dry_run: 是否只是模拟运行
    """
    directory = Path(directory)
    if not directory.exists():
        print(f"错误: 目录 {directory} 不存在")
        return
    
    # 文件类型映射
    file_types = {
        '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
        '文档': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        '视频': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv'],
        '音频': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        '代码': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.h'],
        '数据': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite']
    }
    
    # 统计信息
    stats = {}
    
    for file_path in directory.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix.lower()
            
            # 查找文件类型
            file_type = '其他'
            for type_name, extensions in file_types.items():
                if file_ext in extensions:
                    file_type = type_name
                    break
            
            # 创建目标目录
            target_dir = directory / file_type
            if not target_dir.exists():
                if not dry_run:
                    target_dir.mkdir()
                print(f"创建目录: {target_dir}")
            
            # 移动文件
            target_path = target_dir / file_path.name
            if not dry_run:
                shutil.move(str(file_path), str(target_path))
            
            # 更新统计
            stats[file_type] = stats.get(file_type, 0) + 1
            print(f"移动: {file_path.name} -> {file_type}/")
    
    # 打印统计信息
    print("\n整理完成!")
    print("统计信息:")
    for type_name, count in stats.items():
        print(f"  {type_name}: {count} 个文件")
    
    if dry_run:
        print("\n注意: 这是模拟运行，没有实际移动文件")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="文件整理工具")
    parser.add_argument("directory", help="要整理的目录路径")
    parser.add_argument("--dry-run", action="store_true", help="模拟运行，不实际移动文件")
    
    args = parser.parse_args()
    organize_files(args.directory, args.dry_run)