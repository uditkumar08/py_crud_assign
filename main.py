from fastapi import FastAPI,HTTPException
from pydantic import BaseModel



app= FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

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
    return data

# task to be created 

@app.post("/tasks",status_code=201)
def create_task(task:Task):
    global id_cnt
    task_id=id_cnt
    tasks[task_id]=task
    id_cnt=id_cnt+1
    return store_task(task_id,task)


# retrieve all task

@app.get("/tasks")
def get_tasks():
    result=[]
    for task_id,task in tasks.items():
        result.append(store_task(task_id,task))
    return result

# get single by id one on one
@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Task not found")
    return store_task(task_id, tasks[task_id])

# update 
@app.put("/tasks/{task_id}")
def update_task(task_id:int,task:Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Task not found")
    tasks[task_id]=task
    return store_task(task_id, task)


# Delete
@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message":"Task deleted"}