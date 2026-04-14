#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件工具函数
提供常用的文件操作功能
"""
import os
import shutil
from pathlib import Path

def get_file_size(file_path):
    """获取文件大小（可读格式）"""
    size = os.path.getsize(file_path)
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    
    return f"{size:.2f} TB"

def count_files(directory, recursive=True):
    """统计目录中的文件数量"""
    directory = Path(directory)
    if recursive:
        files = list(directory.rglob('*'))
    else:
        files = list(directory.glob('*'))
    
    file_count = sum(1 for f in files if f.is_file())
    dir_count = sum(1 for f in files if f.is_dir())
    
    return {
        'files': file_count,
        'directories': dir_count,
        'total': file_count + dir_count
    }

def copy_with_structure(src, dst):
    """复制文件并保持目录结构"""
    src = Path(src)
    dst = Path(dst)
    
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    elif src.is_dir():
        for item in src.rglob('*'):
            if item.is_file():
                rel_path = item.relative_to(src)
                target_path = dst / rel_path
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_path)

def find_large_files(directory, min_size_mb=10):
    """查找大文件"""
    directory = Path(directory)
    large_files = []
    
    for file_path in directory.rglob('*'):
        if file_path.is_file():
            size_mb = file_path.stat().st_size / (1024 * 1024)
            if size_mb >= min_size_mb:
                large_files.append({
                    'path': str(file_path),
                    'size_mb': round(size_mb, 2)
                })
    
    # 按大小排序
    large_files.sort(key=lambda x: x['size_mb'], reverse=True)
    return large_files

def clean_temp_files(directory):
    """清理临时文件"""
    directory = Path(directory)
    temp_extensions = ['.tmp', '.temp', '.bak', '.swp', '.DS_Store']
    deleted_count = 0
    
    for ext in temp_extensions:
        for file_path in directory.rglob(f"*{ext}"):
            try:
                file_path.unlink()
                deleted_count += 1
                print(f"删除: {file_path}")
            except Exception as e:
                print(f"删除 {file_path} 失败: {e}")
    
    print(f"清理完成: 删除了 {deleted_count} 个临时文件")
    return deleted_count