from functools import wraps
import jwt
import os
import logging
from flask import request, jsonify, Response, g
#from config.config import Config
from models.all_models import User
from config.database import get_db
from dotenv import load_dotenv

def decode_jwt(token):
    try:
        token = token.split(" ")[1]  # Split the token in 'Bearer <token>' format
        return jwt.decode(token, str(os.getenv('SECRET_KEY')), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        logging.error("Token has expired")
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        logging.error("Invalid token")
        return {'error': 'Invalid token'}

"""def authenticate_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            logging.warning("Missing Authorization header")
            return Response(
                response='{"message": "Unauthorized - Missing Authorization header"}',
                status=401
            )

        user_info = decode_jwt(auth_header)

        if 'error' in user_info:
            return Response(
                response=f'{{"message": "Unauthorized - {user_info["error"]}"}}',
                status=401
            )

        if 'role' not in user_info or user_info['role'] != 'admin':
            logging.warning("User is not authorized")
            return Response(
                response='{"message": "Unauthorized - User is not authorized"}',
                status=403
            )

        g.user_info = user_info  # Set user information in global `g`
        
        return func(*args, **kwargs)  # Proceed to the actual function

    return wrapper"""

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            logging.warning("Missing Authorization header")
            return Response(
                response='{"message": "Unauthorized - Missing Authorization header"}',
                status=401
            )
        print("task:",token)
        try:
            data = decode_jwt(token)
            print("data:",data)
            if 'error' in data:
                print("error ra mama")
                return Response(
                    response=f'{{"message": "Unauthorized - {data["error"]}"}}',
                    status=401
                )
            print("data2:",data)
            current_user = db.query(User).filter(User.username == str(data['username'])).first()
            print("current_user:",current_user)
            # Store user data in session
            #session['current_user_id'] = current_user.id
            #session['current_username'] = current_user.username  

        except:
            print("task2")
            return jsonify({"message": "Token is invalid!"}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not hasattr(current_user, 'role') or current_user.role != 'admin':
            logging.warning("User is not authorized")
            return Response(
                response='{"message": "Unauthorized - User is not authorized"}',
                status=403
            )
        return f(current_user, *args, **kwargs)
    return decorated

def user_or_admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not hasattr(current_user, 'role'):
            logging.warning("User is not authorized")
            return Response(
                response='{"message": "Unauthorized - User is not authorized"}',
                status=403
            )
        return f(current_user, *args, **kwargs)
    return decorated