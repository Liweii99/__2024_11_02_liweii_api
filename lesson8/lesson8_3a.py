from tools import fetch_youbike_data
import streamlit as st

youbike_data:list[dict] = fetch_youbike_data()

# 使用streamlit分2個欄位
# 使用you_bike_data:list的資料, 取出所有的行政區域(sarea), 不可以重複
# 左邊是選擇行政區域(sarea), 使用下拉式表單
# 右邊是顯示該行政區域的YouBike站點資訊的表格資料
# 最下方是顯示該行政區域的YouBike站點資訊的地圖
# 使用streamlit分2個欄位
col1, col2 = st.columns(2)

# 取出所有的行政區域(sarea), 不可以重複
sareas = list(set([item['sarea'] for item in youbike_data]))

# 左邊是選擇行政區域(sarea), 使用下拉式表單
selected_sarea = col1.selectbox('選擇行政區域', sareas)

# 右邊是顯示該行政區域的YouBike站點資訊的表格資料
filtered_data = [item for item in youbike_data if item['sarea'] == selected_sarea]
col2.table(filtered_data)

# 最下方是顯示該行政區域的YouBike站點資訊的地圖
filter_data = list(filter(lambda item:item['sarea'] == selected_sarea,youbike_data))
locations = [{'lat': float(item['lat']), 'lon': float(item['lng'])} for item in filter_data]
st.map(locations)
