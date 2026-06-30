from datetime import datetime
from sqlalchemy import func, select
from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    mapped_column
    )
from db import SessionLocal, engine

class Base(DeclarativeBase): 
    pass 


class Task(Base): 
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

Base.metadata.create_all(bind=engine)


def AddTask(title: str) -> None: 
    with SessionLocal() as s: 
        task = Task(title=title)
        s.add(task)
        s.commit()


def completed(task_id: int) -> None: 
    with SessionLocal() as s: 
        task = s.get(Task, task_id)
        if task: 
            task.completed = True
            s.commit()


def delete(task_id: int) -> None: 
    with SessionLocal() as s: 
        task = s.get(Task, task_id)

        if task: 
            s.delete(task)
            s.commit()

    
def show() -> None: 
    with SessionLocal() as s: 
        tasks = s.scalars(select(Task).order_by(Task.created_at)).all()
        return tasks 
 

