import pandas as pd

#1. 模拟一些简单的数据
data = {
	'姓名': ['张三', '李四', '王五'],
	'得分': [85,92,78]
}

#2. 将数据转换为pandas的核心对象: DataFrame(数据表)
df = pd.DataFrame(data)
print(df)

#3. 打印结果
print("项目工程环境验证成功！以下是测试数据：")
print(df)

#4. 简单的计算：求平均分
print(f"\n平均得分是：{df['得分'].mean()}")