from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field



app= FastAPI()

@app.get("/")
def home():
    return {"msg":"welcome in task manager project"}

tasks={}
id_cnt=1
class Task(BaseModel):
    task:str
    description:str
    is_done:bool

