import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#1. 页面配置与字体设置
st.set_page_config(page_title="咖啡店数据看板", layout="wide")
plt.rcParams['font.sans-serif'] = ['SimHei']

st.title("咖啡店业务数据实时分析")

#2. 侧边栏：文件上传
st.sidebar.header("数据管理")
uploaded_file = st.sidebar.file_uploader("上传销售数据(CSV)", type="csv")

if uploaded_file is not None:
	#3.读取数据
	df = pd.read_csv(uploaded_file)
	df['交易时间'] = pd.to_datetime(df['交易时间'])
	df['销售额'] = df['单价']*df['销售数量']
	
	#4. 数据展示  - 核心指标卡片
	total_sales = df['销售额'].sum()
	total_orders = len(df)
	
	col1, col2 = st.columns(2)
	col1.metric("总销售额", f"¥{total_sales:,.2f}")
	col2.metric("总订单数", f"{total_orders} 笔")
	
	#5. 核心逻辑：销售趋势图
	st.subheader("整体销售额趋势")
	
	#按天聚合数据
	daily_sales = df.groupby(df['交易时间'].dt.date)['销售额'].sum()
	
	#使用Streamlit自带的折线图
	st.line_chart(daily_sales)
	
	#6. 数据表格预览 可选
	with st.expander("查看原始数据明细"):
		st.write(df)
else:
	st.info("请先在左侧上传`data/sales_data.csv` 文件来查看结果")		

# ----- 产品对比分析区--------
st.subheader("产品销售对比")

#1. 获取所有不重复的产品名称
all_products = df['商品名称'].unique().tolist()

#2. 建立多选下拉选单
selected_products = st.multiselect(
    "选择产品",
    all_products,
    default=all_products[:2] #默认选择前两个产品
)

if selected_products:
    #3. 按照选中的产品进行过滤
    compare_df = df[df['商品名称'].isin(selected_products)]
    
    #4. 按照产品和交易时间进行分组
    #unstack() 会把产品名称从行索引变为列，交易时间作为行索引
    comparsion_data = compare_df.groupby([df['交易时间'].dt.date, '商品名称'])['销售额'].sum().unstack()

    #5. 使用Streamlit的折线图展示对比结果
    st.line_chart(comparsion_data)
else:
    st.warning("请先上传销售数据")
