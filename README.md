

# **FastAPI Task Management System**

## **Description**

The **FastAPI Task Management System** is a powerful API built with **FastAPI** that allows users to create, update, delete, and track tasks. It includes user authentication, task assignment, and management features, offering a smooth and scalable solution for task tracking. This API uses **SQLite** or **MySQL** for data storage and incorporates modern practices for security, scalability, and performance.



## **Features**

- **Performance**
    
    - **FastAPI's async capabilities** provide high performance and low latency for fast responses.
    - **SQLAlchemy's efficient query optimization** for handling complex database queries seamlessly.
- **Security**
    
    - **JWT authentication** for secure user login and token-based authorization.
    - **Bcrypt password hashing** for storing passwords securely in the database.
    - **SQL injection protection** through the use of ORM (SQLAlchemy).
- **Scalability**
    
    - **Modular architecture**: Each feature is broken into separate modules for easy scalability and maintenance.
    - **Dependency injection**: Used for injecting dependencies, improving modularity and testability.
    - **Separate service layer**: To separate business logic from route definitions.
- **Maintainability**
    
    - **Clear project structure** for easy understanding and management of the codebase.
    - **Separation of concerns**: Ensures that each part of the application has a clear responsibility.
    - **Configuration management** with environment variables and configuration files for better flexibility.


## Prerequisites

- Python 3.9+
- pip
- Virtual environment support
## **Libraries Used**

- **FastAPI** 
- **SQLAlchemy** 
- **SQLite/MySQL** 
- **JWT**
- **Bcrypt** 
- **Python-dotenv** 



## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/pavandandla/FastAPI-Task-Management-System.git
cd FastAPI-Task-Management-System
```



### **2. Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```



### **3. Install Dependencies**

```bash
pip install -r src/requirements.txt
```



### **4. Configure Environment Variables**

Create a `.env` file in the root directory with the following configuration:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=mysql://username:password@localhost/db_name
JWT_SECRET_KEY=your_jwt_secret_key
FLASK_ENV=development
```

- **SECRET_KEY**: A key for securely signing JWT tokens.
- **DATABASE_URL**: MySQL connection string or SQLite file path.
- **JWT_SECRET_KEY**: Key used for encoding and decoding JWT tokens.
- **FLASK_ENV**: Set to `development` for debugging.



### **5. Set Up the Database**

Run the following command to initialize the database and create necessary tables:

```bash
python src/init_db.py
```



### **6. Run the Application**

To run the FastAPI application, execute:

```bash
uvicorn src.app:app --reload
```

The application will be available at: `http://127.0.0.1:8000`





## **Example Workflow**

1. **User Registration and Authentication**  
    Users can register and log in using the `/register` and `/login` endpoints. Upon successful login, they receive a JWT token for authentication.
    
2. **Task Management**  
    Users can create, update, delete, and view tasks. Tasks are associated with users, allowing users to track and manage their tasks easily.
    
3. **User and Task Assignment**  
    Tasks can be assigned to specific users, and users can view all the tasks assigned to them via the `/tasks/user/{user_id}` endpoint.
    





## **Environment Configuration**

Example `.env` file:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=mysql://username:password@localhost/db_name
JWT_SECRET_KEY=your_jwt_secret_key
```



## **Contact**

For questions, suggestions, or issues, contact:

- GitHub: [pavandandla](https://github.com/pavandandla)
