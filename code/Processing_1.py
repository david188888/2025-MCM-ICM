import pandas as pd

# 加载数据集
medal_counts = pd.read_csv("C:\\Users\\16348\\Desktop\\C题数据\\2025_Problem_C_Data\\summerOly_medal_counts.csv")
athletes = pd.read_csv("C:\\Users\\16348\\Desktop\\C题数据\\2025_Problem_C_Data\\summerOly_athletes.csv")

# 1. 检查缺失数据
def check_missing_data(df):
    missing_data = df.isnull().sum()
    missing_data_percentage = (missing_data / len(df)) * 100
    return missing_data, missing_data_percentage

# 检查两个数据集的缺失数据
medal_missing_data, medal_missing_percentage = check_missing_data(medal_counts)
athletes_missing_data, athletes_missing_percentage = check_missing_data(athletes)

# 2. 检查奖牌总数的逻辑一致性（Gold + Silver + Bronze 应等于 Total）
def check_logical_consistency(df):
    df['Total_check'] = df['Gold'] + df['Silver'] + df['Bronze']
    df['Total_inconsistent'] = df['Total'] != df['Total_check']
    return df

# 对 medal_counts 进行逻辑一致性检查
medal_counts_checked = medal_counts.groupby('Year', group_keys=False).apply(check_logical_consistency)

# 提取逻辑不一致的数据
inconsistent_total_data = medal_counts_checked[medal_counts_checked['Total_inconsistent'] == True]

# 3. 检查年份是否合理（Year 应在 1896 到当前年份之间）
current_year = 2024
medal_counts['Year_inconsistent'] = (medal_counts['Year'] < 1896) | (medal_counts['Year'] > current_year)
year_inconsistent_data = medal_counts[medal_counts['Year_inconsistent'] == True]

# 4. 使用 IQR 方法检测 Gold、Silver、Bronze 和 Total 的异常值（按年份分组）
def detect_outliers_per_year(df, column):
    outliers = pd.Series(dtype='bool')
    for year, group in df.groupby('Year'):
        Q1 = group[column].quantile(0.25)
        Q3 = group[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        year_outliers = (group[column] < lower_bound) | (group[column] > upper_bound)
        outliers = pd.concat([outliers, year_outliers])
    return outliers

gold_outliers = detect_outliers_per_year(medal_counts, 'Gold')
silver_outliers = detect_outliers_per_year(medal_counts, 'Silver')
bronze_outliers = detect_outliers_per_year(medal_counts, 'Bronze')
total_outliers = detect_outliers_per_year(medal_counts, 'Total')

gold_outliers_data = medal_counts[gold_outliers]
silver_outliers_data = medal_counts[silver_outliers]
bronze_outliers_data = medal_counts[bronze_outliers]
total_outliers_data = medal_counts[total_outliers]

# 5. 检查 athletes 数据中的 Sex 和 NOC 列是否有效
athletes['Medal_invalid'] = ~athletes['Medal'].isin(['Gold', 'Silver', 'Bronze', 'No medal'])
athletes['Sex_invalid'] = ~athletes['Sex'].isin(['M', 'F'])
athletes['NOC_invalid'] = athletes['NOC'].isnull()  # 检查 NOC 是否缺失

# 提取无效数据
invalid_medal_data = athletes[athletes['Medal_invalid'] == True]
invalid_sex_data = athletes[athletes['Sex_invalid'] == True]
invalid_noc_data = athletes[athletes['NOC_invalid'] == True]

# 汇总检测到的问题
medal_counts_issues = {
    'Missing data': medal_missing_data,
    'Inconsistent Total': inconsistent_total_data.shape[0],  # 逻辑不一致的行数
    'Year inconsistencies': year_inconsistent_data.shape[0],
    'Outliers in Gold': gold_outliers_data.shape[0],
    'Outliers in Silver': silver_outliers_data.shape[0],
    'Outliers in Bronze': bronze_outliers_data.shape[0],
    'Outliers in Total': total_outliers_data.shape[0]
}

athletes_issues = {
    'Missing data': athletes_missing_data,
    'Invalid Medal values': invalid_medal_data.shape[0],
    'Invalid Sex values': invalid_sex_data.shape[0],
    'Invalid NOC values': invalid_noc_data.shape[0]
}

# 将问题保存为 DataFrame
medal_counts_issues_df = pd.DataFrame(medal_counts_issues, index=[0])
athletes_issues_df = pd.DataFrame(athletes_issues, index=[0])

# 将问题导出为 CSV 文件
medal_counts_issues_df.to_csv('medal_counts_issues.csv', index=False)
athletes_issues_df.to_csv('athletes_issues.csv', index=False)

# 将具体的问题数据导出为 CSV 文件
inconsistent_total_data.to_csv('inconsistent_total_data.csv', index=False)
year_inconsistent_data.to_csv('year_inconsistent_data.csv', index=False)
gold_outliers_data.to_csv('gold_outliers_data.csv', index=False)
silver_outliers_data.to_csv('silver_outliers_data.csv', index=False)
bronze_outliers_data.to_csv('bronze_outliers_data.csv', index=False)
total_outliers_data.to_csv('total_outliers_data.csv', index=False)

invalid_medal_data.to_csv('invalid_medal_data.csv', index=False)
invalid_sex_data.to_csv('invalid_sex_data.csv', index=False)
invalid_noc_data.to_csv('invalid_noc_data.csv', index=False)

# 输出保存成功的消息
print("问题已保存到 'medal_counts_issues.csv' 和 'athletes_issues.csv'。")
print("具体问题数据已保存到 CSV 文件。")