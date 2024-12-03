from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.database import Base
from pydantic import BaseModel
from typing import List, Optional

# SQLAlchemy Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    role = Column(String(50), nullable=False, default='user')
    #is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")

    # Custom to_dict for User
    def user_to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            "tasks": [task.task_to_dict() for task in self.tasks]  # Include related tasks
        }


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(100), index=True)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")

    # Custom to_dict for Task
    def task_to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "owner_id": self.owner_id
        }

"""
One-to-Many Relationship Between User and Task
tasks = relationship("Task", back_populates="owner")
tasks =:
Represents a collection of all tasks assigned to a user.

relationship("Task", ...):
Establishes a one-to-many relationship between the User model and the Task model.

Each User can have multiple tasks, but each Task belongs to only one User.
back_populates="owner":

Creates a bidirectional relationship.
Each Task can reference the associated User via the owner attribute.

owner = relationship("User", back_populates="tasks")
owner =:
Represents the user (owner) associated with a specific task.

relationship("User", ...):
Establishes a many-to-one relationship between the Task model and the User model.

Each Task is owned by one User.
back_populates="tasks":

Creates a bidirectional relationship.
Each User can reference all their associated tasks via the tasks attribute.

"""
