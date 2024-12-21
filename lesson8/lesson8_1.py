import streamlit as st

# Initialize the counter if it doesn't exist
#手動建立counter_key, 並設定初始值為0
if "counter" not in st.session_state:
    #st.session_state['counter'] = 0
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"這頁網頁己經執行 {st.session_state.counter}次次.")
st.button("再執行一次", key="reset")#自動建立reset_key
if st.session_status:
    st.session_state.counter +=1
#st.write(st.session_state)
