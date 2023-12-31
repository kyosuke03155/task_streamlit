from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, index=True)
    is_completed = Column(Boolean, default=False)
    deadline = Column(DateTime)
    priority = Column(Integer, default=1)


