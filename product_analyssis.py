import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体（解决 Windows 环境下绘图中文乱码问题）
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 1. 加载数据并计算销售额
df = pd.read_csv('data/sales_data.csv')
df['销售额'] = df['单价'] * df['销售数量']

# 2. 按产品汇总销量和销售额
product_stats = df.groupby('商品名称').agg({
    '销售数量': 'sum',
    '销售额': 'sum'
}).sort_values(by='销售额', ascending=False) # 按销售额从高到低排序

print("产品销售排名：")
print(product_stats)

# 3. 绘制柱状图
product_stats['销售额'].plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('各产品总销售额分布图')
plt.xlabel('产品名称')
plt.ylabel('销售额 (元)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. 显示图表
plt.tight_layout()
plt.show()

# 5. 到处为excel文件
product_stats.to_excel('data/产品分析报告.xlsx')
print("报告已生成在data 文件夹下!")