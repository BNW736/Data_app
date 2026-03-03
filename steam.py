import streamlit as st
import requests

url = "http://127.0.0.1:8000/get_data"

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
            
