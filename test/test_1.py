import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 创建 DataFrame
data = {
    '姓名': ['小明', '小红', '小刚', '小华', '小李'],
    '年龄': [23, 25, 22, 24, np.nan],
    '成绩': [88, 92, 85, np.nan, 90],
    '性别': ['男', '女', '男', '女', '男']
}

df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 2. 数据清洗
# 填充缺失值
df['年龄'].fillna(df['年龄'].mean(), inplace=True)  # 用平均值填充年龄
df['成绩'].fillna(df['成绩'].mean(), inplace=True)  # 用平均值填充成绩

print("\n清洗后的数据:")
print(df)

# 3. 数据选择与过滤
# 选择年龄大于23的学生
filtered_df = df[df['年龄'] > 23]
print("\n年龄大于23的学生:")
print(filtered_df)

# 4. 分组与聚合
# 按性别分组并计算平均成绩
grouped = df.groupby('性别')['成绩'].mean()
print("\n按性别分组的平均成绩:")
print(grouped)

# 5. 数据可视化
plt.figure(figsize=(8, 5))
df['性别'].value_counts().plot(kind='bar', color=['blue', 'pink'])
plt.title('性别分布')
plt.xlabel('性别')
plt.ylabel('人数')
plt.xticks(rotation=0)
plt.show()

# 6. 输出到 CSV 文件
df.to_csv('学生数据.csv', index=False)
print("\n数据已输出到 '学生数据.csv'")