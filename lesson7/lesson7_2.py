from tools import taipei
import streamlit as st

@st.dialog("目前網路出現狀況")
def vote(error):
    st.write(error)

try:
    youbike_data:list[dict] = taipei.get_youbikes()
except Exception as error:    
    vote(error)
    st.write("喝杯咖啡!請等一下再試!")
    st.stop()
'''因有st.stop (程式結束),可以省else
else:
    st.write(youbike_data)'''        
st.table(youbike_data)

