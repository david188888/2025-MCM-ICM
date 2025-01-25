import pandas as pd

# 读取数据
medal_counts = pd.read_csv("C:/Users/16348/Desktop/Updated_Result_with_Events_as_Columns.csv")
athletes = pd.read_csv("C:/Users/16348/MEISAI/2025-MCM-ICM/data/summerOly_athletes.csv")

# 定义奖牌对应的分数
medal_points = {
    'Gold': 3,
    'Silver': 2,
    'Bronze': 1,
    'No medal': 0
}

# 1. 将Event列作为新增列，确保没有重复的列
events = athletes['Event'].unique()  # 获取所有唯一的Event
new_columns = []

# 确保这些事件列都存在于medal_counts中
for event in events:
    if event not in medal_counts.columns:
        new_columns.append(event)

# 如果有新的列，先将这些列添加到medal_counts
if new_columns:
    new_df = pd.DataFrame(0, index=medal_counts.index, columns=new_columns)  # 创建新的列，并初始化为0
    medal_counts = pd.concat([medal_counts, new_df], axis=1)  # 一次性合并新列

# 2. 计算这些新增列的得分
# 创建一个用于记录每个团队和项目是否已添加分数的字典
added_scores = {}

for index, row in athletes.iterrows():
    team = row['Team']  # 提取Team列
    event = row['Event']  # 提取Event列
    year = row['Year']
    medal = row['Medal']

    # 获取奖牌的分数
    points = medal_points.get(medal, 0)  # 如果奖牌为None，默认为0

    # 用于记录是否已经为该事件（团队+项目+年份）添加过分数
    event_key = (team, event, year)

    # 只在该团队和该项目的分数未被添加时，才进行更新
    if event_key not in added_scores:
        # 使用loc直接查找并更新对应的行，将Team与medal_counts的NOC和Year进行匹配
        mask = (medal_counts['NOC'] == team) & (medal_counts['Year'] == year)

        # 查找匹配的行
        if mask.any():
            # 如果找到了匹配的行，更新该行对应Event列的分数
            medal_counts.loc[mask, event] += points

        # 标记为已经添加过该项目的分数
        added_scores[event_key] = True

# 保存更新后的数据
medal_counts.to_csv("C:/Users/16348/Desktop/result.csv", index=False)
