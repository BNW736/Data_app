import streamlit as st
import requests

url = "http://127.0.0.1:8000/get_data"
url_train = "http://127.0.0.1:8000/train"

if "columns" not in st.session_state:
    st.session_state["columns"] = [] 
    
uploaded_file = st.file_uploader("Upload CSV file")
if st.button("press"):
    my_files = {
        "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
    }
    response = requests.post(url, files=my_files)
        
    if response.status_code == 200:
        st.success("File processed successfully!")
        
        data = response.json()
        st.dataframe(data)
        
        # Grab the keys from the first row of data and save to memory!
        if len(data) > 0:
            st.session_state["columns"] = list(data[0].keys())
    else:
        st.error(f"Server Error: {response.status_code}. Check FastAPI terminal!")
        
        
modol=["lightgbm","catboot","tensor"]
x = st.multiselect("Input X? (Predictors)", options=st.session_state["columns"])
y = st.selectbox("Input Y? (Target)", options=st.session_state["columns"])
model=st.selectbox("model",options=modol)


if st.button("train") :
    my_files = {
        "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
    }
    
    x_string = ",".join(x)
    
    form_data = {
        "x_axis": x_string, 
        "y_axis": y ,
        "model":model
    }
    
    response = requests.post(url_train, files=my_files, data=form_data)
        
    if response.status_code == 200:
        st.success("Model trained successfully!")
        st.dataframe(response.json())
        st.line_chart(response.json())
    else:
        st.error(f"Server Error: {response.text}")