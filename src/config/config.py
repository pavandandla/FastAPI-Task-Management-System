import os
from dotenv import load_dotenv
import pymysql

pymysql.install_as_MySQLdb()  # Ensure mysqlclient works with pymysql
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Allow HTTP traffic for local dev

load_dotenv()  # Load environment variables from a .env file

class Config:
    #SECRET_KEY = os.getenv('SECRET_KEY')
    ##JWT_ALGORITHM = 'HS256'  # Algorithm for JWT
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')  # e.g. "mysql+pymysql://username:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

