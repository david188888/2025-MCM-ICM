import pandas as pd

# 读取文件
df = pd.read_excel("C:/Users/16348/Desktop/test_with_lagged_people_count.xlsx")

# 按照国家和年份排序
df = df.sort_values(by=['Team', 'Year'])

# 计算滞后项目数量（前三次平均项目数量）
df['Lagged Event Count'] = df.groupby('Team')['Event Count'].transform(lambda x: x.rolling(3, min_periods=1).mean())

# 保存新的文件
df.to_excel("C:/Users/16348/Desktop/test_with_lagged_event_count.xlsx", index=False)

print("文件已保存到 C:/Users/16348/Desktop/test_with_lagged_event_count.xlsx")
