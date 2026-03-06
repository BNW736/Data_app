import streamlit as st

dic = {"name": 1, "boy": 3}
y=st.selectbox("cjoose", options=dic)
print(y)
