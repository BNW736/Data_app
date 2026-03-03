from fastapi import FastAPI, UploadFile, File
import pandas as pd
from graphs import Graph


app = FastAPI()

@app.post("/get_data")
def process(file: UploadFile = File(...)): 
    df = pd.read_csv(file.file)
    G=Graph()
    df = G.data(df)
    df = df.fillna("") 
    return df.to_dict(orient="records")
    

