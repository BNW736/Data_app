import streamlit as st
import requests

url = "http://127.0.0.1:8000/get_data"
url_train = "http://127.0.0.1:8000/trian"

# 1. Show the uploader
uploaded_file = st.file_uploader("Upload CSV file")

if st.button("press"):
    my_files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
        }
    response = requests.post(url, files=my_files)
        
    if response.status_code == 200:
        st.success("File processed successfully!")
        
        st.dataframe(response.json())
    else:
        st.error(f"Server Error: {response.status_code}. Check FastAPI terminal!")
x=st.text_input("input x?")
y=st.text_input("input Y?")

if st.button("train"):
    my_files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
                
        }
    file = {
            "x":x,
            "y":y 
        }
    response = requests.post(url_train, json=my_files,data=file)
        
    if response.status_code == 200:
        st.success("File processed successfully!")
        st.dataframe(response.json())
          
