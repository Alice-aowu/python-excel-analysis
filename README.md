# Python Excel 自动清洗与数据分析报表工具

## 项目简介
基于 Python + pandas 开发的自动化 Excel 数据处理工具
专为新手学习数据处理、办公自动化设计，一键完成：
- 数据去重、空值清洗
- 批量数据分析统计
- 自动生成可视化图表
- 输出标准分析报表

## 技术栈
- Python
- pandas（数据处理）
- matplotlib（数据可视化）
- openpyxl（Excel读写）

## 使用方法
1. 安装依赖
```bash
pip install pandas openpyxl matplotlib
```

2. 在项目目录放入 `data.xlsx` 原始数据

3. 运行程序
```bash
python main.py
```

## 输出文件
- cleaned_data.xlsx：清洗后的干净数据
- report.xlsx：数据统计分析报表
- chart.png：数据柱状统计图

## 项目优势
- 零基础可运行
- 代码注释详细，适合学习
- 完全自动化，无需手动操作
- 可拓展为批量文件处理、自动报表生成

