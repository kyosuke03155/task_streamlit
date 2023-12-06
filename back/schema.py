from pydantic import BaseModel, Field
from datetime import date, timedelta

# タスク参照定義
class TaskSchema (BaseModel):
    task_id: int = Field()
    content: str = Field(max_length=100)
    is_completed: bool = Field()
    priority: int = Field()
    deadline: date = Field()
    class Config:
        orm_mode = True

# タスク登録定義
class TaskCreatingSchema (BaseModel):
    content: str = Field(max_length=100)
    priority: int = Field()
    is_completed: bool = Field(default=False)
    deadline: date = Field(default=date.today() + timedelta(days=7))

    
    #一週間後
    deadline: date = date.today() + timedelta(days=7) 
    class Config:
        orm_mode = True
