import pandas as pd

# 读取文件
df = pd.read_excel("C:/Users/16348/Desktop/test_with_people_count.xlsx")

# 按照国家和年份排序
df = df.sort_values(by=['Team', 'Year'])

# 计算每个国家的第一次参赛年份
df['First Participation Year'] = df.groupby('Team')['Year'].transform('min')

# 计算每个国家从第一次参赛到当前年份的参赛人数增长率
df['People Growth Rate'] = (df['People Count'] - df.groupby('Team')['People Count'].transform('first')) / df.groupby('Team')['People Count'].transform('first')
df['People Growth Rate'] = df['People Growth Rate'].fillna(0)

# 计算每个国家从第一次参赛到当前年份的参赛项目增长率
df['Event Growth Rate'] = (df['Event Count'] - df.groupby('Team')['Event Count'].transform('first')) / df.groupby('Team')['Event Count'].transform('first')
df['Event Growth Rate'] = df['Event Growth Rate'].fillna(0)

# 保存新的文件
df.to_excel("C:/Users/16348/Desktop/test_with_event_growth_rate.xlsx", index=False)

print("文件已保存到 C:/Users/16348/Desktop/test_with_event_growth_rate.xlsx")
