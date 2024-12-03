from sqlalchemy.orm import Session
import jwt
import os
from dotenv import load_dotenv 
from models.all_models import Task, User#, UserCreate, TaskBase, TaskCreate, TaskUpdate
from flask_bcrypt import Bcrypt  # Ensure you have the correct import
bcrypt = Bcrypt()



async def create_task(db: Session, form_data, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return {
            "status": "failed",
            "statusCode": 404,
            "message": "User not found"
        }

    # Create a new task based on provided form data
    db_task = Task(
        title=form_data.get("title"),  # Get title from form_data or None
        description=form_data.get("description"),  # Get description from form_data or None
        completed=form_data.get("completed") == 'true',  # Convert to boolean
        owner_id=user.id
    )

    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return {
            "status": "success",
            "statusCode": 201,
            "message": "Task created successfully",
            "data": db_task.task_to_dict()
        }
    except Exception as e:
        return {
            "status": "failed",
            "statusCode": 500,
            "message": "Failed to create task",
            "error": str(e)
        }

async def get_tasks(db: Session):
    tasks = db.query(Task).all()
    if not tasks:
        return {
            "status": "failed",
            "statusCode": 404,
            "message": "No tasks found"
        }
    return {
        "status": "success",
        "statusCode": 200,
        "data": [task.task_to_dict() for task in tasks]
    }

async def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {
            "status": "failed",
            "statusCode": 404,
            "message": "Task not found"
        }
    return {
        "status": "success",
        "statusCode": 200,
        "data": task.task_to_dict()
    }

async def update_task(db: Session, task_id: int, form_data):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return {
            "status": "failed",
            "statusCode": 404,
            "message": "Task not found"
        }

    # Update only the fields that are provided
    if "title" in form_data:
        db_task.title = form_data["title"]
    if "description" in form_data:
        db_task.description = form_data.get("description", db_task.description)  # Keep current description if not provided
    if "completed" in form_data:
        db_task.completed = form_data.get("completed") == 'true'  # Convert to boolean

    db.commit()
    db.refresh(db_task)
    return {
        "status": "success",
        "statusCode": 200,
        "message": "Task updated successfully",
        "data": db_task.task_to_dict()
    }

async def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return {
            "status": "failed",
            "statusCode": 404,
            "message": "Task not found"
        }
    db.delete(db_task)
    db.commit()
    return {
        "status": "success",
        "statusCode": 200,
        "message": "Task deleted successfully"
    }

async def create_user(db: Session, form_data):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.username == form_data['username']).first()
    if existing_user:
        return {
            "status": "failed",
            "statusCode": 409,  # Conflict
            "message": "User already exists",
        }

    try:
        hashed_password = bcrypt.generate_password_hash(form_data['password']).decode('utf-8')
        
        db_user = User(username=form_data['username'], hashed_password=hashed_password,role=form_data['role'])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {
            "status": "success",
            "statusCode": 201,
            "message": "User created successfully",
            "data": db_user.user_to_dict()
        }
    except Exception as e:
        return {
            "status": "failed",
            "statusCode": 500,
            "message": "Failed to create user",
            "error": str(e)
        }

async def login(db: Session,form_data):
    try:
        if "username" in form_data and "password" in form_data:
            print(form_data)
            user =  db.query(User).filter(User.username == form_data['username']).first()
            if user and bcrypt.check_password_hash(user.hashed_password, form_data["password"]):
                # Include role and username in the token
                token_Data = {
                    'role': user.role,
                    'username': user.username,
                    'id': user.id
                }
                #print("id===>",user.id)
                
                # Encode the token using JWT
                token = jwt.encode(token_Data, str(os.getenv('SECRET_KEY')) , algorithm='HS256')

                print("token===>",token)
               
                return {'message':f"Login Successful.Welcome,{user.username}!", 'status': "success", "statusCode": 200, "token": token}, 200
            else:
                return {'status': "failed", "statusCode": 401, "message": "Invalid credentials!"}, 401
        else:
            return {'status': "failed", "statusCode": 400, "message": "Email and password are required"}, 400
    except Exception as e:
        return {'status': "failed", "statusCode": 500, "message": "Error occurred", "error": str(e)}, 500