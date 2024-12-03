from fastapi import APIRouter, Depends
from controllers.user_controller import (
    create_new_user,
    create_new_task,
    read_tasks,
    read_task,
    update_existing_task,
    delete_existing_task,
    create_login
)


# Create a FastAPI APIRouter
user_bp = APIRouter()

user_bp.add_api_route("/create-new-user/", create_new_user, methods=["POST"])
user_bp.add_api_route("/create-login/", create_login, methods=["POST"])
user_bp.add_api_route("/create-new-task/", create_new_task, methods=["POST"])
user_bp.add_api_route("/read-tasks/", read_tasks, methods=["GET"])
user_bp.add_api_route("/read-task/{task_id}", read_task, methods=["GET"])
user_bp.add_api_route("/update-existing-task/{task_id}", update_existing_task, methods=["PUT"])
user_bp.add_api_route("/delete-existing-task/{task_id}", delete_existing_task, methods=["DELETE"])