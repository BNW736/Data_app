from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
from graphs import Graph
from predict import light
import logging

app = FastAPI()

@app.post("/get_data")
def process(file: UploadFile = File(...)): 
    df = pd.read_csv(file.file)
    G = Graph()
    df = G.data(df)
    return df.to_dict(orient="records") 

@app.post("/train")
def specific(
    file: UploadFile = File(), 
    x_axis: str = Form(), 
    y_axis: str = Form(),
    model: str=Form()
    ):
    
    df = pd.read_csv(file.file, thousands=',')
    
    logging.info("Available Columns:", df.columns.tolist())
    
    G = Graph()
    df = G.data(df)
    
    x_list = []
    rough_list = x_axis.split(",")

    for feature in rough_list:
        cleaned_feature = feature.strip()
        x_list.append(cleaned_feature)
    p = light()
    p.clasifer(df,x_list,y_axis)
    if model=="lightgbm":
        predictions = p.lightgbm()
    if model=="catboot":
        predictions=p.catboot()
    if model=="tensor":
        predictions=p.tenser()
    data = {
        "predictions": predictions.tolist() 
    }
    return data