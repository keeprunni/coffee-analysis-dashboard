import pandas as pd

#1. 故意制造一份有缺失值的销售数据
df_sales = pd.read_csv('data/sales_data.csv')
df_sales.loc[0:4, '单价'] = None #抹掉前五行的单价
df_sales.loc[10:14, '销售数量'] = None #抹掉另外5行的数量
df_sales.to_csv('data/sales_dirty.csv', index=False, encoding='utf_8_sig')

#2. 创建一份成本表
cost_data = {
'商品名称': ['拿铁', '美式', '卡布奇诺', '摩卡', '澳白'],
   '单位成本': [12, 8, 15, 18, 15]
}

df_costs = pd.DataFrame(cost_data)
df_costs.to_csv('data/costs.csv',index=False, encoding='utf_8_sig')
print("⚠️ 脏数据 'sales_dirty.csv' 和成本表 'costs.csv' 已准备就绪！")