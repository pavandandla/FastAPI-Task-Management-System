from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load database URL from environment variables
#DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URI')
DATABASE_URL="mysql+pymysql://root:Pavan%4012@localhost/registration"
# SQLAlchemy engine and session setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Function to initialize the database and create tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency to get a database session for request handling
def get_db():
    db = SessionLocal()
    try:
        yield db  # Yield session to the route handler
    finally:
        db.close()  # Ensure session is closed after the request