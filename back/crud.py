from sqlalchemy.orm import Session
from sqlalchemy import case, desc
import model, schema
from datetime import datetime

# タスク一覧取得
def get_tasks(db: Session, skip: int = 0, filter_complete: str="none",filter_priority: str = "none",sort_deadline: str = "none",sort_priority: str = "none", limit: int = 100):
    q = db.query(model.Task)
    filter_priority_dic = {
        "high": 2,
        "middle": 1,
        "low": 0,
    }
    if filter_priority != "none":
        q = q.filter(model.Task.priority == filter_priority_dic[filter_priority])
    if filter_complete == "completed":
        q = q.filter(model.Task.is_completed == True)
    elif filter_complete == "uncompleted":
        q = q.filter(model.Task.is_completed == False)
    if sort_deadline == "asc":
        q = q.order_by(model.Task.deadline.asc())
    elif sort_deadline == "desc":
        q = q.order_by(model.Task.deadline.desc())
    if sort_priority == "asc":
        q = q.order_by(model.Task.priority.asc())
    elif sort_priority == "desc":
        q = q.order_by(model.Task.priority.desc())

    return q.offset(skip).limit(limit).all()

# タスク登録
def create_task(db: Session, task: schema.TaskCreatingSchema):
    db_task = model.Task(content = task.content,  priority = task.priority, deadline = task.deadline)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# タスク削除
def delete_task(db: Session, task_id: int):
    db_task = db.query(model.Task).filter(model.Task.task_id == task_id).one()
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None

# タスク更新
def update_task(db: Session, task_id: int, task: schema.TaskCreatingSchema):
    db_task = db.query(model.Task).filter(model.Task.task_id == task_id).first()
    db_task.is_completed = task.is_completed
    db_task.content = task.content
    db_task.priority = task.priority
    db_task.deadline = task.deadline
    db.commit()
    db.refresh(db_task)
    return db_task