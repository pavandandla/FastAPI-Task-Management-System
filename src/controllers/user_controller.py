from fastapi import Depends, Request
from sqlalchemy.orm import Session
from models.all_models import User
from services.user_role_services import create_task, get_tasks, get_task, update_task, delete_task, create_user,login
from config.database import get_db, Base
from pydantic import BaseModel
from middlewares import token_required, admin_required , user_or_admin_required

async def create_new_user(request: Request,db: Session = Depends(get_db)):
    form_data = await request.form()
    return await create_user(db, form_data)


@token_required
async def create_new_task(current_user,request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await create_task(db, form_data, username=current_user.username)

async def create_login(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    print(form_data)
    return await login(db, form_data)

@token_required
@admin_required
async def read_tasks(db: Session = Depends(get_db)):
    return await get_tasks(db)

async def read_task(task_id: int, db: Session = Depends(get_db)):
    return await get_task(db, task_id)

async def update_existing_task(task_id: int, request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    return await update_task(db, task_id, form_data)

async def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    return await delete_task(db, task_id)
