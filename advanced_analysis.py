import pandas as pd

#1. 加载两个表
df_sales = pd.read_csv('data/sales_dirty.csv')
df_costs = pd.read_csv('data/costs.csv')

#2. 清洗数据，删除任何含有空值的行
#dropna() 是Pandas处理缺失值最快的方法
df_sales_clean = df_sales.fillna(0)

print(f"清洗完成！删除了{len(df_sales) -len(df_sales_clean)} 条不完整记录")

#3. 合并表格(merge)
#我们希望根据商品名称将两个表对其
df_combined = pd.merge(df_sales_clean, df_costs, on='商品名称')

print(df_combined)

#4.计算利润
df_combined['单条利润'] = (df_combined['单价'] - df_combined['单位成本'])*df_combined['销售数量']

#5. 查看结果
profit_report = df_combined.groupby('商品名称')['单条利润'].sum().sort_values(ascending=False)
print("\n 各产品总利润分析：")
print(profit_report)
