import pandas as pd

# 读取文件
df = pd.read_excel("C:/Users/16348/Desktop/test_with_last_people_count_v2.xlsx")

# 按照国家和年份排序
df = df.sort_values(by=['Team', 'Year'])

# 计算上一次参赛项目数量
df['Last Event Count'] = df.groupby('Team')['Event Count'].shift(1)

# 对于第一次参赛的国家（NaN），将“上一次参赛项目数量”填充为0
df['Last Event Count'] = df['Last Event Count'].fillna(0)

# 保存新的文件
df.to_excel("C:/Users/16348/Desktop/test_with_last_event_count.xlsx", index=False)

print("文件已保存到 C:/Users/16348/Desktop/test_with_last_event_count.xlsx")
