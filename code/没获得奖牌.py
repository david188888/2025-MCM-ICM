import pandas as pd

# 初始化一个空列表，用来存储结果
medal_info = []

# 读取数据
df1 = pd.read_csv("C:/Users/16348/MEISAI/2025-MCM-ICM/data/Processed_data/processed_summerOly_athletes2.csv")

# 将'Medal'列进行标签编码
df1['Medal'] = df1['Medal'].map({'Gold': 3, 'Silver': 2, 'Bronze': 1, 'No medal': 0})

# 按年份从小到大排序数据
df1 = df1.sort_values(by=['NOC', 'Year'])

# 遍历每个国家
for country in df1['NOC'].unique():
    country_df = df1[df1['NOC'] == country]

    # 判断这个国家是否获得过奖牌
    has_medal = 1 if country_df['Medal'].sum() > 0 else 0

    # 记录每个国家每年的参与情况
    participation_count = 1  # 初始值
    for year in country_df['Year'].unique():
        year_df = country_df[country_df['Year'] == year]

        # 计算该年参加的不同项目数量
        event_count = len(year_df['Event'].unique())

        # 计算该年参加的不同运动员数量
        people_count = len(year_df['Name'].unique())

        # 计算该年获得奖牌的项目数量（同一项目只记一次）
        # 只考虑获得了奖牌的项目，去重后计算数量
        medal_events = year_df[year_df['Medal'] > 0]['Event'].nunique()

        # 将年份、国家、是否得过奖牌、参加次数、项目数量、参赛人数和奖牌总数的信息加入到列表中
        medal_info.append([year, country, has_medal, participation_count, event_count, people_count, medal_events])

        # 参加次数递增
        participation_count += 1

# 创建一个新的DataFrame
medal_df = pd.DataFrame(medal_info,
                        columns=['Year', 'Team', 'Medal', 'Participation Count', 'Event Count', 'People Count', 'Medal Count'])

# 保存到Excel文件
medal_df.to_excel(r'C:\Users\16348\Desktop\test_with_medal_count.xlsx', index=False)

print("文件已保存到C:\\Users\\16348\\Desktop\\test_with_medal_count.xlsx")
