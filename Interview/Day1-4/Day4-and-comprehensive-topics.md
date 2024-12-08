### **Day 4 Notes: Flask Advanced Topics + Mock Practice**

---

## **Part 1: Flask Advanced Topics**

### **1. Flask-SQLAlchemy (Database Integration)**

**Flask-SQLAlchemy** is an Object Relational Mapper (ORM) for integrating relational databases with Flask applications.

#### **Key Concepts**

1. **Database Configuration**:
   - Connect Flask to a database (e.g., SQLite, MySQL, PostgreSQL).
   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///billing.db'
   db = SQLAlchemy(app)
   ```

2. **Defining Models**:
   - Create models representing database tables.
   ```python
   class Customer(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(100), nullable=False)
       email = db.Column(db.String(100), unique=True, nullable=False)
   ```

3. **CRUD Operations**:
   - **Create**:
     ```python
     new_customer = Customer(name="John Doe", email="john@example.com")
     db.session.add(new_customer)
     db.session.commit()
     ```
   - **Read**:
     ```python
     customers = Customer.query.all()
     ```
   - **Update**:
     ```python
     customer = Customer.query.get(1)
     customer.name = "Jane Doe"
     db.session.commit()
     ```
   - **Delete**:
     ```python
     db.session.delete(customer)
     db.session.commit()
     ```

4. **Relationships**:
   - Define relationships between tables.
   ```python
   class Invoice(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
       amount = db.Column(db.Float)
       customer = db.relationship('Customer', backref='invoices')
   ```

---

### **2. Flask-JWT (Token-Based Authentication)**

#### **Installing Flask-JWT-Extended**

```bash
pip install Flask-JWT-Extended
```

#### **Basic Implementation**

```python
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    if username == 'admin':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

# Protected Route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f"Hello, {current_user}")

if __name__ == '__main__':
    app.run(debug=True)
```

#### **Testing with Postman**

1. **Login**:
   - **Endpoint**: `POST /login`  
   - **Body**:  
     ```json
     { "username": "admin" }
     ```
   - **Response**:  
     ```json
     { "access_token": "<your-token>" }
     ```

2. **Access Protected Route**:
   - **Endpoint**: `GET /protected`  
   - **Header**:  
     ```
     Authorization: Bearer <your-token>
     ```

---

### **3. Error Handling in Flask**

#### **Basic Error Handling**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

#### **Custom Error Handling for Routes**

```python
@app.route('/divide')
def divide():
    try:
        result = 10 / 0
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero is not allowed"}), 400
```

---

### **4. Flask Application Structure for a Microservices Project**

**Project Tree**:

```
billing-app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── auth.py
├── config.py
└── run.py
```

1. **`__init__.py`**:
   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy

   db = SQLAlchemy()

   def create_app():
       app = Flask(__name__)
       app.config.from_object('config.Config')
       db.init_app(app)

       from . import routes
       app.register_blueprint(routes.bp)

       return app
   ```

2. **`config.py`**:
   ```python
   class Config:
       SQLALCHEMY_DATABASE_URI = 'sqlite:///billing.db'
       JWT_SECRET_KEY = 'your-secret-key'
   ```

3. **`run.py`**:
   ```python
   from app import create_app

   app = create_app()

   if __name__ == '__main__':
       app.run(debug=True)
   ```

---

## **Part 2: Mock Practice**

### **1. Microservices Integration Task**

**Objective**: Integrate the following services:
1. **Customer Service** (CRUD operations with MongoDB).
2. **Invoice Service** (Fetch and cache invoice data using Redis).

#### **Steps**:
1. **Deploy Both Services**:
   - Use Docker to deploy Flask services.
2. **Test Integration**:
   - Create a customer.
   - Generate an invoice for that customer.
   - Retrieve the invoice and check if caching works.

---

### **2. Quick Coding Challenge**

Solve a **Two-Pointer Technique** problem:

**Problem**:  
Find if a pair of numbers in a sorted array sums to a target.

```python
def find_pair(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# Example
arr = [1, 2, 3, 4, 6]
target = 10
print(find_pair(arr, target))  # Output: (2, 4)
```

---

### **3. Mock Interview Questions**

1. **Scenario-Based**:
   - Design a scalable billing system using AWS services.
2. **Technical**:
   - How would you implement JWT authentication in a microservices architecture?

---

Let me know if you need further clarification or assistance with any of these topics! 😊🚀

### Topics:

1. **Purpose of Using Decorators**  
2. **SQL Queries and Their Usage**  
3. **MongoDB Query Operations**  
4. **Coding Practices for Writing Clean Code**  
5. **Understanding SOLID Principles in Architecture Design**  
6. **ACID Properties (Atomicity, Consistency, Isolation, Durability) in Databases**  
7. **Loosely Coupled vs. Tightly Coupled Systems**  
8. **Generator vs. Iterator: Key Differences**  
9. **How S3 Triggers Work and Example Project with Lambda**  
10. **Benefits of Using API Gateway**  
11. **How AWS Fargate Works as an Alternative to Lambda for Long Execution Times (More than 15 Minutes)**  
12. **Event-Driven Architecture (e.g., API Calls Triggering Billing Updates with Lambda)**  
13. **VPC (Virtual Private Cloud) Overview**  
14. **API Gateway Overview**  
15. **Understanding Lambda Functions in AWS**  
16. **Differences Between JSON Dump, Dumps, Load, and Loads**  
17. **Implementing JWT Authentication in Flask**  
18. **Automated API Testing Practices**  
19. **Introduction to Pytest for Unit Testing**  
20. **WebSockets: Real-time Communication Protocol**  
21. **Handling Concurrency and Parallelism in Python Programming**  
22. **Primitive Data Structures Used in List Data Type**  
23. **Difference Between List and Array Implementations**  
24. **Storing Multiple Data Types in Python**  
25. **Handling and Processing Large Datasets Efficiently**  
26. **Basic Algorithm Practice Questions:**
   - Selection Sort  
   - Bubble Sort  
   - Stack  
   - Queue  
   - Binary Search  
   - Two Pointer Technique  
   - Recursion  
   - Linked List  
   - Binary Search Tree