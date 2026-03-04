from fastapi import FastAPI, UploadFile, File,Form
import pandas as pd
from graphs import Graph
from predict import light

app = FastAPI()

@app.post("/get_data")
def process(file: UploadFile = File()): 
    df = pd.read_csv(file.file)
    G=Graph()
    df = G.data(df)
    dfs=df.columns.tolist()
    return df.to_dict(orient="records") #dfs
@app.post("/train")
def specific(file: UploadFile = File(),x_axis:str=Form(), y_axis:list=Form()):
    df = pd.read_csv(file.file)
    dfs=df.columns.tolist()
    print(dfs)
    G=Graph()
    df = G.data(df)
    p=light()
    p.clasifer(df)
    predictions=p.lightgbm(x_axis,y_axis)
    data = {
        "predictions": predictions.to_csv()
        }
    return data

