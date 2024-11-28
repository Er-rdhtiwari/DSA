### Tips to Remember SOLID Principles

1. **Single Responsibility Principle (SRP)**:  
   A class should have one job or reason to change.  
   - Tip: *"One Class, One Responsibility."*  
   - Example: Separate `InvoicePrinter` from `InvoiceCalculator`.

2. **Open/Closed Principle (OCP)**:  
   A class should be open for extension but closed for modification.  
   - Tip: *"Add features, don’t change existing code."*  
   - Example: Use strategy patterns to add new behaviors like payment methods.

3. **Liskov Substitution Principle (LSP)**:  
   Subtypes should be usable in place of their base types without breaking functionality.  
   - Tip: *"Subclasses should behave as expected."*  
   - Example: Avoid breaking expected behavior, like a `Square` subclass altering `Rectangle`.

4. **Interface Segregation Principle (ISP)**:  
   A class should not be forced to implement unused methods.  
   - Tip: *"Small, specific interfaces are better than one large interface."*  
   - Example: Split an `Animal` interface into `FlyingAnimal` and `RunningAnimal`.

5. **Dependency Inversion Principle (DIP)**:  
   Depend on abstractions, not concrete implementations.  
   - Tip: *"Use interfaces for flexibility and decoupling."*  
   - Example: `NotificationService` depends on `INotifier`, not directly on `EmailNotifier`.

---

### Mnemonic:  
**"S.O.L.I.D: Smart Objects Lead In Design."**

By ensuring **small, focused, and decoupled designs**, SOLID principles help create maintainable and scalable systems.

### **SOLID Principles Summary**

The **SOLID** principles are a set of five design principles that help create software that is easier to understand, maintain, and extend. These principles promote **good object-oriented design** practices. Here's a summary based on the discussions above:

---

### **1. Single Responsibility Principle (SRP)**

**Definition**: A class should have only one reason to change, meaning it should only have one job (Primary Responsibility not Secondary Responsibility) or responsibility.

- **Why it matters**: When classes are focused on a single responsibility, they are easier to understand, test, and maintain.
- **Example**: A `PaymentProcessor` class should focus solely on processing payments. If it starts handling logging, reporting, or user authentication, it violates SRP.
  
---

### **2. Open/Closed Principle (OCP)**

**Definition**: Software entities (classes, modules, functions) should be open for extension but closed for modification.

- **Why it matters**: It allows you to extend the behavior of a class without changing its existing code, making it safer to add new features or functionality.
- **Example**: By using **abstract classes** and **polymorphism**, we can add new payment methods (like `PayPalPayment`, `CreditCardPayment`) without changing the core `PaymentService` class, which adheres to OCP.

---

### **3. Liskov Substitution Principle (LSP)**

**Definition**: Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.

- **Why it matters**: It ensures that a subclass can be used interchangeably with its parent class without breaking the system.
- **Example**: In the `PaymentMethod` example, you can replace `CreditCardPayment` with `PayPalPayment` in the `PaymentService` class without any issues because both classes implement the same `process_payment` method from the abstract `PaymentMethod` class.

---

### **4. Interface Segregation Principle (ISP)**

**Definition**: Clients should not be forced to depend on interfaces they do not use.

- **Why it matters**: It reduces the impact of change on clients by ensuring that they are only exposed to the methods they actually need.
- **Example**: Instead of having one massive interface for all types of payment methods, you could break down different operations (e.g., refund, chargeback, capture) into smaller, more specific interfaces that are only implemented when necessary.

---

### **5. Dependency Inversion Principle (DIP)**

**Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions.

- **Why it matters**: It reduces the coupling between high-level and low-level components by introducing abstractions (abstract classes or interfaces). This makes your code more flexible and easier to test.
- **Example**: Instead of directly coupling `PaymentService` to `CreditCardPayment`, `PaymentService` depends on the abstraction `PaymentMethod`. This allows you to easily swap out different payment methods (like `PayPalPayment`) without modifying the `PaymentService`.

---

### **How These Principles Work Together**

- **SRP**: Helps ensure each class is responsible for one thing, making them easier to understand and modify.
- **OCP**: Makes it easy to extend functionality without changing existing code, which is achieved by designing classes with abstraction and polymorphism.
- **LSP**: Ensures that subclasses can be used interchangeably with their parent classes, promoting the reusability and flexibility of code.
- **ISP**: Encourages the design of smaller, specific interfaces that are only implemented as needed, preventing clients from being burdened with irrelevant methods.
- **DIP**: Focuses on decoupling high-level modules from low-level details by depending on abstractions, which makes the system flexible, extensible, and easier to test.

---

### **Example: Putting SOLID Together**

Consider the following example where we apply all SOLID principles to the **PaymentService**:

1. **Single Responsibility Principle (SRP)**:
   - `PaymentService` is responsible for handling payments, not for logging or user management.
2. **Open/Closed Principle (OCP)**:
   - You can add new payment methods (like `CreditCardPayment`, `PayPalPayment`) without modifying the `PaymentService`.
3. **Liskov Substitution Principle (LSP)**:
   - `PaymentService` can work with any subclass of `PaymentMethod` without breaking functionality.
4. **Interface Segregation Principle (ISP)**:
   - Each payment method only implements the `process_payment` method, and additional methods can be added if needed without forcing the implementation of unused methods.
5. **Dependency Inversion Principle (DIP)**:
   - `PaymentService` depends on the abstract class `PaymentMethod`, not concrete classes like `CreditCardPayment`. This allows easy substitution of payment methods and better testing.

---

### **Conclusion**

- The **SOLID** principles encourage designing software that is modular, flexible, and easy to maintain and extend.
- **SRP**, **OCP**, **LSP**, **ISP**, and **DIP** all work together to create a more efficient, maintainable, and scalable system.
- Using these principles in your code makes it easier to adapt to changing requirements, test individual components, and prevent code that is difficult to maintain.

By incorporating SOLID principles into your development practices, you can build robust and future-proof applications that stand the test of time.

Certainly! Below is a simple Python module that demonstrates a **wrong implementation** of the **SOLID principles** followed by the **correct implementation**.

### **Problem Scenario**
Let's imagine we're creating a module for handling different types of **shapes** (e.g., `Circle`, `Rectangle`) and calculating their **area**.

#### **1. Wrong Implementation (Breaking SOLID Principles)**

This initial implementation will violate the **SOLID** principles by having a single class handle all the operations without proper separation of concerns, abstraction, and extensibility.

```python
# Wrong Implementation (Violates SOLID Principles)
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        if shape_type == "circle":
            self.radius = 5
        elif shape_type == "rectangle":
            self.length = 5
            self.width = 10
        else:
            raise ValueError("Unknown shape type")

    def area(self):
        if self.shape_type == "circle":
            return 3.14 * (self.radius ** 2)
        elif self.shape_type == "rectangle":
            return self.length * self.width
        else:
            raise ValueError("Unknown shape type")

# Usage
shape = Shape("circle")
print("Circle Area:", shape.area())

shape = Shape("rectangle")
print("Rectangle Area:", shape.area())
```

### **Issues with the Above Code:**
- **Single Responsibility Principle (SRP)**: `Shape` class is responsible for both the creation of shapes and calculating their area, violating SRP.
- **Open/Closed Principle (OCP)**: To add more shapes (e.g., `Triangle`), we need to modify the `Shape` class.
- **Liskov Substitution Principle (LSP)**: The design does not allow easy extension for new shape classes that could be used interchangeably.
- **Interface Segregation Principle (ISP)**: `Shape` class forces every shape to implement area calculation in a single, monolithic method.
- **Dependency Inversion Principle (DIP)**: The class is tightly coupled to specific shape types (e.g., `circle`, `rectangle`).

---

#### **2. Correct Implementation (SOLID Principles Applied)**

Let's refactor the code to follow **SOLID** principles correctly.

```python
from abc import ABC, abstractmethod

# 1. **Single Responsibility Principle (SRP)**: Create a class for each responsibility.
# 2. **Open/Closed Principle (OCP)**: The code should be open for extension but closed for modification.
# 3. **Liskov Substitution Principle (LSP)**: Subtypes should be substitutable for their base types.
# 4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on methods they don't use.
# 5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules.

# Abstract Base Class (Abstract Interface for Shapes)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Concrete Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Concrete Triangle Class (new shape can be added easily, adhering to OCP)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# High-level module that works with shapes through abstraction (DIP)
class AreaCalculator:
    def __init__(self, shape: Shape):
        self.shape = shape

    def calculate_area(self):
        return self.shape.area()

# Usage
circle = Circle(5)
rectangle = Rectangle(5, 10)
triangle = Triangle(4, 6)

# Dependency Injection: We pass the concrete shape classes to AreaCalculator, following DIP
calculator = AreaCalculator(circle)
print("Circle Area:", calculator.calculate_area())

calculator = AreaCalculator(rectangle)
print("Rectangle Area:", calculator.calculate_area())

calculator = AreaCalculator(triangle)
print("Triangle Area:", calculator.calculate_area())
```

---

### **Explanation of Correct Implementation (SOLID)**

1. **Single Responsibility Principle (SRP)**:
   - The `Circle`, `Rectangle`, and `Triangle` classes are now only responsible for storing shape-specific data and calculating their area.
   - The `AreaCalculator` class is responsible only for calculating the area of any shape.

2. **Open/Closed Principle (OCP)**:
   - To add new shapes (like `Triangle`), we don't need to modify the existing `AreaCalculator` or other shape classes. We simply create a new subclass of `Shape` and implement the `area()` method.

3. **Liskov Substitution Principle (LSP)**:
   - We can replace any shape object (`Circle`, `Rectangle`, `Triangle`) with another shape object in the `AreaCalculator`, and it will still work as expected without breaking functionality.

4. **Interface Segregation Principle (ISP)**:
   - The `Shape` class is now an abstract class that defines only the `area()` method. Each specific shape implements this method without being forced to implement other unrelated methods.

5. **Dependency Inversion Principle (DIP)**:
   - The `AreaCalculator` depends on the abstraction (`Shape`) rather than concrete implementations like `Circle`, `Rectangle`, or `Triangle`. This allows for easy substitution of different shape classes without modifying `AreaCalculator`.

---

### **Summary of the Key Points**

- **SRP**: Each class has one responsibility.
- **OCP**: New shapes can be added without modifying existing code.
- **LSP**: Subclasses (`Circle`, `Rectangle`, `Triangle`) can be used interchangeably.
- **ISP**: The interface is minimal, with only the `area` method being required.
- **DIP**: `AreaCalculator` depends on the abstraction `Shape`, not concrete classes like `Circle` or `Rectangle`.

This design ensures that the system is easy to maintain, extend, and test, following the **SOLID** principles.

Here are some **industry design principles** commonly used in software development, along with Python examples that demonstrate these principles.

---

## 1. **Single Responsibility Principle (SRP)**
**Definition**: A class should have one and only one reason to change. Each class should be responsible for a single piece of functionality.

**Example**:
```python
class Logger:
    """
    Handles logging responsibilities.
    """
    def log(self, message: str):
        print(f"Log: {message}")

class OrderProcessor:
    """
    Handles order processing responsibilities.
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def process_order(self, order_id: int):
        # Order processing logic
        self.logger.log(f"Processing order ID: {order_id}")

# Usage
logger = Logger()
order_processor = OrderProcessor(logger)
order_processor.process_order(123)
```

**Key Takeaway**: The `Logger` handles logging, while `OrderProcessor` deals with order logic, ensuring each class has a single responsibility.

---

## 2. **Open/Closed Principle (OCP)**
**Definition**: Classes should be open for extension but closed for modification.

**Example**:
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def calculate_discount(self, price: float) -> float:
        return price - (price * self.percentage / 100)

class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def checkout(self, price: float) -> float:
        return self.discount_strategy.calculate_discount(price)

# Usage
cart1 = ShoppingCart(NoDiscount())
print(cart1.checkout(100))  # Output: 100

cart2 = ShoppingCart(PercentageDiscount(10))
print(cart2.checkout(100))  # Output: 90
```

**Key Takeaway**: New discount strategies can be added without modifying the existing code.

---

## 3. **Liskov Substitution Principle (LSP)**
**Definition**: Subtypes should be substitutable for their base types without altering the correctness of the program.

**Example**:
```python
class Bird:
    def fly(self):
        return "I can fly"

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly")

def let_bird_fly(bird: Bird):
    print(bird.fly())

# Usage
sparrow = Sparrow()
let_bird_fly(sparrow)  # Output: "I can fly"

penguin = Penguin()
try:
    let_bird_fly(penguin)  # Violates LSP: Raises NotImplementedError
except NotImplementedError as e:
    print(e)
```

**Fix**: Use a more appropriate design, such as introducing an abstract method for flight capability.

---

## 4. **Interface Segregation Principle (ISP)**
**Definition**: A class should not be forced to implement interfaces it doesn’t use.

**Example**:
```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, content: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self, content: str):
        print(f"Printing: {content}")

    def scan(self) -> str:
        return "Scanned document"

class SimplePrinter(Printer):
    def print(self, content: str):
        print(f"Printing: {content}")

# Usage
device = MultiFunctionDevice()
device.print("Hello")
print(device.scan())

printer = SimplePrinter()
printer.print("Simple printer")
```

**Key Takeaway**: Each interface is specific, and classes implement only the interfaces they need.

---

## 5. **Dependency Inversion Principle (DIP)**
**Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Example**:
```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailNotification(NotificationService):
    def send_notification(self, message: str):
        print(f"Email: {message}")

class SMSNotification(NotificationService):
    def send_notification(self, message: str):
        print(f"SMS: {message}")

class UserNotifier:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify(self, message: str):
        self.notification_service.send_notification(message)

# Usage
email_service = EmailNotification()
sms_service = SMSNotification()

notifier = UserNotifier(email_service)
notifier.notify("Your order has been shipped.")  # Output: "Email: Your order has been shipped."

notifier = UserNotifier(sms_service)
notifier.notify("Your order has been delivered.")  # Output: "SMS: Your order has been delivered."
```

**Key Takeaway**: `UserNotifier` depends on an abstraction (`NotificationService`), not concrete implementations.

---

### Additional Principles and Patterns
1. **DRY (Don't Repeat Yourself)**:
   - Consolidate repeated logic into reusable functions or classes.

2. **KISS (Keep It Simple, Stupid)**:
   - Avoid unnecessary complexity. Write code that is easy to understand.

3. **YAGNI (You Aren't Gonna Need It)**:
   - Implement features only when required, avoiding over-engineering.

4. **Factory Pattern**:
   - Use factories for object creation to encapsulate logic.

---

By following these principles, you can create a scalable, maintainable, and clean codebase that adheres to industry standards.