import pandas as pd
import random
from datetime import datetime, timedelta

# 1. 准备基础数据
products = {
    '拿铁': 28,
    '美式': 22,
    '卡布奇诺': 30,
    '摩卡': 32,
    '澳白': 28
}

data_list = []
start_date = datetime(2023, 10, 1)

# 2. 随机生成 100 条销售记录
for i in range(100):
    date = start_date + timedelta(days=random.randint(0, 6), hours=random.randint(8, 20))
    name = random.choice(list(products.keys()))
    price = products[name]
    count = random.randint(1, 5)
    
    data_list.append([date, name, price, count])

# 3. 转换为 DataFrame 并保存
df = pd.DataFrame(data_list, columns=['交易时间', '商品名称', '单价', '销售数量'])
df.to_csv('data/sales_data.csv', index=False, encoding='utf_8_sig')

print("✅ 实验数据 'data/sales_data.csv' 已生成！")