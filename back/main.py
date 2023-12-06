from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import model, schema, crud
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 　タスク取得
@app.get("/tasks", response_model=List[schema.TaskSchema])
async def read_tasks(skip: int = 0, limit: int = 100, filter_complete: str = "全て",filter_priority: str = "全て",sort_deadline: str = "none",sort_priority: str = "none",db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip,filter_priority=filter_priority,filter_complete=filter_complete,sort_deadline=sort_deadline,sort_priority=sort_priority ,limit=limit)
    return tasks

#　タスク登録
@app.post("/tasks", response_model=schema.TaskSchema)
async def create_task(task: schema.TaskCreatingSchema, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

#　タスク削除
@app.delete("/tasks/{task_id}", response_model=schema.TaskSchema)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db=db, task_id=task_id)

# タスク更新
@app.put("/tasks/{task_id}", response_model=schema.TaskSchema)
async def update_task(task_id: int, task: schema.TaskCreatingSchema, db: Session = Depends(get_db)):
    return crud.update_task(db=db, task_id=task_id, task=task)
