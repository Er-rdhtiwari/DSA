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

### 