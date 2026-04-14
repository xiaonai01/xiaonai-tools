#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网页抓取工具
简单易用的网页数据抓取工具
"""
import requests
from bs4 import BeautifulSoup
import json
import csv
from pathlib import Path

class WebScraper:
    def __init__(self, base_url=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_page(self, url):
        """获取网页内容"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"获取网页失败: {e}")
            return None
    
    def parse_html(self, html):
        """解析HTML"""
        return BeautifulSoup(html, 'html.parser')
    
    def extract_links(self, soup, base_url=None):
        """提取所有链接"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if base_url and not href.startswith('http'):
                href = base_url + href
            links.append({
                'text': link.get_text().strip(),
                'url': href
            })
        return links
    
    def extract_images(self, soup, base_url=None):
        """提取所有图片"""
        images = []
        for img in soup.find_all('img', src=True):
            src = img['src']
            if base_url and not src.startswith('http'):
                src = base_url + src
            images.append({
                'alt': img.get('alt', ''),
                'src': src
            })
        return images
    
    def extract_text(self, soup):
        """提取所有文本"""
        return soup.get_text(separator='\n', strip=True)
    
    def scrape_to_json(self, url, output_file):
        """抓取网页并保存为JSON"""
        html = self.fetch_page(url)
        if not html:
            return False
        
        soup = self.parse_html(html)
        
        data = {
            'url': url,
            'title': soup.title.string if soup.title else '',
            'links': self.extract_links(soup, self.base_url),
            'images': self.extract_images(soup, self.base_url),
            'text': self.extract_text(soup)
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"数据已保存到 {output_file}")
        return True
    
    def scrape_to_csv(self, url, output_file, selector=None):
        """抓取表格数据并保存为CSV"""
        html = self.fetch_page(url)
        if not html:
            return False
        
        soup = self.parse_html(html)
        
        if selector:
            tables = soup.select(selector)
        else:
            tables = soup.find_all('table')
        
        if not tables:
            print("未找到表格")
            return False
        
        # 处理第一个表格
        table = tables[0]
        rows = []
        
        for tr in table.find_all('tr'):
            row = []
            for td in tr.find_all(['td', 'th']):
                row.append(td.get_text().strip())
            rows.append(row)
        
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        print(f"表格数据已保存到 {output_file}")
        return True

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="网页抓取工具")
    parser.add_argument("url", help="要抓取的网页URL")
    parser.add_argument("-o", "--output", help="输出文件路径")
    parser.add_argument("-f", "--format", choices=['json', 'csv'], default='json', help="输出格式")
    parser.add_argument("-s", "--selector", help="CSS选择器（用于CSV格式）")
    
    args = parser.parse_args()
    
    scraper = WebScraper()
    
    if args.format == 'json':
        output_file = args.output or 'scraped_data.json'
        scraper.scrape_to_json(args.url, output_file)
    elif args.format == 'csv':
        output_file = args.output or 'scraped_data.csv'
        scraper.scrape_to_csv(args.url, output_file, args.selector)