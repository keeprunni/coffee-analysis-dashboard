import pandas as pd

#1. 读取数据
df = pd.read_csv('data/sales_data.csv')

#2.  将“交易时间”转换为真正的日期格式，这样python才能识别日期
df['交易时间'] = pd.to_datetime(df['交易时间'])

#3. 创建销售额列
df['销售额'] = df['单价']*df['销售数量']

#4. 提取日期 去除具体的小时分钟，按日期分组并求和
daily_sales = df.groupby(df['交易时间'].dt.date)['销售额'].sum()

#5. 找出最高额
best_day = daily_sales.idxmax()
max_amount = daily_sales.max()

print(f"\n 生意最好的一天是：{best_day}， 总销售额是{max_amount}" )