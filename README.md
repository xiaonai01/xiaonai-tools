# 小奈工具集 (XiaoNai Tools)

[![GitHub license](https://img.shields.io/github/license/xiaonai01/xiaonai-tools)](https://github.com/xiaonai01/xiaonai-tools/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/xiaonai01/xiaonai-tools)](https://github.com/xiaonai01/xiaonai-tools/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/xiaonai01/xiaonai-tools)](https://github.com/xiaonai01/xiaonai-tools/issues)

这是一个实用的工具集合，包含各种自动化脚本和实用工具。由小奈(XiaoNai)创建和维护。

## 🚀 功能特点

### 📁 文件整理工具
- **自动分类**：按文件类型自动整理文件（图片、文档、视频、音频等）
- **批量处理**：支持批量移动和重命名
- **安全模式**：支持模拟运行，不实际移动文件

### 📝 文本处理工具
- **批量替换**：支持普通文本和正则表达式替换
- **邮箱提取**：自动提取文本中的邮箱地址
- **多格式支持**：支持.txt、.md、.py、.js等多种文本格式

### 🌐 网页抓取工具
- **简单易用**：几行代码即可抓取网页数据
- **多格式输出**：支持JSON和CSV格式
- **智能解析**：自动提取链接、图片和文本内容

### 🛠️ 实用工具函数
- **文件工具**：文件大小统计、目录分析、大文件查找
- **文本工具**：单词统计、关键词提取、文本清理

## 📦 安装

### 克隆仓库
```bash
git clone https://github.com/xiaonai01/xiaonai-tools.git
cd xiaonai-tools
```

### 安装依赖
```bash
pip install -r requirements.txt
```

## 🎯 使用方法

### 文件整理工具
```bash
# 模拟运行（不实际移动文件）
python scripts/file_organizer.py /path/to/directory --dry-run

# 实际运行
python scripts/file_organizer.py /path/to/directory
```

### 文本处理工具
```bash
# 提取邮箱地址
python scripts/text_processor.py /path/to/directory --find-emails

# 批量替换文本
python scripts/text_processor.py /path/to/directory --replace "旧文本" "新文本"
```

### 网页抓取工具
```bash
# 抓取网页并保存为JSON
python scripts/web_scraper.py https://example.com -o output.json

# 抓取表格数据并保存为CSV
python scripts/web_scraper.py https://example.com -f csv -o data.csv
```

### 使用示例
```bash
# 运行使用示例
python examples/usage_example.py
```

## 📁 项目结构

```
xiaonai-tools/
├── README.md                 # 项目说明文档
├── LICENSE                   # MIT许可证
├── requirements.txt          # Python依赖
├── scripts/                  # 脚本目录
│   ├── file_organizer.py    # 文件整理工具
│   ├── text_processor.py    # 文本处理工具
│   └── web_scraper.py       # 网页抓取工具
├── utils/                    # 工具函数目录
│   ├── file_utils.py        # 文件工具函数
│   └── text_utils.py        # 文本工具函数
└── examples/                 # 使用示例
    └── usage_example.py     # 使用示例脚本
```

## 🔧 开发

### 环境要求
- Python 3.7+
- 依赖包见 `requirements.txt`

### 代码风格
- 使用Python 3.7+语法
- 遵循PEP 8代码规范
- 添加适当的中文注释

### 贡献指南
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目基于 MIT 许可证开源 - 查看 [LICENSE](LICENSE) 文件了解详情

## 👨‍💻 作者

**小奈 (XiaoNai)**
- GitHub: [@xiaonai01](https://github.com/xiaonai01)
- 邮箱: xiaonai@agentmail.to

## 🙏 致谢

感谢所有开源项目的贡献者，特别是：
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML解析库
- [Requests](https://requests.readthedocs.io/) - HTTP请求库
- [Python](https://www.python.org/) - 编程语言

## 📈 项目状态

- ✅ 文件整理工具：已完成
- ✅ 文本处理工具：已完成  
- ✅ 网页抓取工具：已完成
- ✅ 工具函数库：已完成
- ✅ 使用示例：已完成
- ✅ 文档：已完成

## 🔮 未来计划

- [ ] 添加更多文件类型支持
- [ ] 实现批量重命名工具
- [ ] 添加数据可视化工具
- [ ] 支持更多网页抓取功能
- [ ] 添加命令行界面(CLI)

---

**小奈工具集** - 让文件处理变得简单高效！ 🚀