import pandas as pd
import numpy as np

# 加载数据（使用原始字符串并指定编码）
file_path = r"D:\python\MCM2025\data processing\数据预处理结果\summerOly_programs.csv"
try:
    df = pd.read_csv(file_path, encoding='GBK')  # 尝试 GBK 编码
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')  # 如果 GBK 失败，尝试 ISO-8859-1

# 1. 处理乱码
df.replace(to_replace=r'[^\x00-\x7F]', value='', regex=True, inplace=True)

# 2. 处理数字前后的异常符号
df.replace(to_replace=r'[^0-9.]', value='', regex=True, inplace=True)

# 3. 处理空值
df.fillna(0, inplace=True)
df = df.dropna(thresh=len(df.columns) - 5)

# 4. 重新计算 Total 值
# 假设 Total 是 Gold + Silver + Bronze 的和
if 'Gold' in df.columns and 'Silver' in df.columns and 'Bronze' in df.columns:
    df['Total'] = df['Gold'].astype(float) + df['Silver'].astype(float) + df['Bronze'].astype(float)

# 保存处理后的数据
output_file_path = r"D:\python\MCM2025\data processing\数据预处理结果\summerOly_programs_cleaned.csv"
df.to_csv(output_file_path, index=False, encoding='GBK')  # 保存为 GBK 编码

print(f"数据预处理完成，结果已保存到 {output_file_path}")