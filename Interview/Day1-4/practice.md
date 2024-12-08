### Comprehension
```python
doube = [ i*2 for i in range(10)]
print(doube)
keyPair = {i: i * 2 for i in range(10)}
print(keyPair)
```
---
### Lambda
```python
totalSum = lambda x,y: x+y
print(totalSum( 6,6))
```
---

### Abstract Method
```python
from abc import abstractmethod, ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

class Squire(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side

if __name__ == "__main__":
    rec= Rectangle(4,5)
    squire = Squire(5)
    print(f"rec : {rec.area()}")
    # print(f"squire : {squire.area()}")
```
---

### First Class Function
```python
def greeting(name):
    print(f"Hi {name}")

def greetAll(greeting,peoples):
    for people in peoples:
        greeting(people)

if __name__ == "__main__":
    peoples = ["ram", "shaym"]
    greetAll(greeting,peoples)
```

### @property and setter 
```python
from abc import ABC, abstractmethod

class Employee(ABC):

    @property
    @abstractmethod
    def salary(self):
        pass

    @salary.setter
    @abstractmethod
    def salary(self,value):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value>30000:
            print(f"Salary Must be equal or greater that 30000")
        self._salary  =value

if __name__ == "__main__":
    Jhon = FullTimeEmployee("jhon", 50000)
    Rohan = FullTimeEmployee("Rohan", 3000)
    print(Jhon.salary)
    print(Rohan.salary)
    Jhon.salary = 100000
    Jhon.salary = 100
```
---

### Dependency Injection
```python
from abc import ABC, abstractmethod

class Notifire(ABC):
    @abstractmethod
    def send(self, message:str):
        pass

class EmailNotifire(Notifire):
    def send(self, message:str):
        return f"Email Message {message}"

class SmsNotifire(Notifire):
    def send(self, message:str):
        return f"SMS Messsage {message}"

class OrderProcess:
    def __init__(self,notifire:Notifire):
        self.notifire = notifire

    def process_order(self, oder_id:int):
        print(f"Processing order")
        data= self.notifire.send("Order Processed")
        print(f"Status: {data}")


if __name__ == "__main__":
    emailNotifire = EmailNotifire()
    smsNotifire = SmsNotifire()

    order = OrderProcess(emailNotifire)
    order.process_order(123)
    order = OrderProcess(smsNotifire)
    order.process_order(123)
```

---

### Multithreading
```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor
def square_number(number):
    time.sleep(2)
    print(f"Square of Number {number} == {number*number} \n")

def main(numbers):
    for number in range(numbers):
        thread  = threading.Thread(target=square_number,args=(number,) )
        thread.start()

def thread_pool_execuror(numbers):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(square_number, range(numbers))


if __name__ == "__main__":
    main(100)
    thread_pool_execuror(100)
```

---

### Multiprocessing
```python
from multiprocessing import Pool
import time

def square_number(number):
    time.sleep(2)
    print(f"Square of Number {number} == {number*number} \n")

def pool_executor(numbers):
    with Pool(5) as executor:
        executor.map(square_number, range(numbers))


if __name__ == "__main__":
    pool_executor(100)
```

### Asynchronous
```python
from multiprocessing import Pool
import time

def square_number(number):
    time.sleep(2)
    print(f"Square of Number {number} == {number*number} \n")

def pool_executor(numbers):
    for num in range(numbers):
        with Pool(5) as pool:
            result= pool.apply_async(square_number, (num,))
            result.wait()

if __name__ == "__main__":
    pool_executor(10)
```

```python
import asyncio

async def square_number(number):
    await asyncio.sleep(2)
    print(f"Square of Number {number} == {number*number} \n")

async def main(number):
    numbers = range(number)
    tasks = [ square_number(number) for number in numbers]
    await  asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main(10))
```
---

### Decorator
```python
def start_calculation(func):
    def wrapper(numbers):  # accept numbers argument here
        print(f"Starting calculation")
        result = func(numbers)
        print(f"Calculation done")
        return result  # return the result of the function
    return wrapper


@start_calculation
def total_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    result = total_sum([1, 2, 3, 4, 5])
    print(f"Total Sum: {result}")
```
---
### SQL
```SQL
1: 
CREATE TABLE order (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_number VARCHAR(10),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
2: 
CREATE TABLE customer (
    customer_id INT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    PRIMARY KEY (customer_id, email)
);
3:
SELECT Employee.name, Departments.DepartmentName
FROM Employee
INNER JOIN Departments
ON Employee.DepartmentID = Departments.DepartmentID;
4:
SELECT Employee.name, Departments.DepartmentName
FROM Employee
RIGHT JOIN Departments
ON Employee.DepartmentID = Departments.DepartmentID;
5:
SELECT Employee.name, Departments.DepartmentName
FROM Employee
LEFT JOIN Departments
ON Employee.DepartmentID = Departments.DepartmentID;
6:
SELECT Employee.name, Employee.DepartmentID
FROM Employee
WHERE Employee.name = 'RADHE' AND Employee.DepartmentID = 5;
7:
INSERT INTO customers (customer_id, name, email)
VALUES (1, 'John Doe', 'john@example.com');
8:
UPDATE customers
SET email = 'newemail@example.com'
WHERE customer_id = 1;
9:
DELETE FROM customers
WHERE customer_id = 1;

```
---
```python
import sqlite3

connection = sqlite3.connect('company.db')
cursor = connection.cursor()

Query = """
CREATE TABLE customer(
    customer_ID INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
"""
cursor.execute(Query)
connection.commit()
connection.close()
```
---
### MongoDb
```python
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['ecommerce']


db.customer.find({'name':'john'})
db.customer.find()
db.customer.insert_one({"name":'nani', 'email':'sample@gmail.com'})
db.customer.update_one({'name':'nani'}, { '$set': {'email':'nani@email.com'} })
db.customer.delete_one({'name':'nani'})

db.order.aggregate([
    {'$match': {'status':'shipped'}},
    {'$group': {'_id': '$customer_id', "total":{"$sum":"$amount"}}}
])
```
---
### JWT
```python
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'  # Change this to a secure key
jwt = JWTManager(app)

# Login Route to Generate JWT
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
    return jsonify({"message": f"Hello, {current_user}!"})

if __name__ == '__main__':
    app.run(debug=True)

```
---

### WebSockets
```python
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    send(f"Echo: {msg}")

@app.route('/')
def index():
    return "WebSocket Server is running"

if __name__ == '__main__':
    socketio.run(app, debug=True)

```

### Threading
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

```
---
### Multiporcessing
```python
from multiprocessing import Process

def square_numbers():
    for i in range(5):
        print(i * i)

process = Process(target=square_numbers)
process.start()
process.join()

```
---

### ASYNCIO
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())

```
---

### Bubble Sort
```python
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j]= numbers[j], numbers[i]
    return numbers
```
---
### Binary search
```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:
        mid = (left+right)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid]< target:
            left = mid+1
        elif numbers[mid]> target:
            right = mid-1
    return False
```
---

