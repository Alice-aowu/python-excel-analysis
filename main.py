import pandas as pd
import matplotlib.pyplot as plt

# ---------------------- 1. 读取原始Excel数据 ----------------------
df = pd.read_excel("data.xlsx")
print("✅ 数据读取成功！")
print("原始数据预览：")
print(df.head())
print("原始数据行数：", len(df))

# ---------------------- 2. 数据清洗（核心功能） ----------------------
# 去除重复行
df = df.drop_duplicates()
# 删除存在空值的行
df = df.dropna()
# 重置索引
df = df.reset_index(drop=True)

print("\n✅ 数据清洗完成！")
print("清洗后数据行数：", len(df))

# 保存清洗后的数据
df.to_excel("cleaned_data.xlsx", index=False)

# ---------------------- 3. 基础数据分析统计 ----------------------
# 只针对数值列统计
stat_df = df.describe()
print("\n===== 数据分析结果 =====")
print(stat_df)

# 导出统计报表
stat_df.to_excel("report.xlsx")
print("\n✅ 分析报表已保存为 report.xlsx")

# ---------------------- 4. 自动生成数据图表 ----------------------
# 设置中文（解决matplotlib中文乱码）
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

# 取第一列数值数据画图（通用适配所有成绩/金额/数据表格）
num_data = df.select_dtypes(include=["number"])
num_data.plot(kind="bar", figsize=(10, 6))
plt.title("Excel 数据统计柱状图")
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

print("✅ 数据图表已保存为 chart.png")
print("\n🎉 全部任务完成！已生成清洗文件、分析报表、统计图表")
