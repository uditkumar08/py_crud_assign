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


# to store data in dict
def store_task(task_id,task):
    data=task.model_dump()
    data["id"]=task_id

# task to be created 

@app.post("/tasks",status_code=201)
def create_task(task:Task):
    global id_cnt
    task_id=id_cnt
    tasks[task_id]=task
    id_cnt=id_cnt+1
    return store_task(task_id,task)


