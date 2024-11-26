### **Open/Closed Principle (OCP)**

The **Open/Closed Principle** is another one of the five SOLID principles in software design. It states:

> **"Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification."**

This means you should be able to add new functionality to a class without modifying its existing code. This is achieved through **abstraction** and **polymorphism**, ensuring that changes to one part of the code don’t break other parts.

---

### **Why OCP is Important?**
1. **Minimizes Risk**: Existing code remains untouched, reducing the chances of introducing bugs.
2. **Improves Flexibility**: New features can be added easily without altering core functionality.
3. **Encourages Modular Design**: Promotes the use of abstractions and interfaces.

---

### **Examples**

#### **Bad Example (Violating OCP)**
In this example, adding a new shape (e.g., `Triangle`) requires modifying the `AreaCalculator` class, which violates OCP.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius
        else:
            raise ValueError("Unsupported shape")
```

- **Issue**: To add a new shape like `Triangle`, you’d need to modify `AreaCalculator`, violating OCP.

---

#### **Good Example (Following OCP)**
By using **abstraction** and **polymorphism**, you can design a system that supports new shapes without modifying existing code.

```python
from abc import ABC, abstractmethod

# Abstract class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Triangle class (new shape)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# AreaCalculator doesn't need modification
class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()

# Usage
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(6, 7),
]

calculator = AreaCalculator()
for shape in shapes:
    print(f"Area: {calculator.calculate_area(shape)}")
```

---

### **Explanation**
1. **Abstraction**: The `Shape` abstract base class defines a common interface (`area`) for all shapes.
2. **Extension**: New shapes like `Triangle` can be added by creating new subclasses without modifying existing code.
3. **Polymorphism**: The `AreaCalculator` works with any object that adheres to the `Shape` interface.

---

### **Benefits of Following OCP**
- The `AreaCalculator` class does not require modification when adding new shapes.
- Reduces the risk of breaking existing functionality.
- Makes the code more maintainable and scalable.

This approach adheres to the Open/Closed Principle by being open to extension (adding new shapes) but closed to modification (no changes to `AreaCalculator`).

### **What is an Abstract Class?**

An **abstract class** is a class that cannot be instantiated on its own and serves as a blueprint for other classes. It typically contains one or more **abstract methods**, which are methods declared but not implemented in the abstract class. Subclasses inheriting from the abstract class must provide implementations for these abstract methods.

In Python, abstract classes are defined using the `abc` (Abstract Base Class) module.

---

### **Abstract Class for Shapes**

In the example, the abstract class `Shape` serves as a contract for all shapes, ensuring that any class representing a shape (e.g., `Rectangle`, `Circle`, `Triangle`) provides an implementation for the `area` method.

#### **Code Example**
```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of a shape"""
        pass
```

- **Purpose**: The abstract class enforces that every subclass (like `Rectangle`, `Circle`, etc.) implements the `area` method.

---

### **Importance of Abstract Class**

1. **Encapsulation of Common Behavior**:
   - Abstract classes encapsulate shared functionality or behavior that multiple subclasses can inherit.
   - For example, if all shapes had a method to calculate the perimeter, you could define it in the `Shape` abstract class.

2. **Establishing a Contract**:
   - Abstract classes act as a **contract**: any class inheriting from the abstract class must implement the abstract methods.
   - In the example, all shapes must have an `area` method. This ensures a consistent interface for all shapes.

3. **Promotes Extensibility**:
   - You can add new shape types (`Triangle`, `Polygon`, etc.) without modifying the existing `AreaCalculator` class. As long as they inherit from `Shape` and implement `area`, the system remains functional.

4. **Improves Code Organization and Maintainability**:
   - Abstract classes provide a logical structure to the system. Developers can look at the abstract class to understand the expected behavior of all its subclasses.

5. **Supports Polymorphism**:
   - Polymorphism allows code to interact with objects of different subclasses through the common interface provided by the abstract class.
   - For example:
     ```python
     def calculate_area(shape: Shape):
         return shape.area()
     ```
     This function can work with any object that is a subclass of `Shape`, regardless of its specific type.

6. **Prevents Instantiation**:
   - Abstract classes cannot be instantiated directly. This ensures that only meaningful, concrete implementations are used in the code.

---

### **Concrete Example with Abstract Class**

```python
from abc import ABC, abstractmethod

# Abstract class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete implementation for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Concrete implementation for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```

Here:
- `Shape` is the abstract class that defines the `area` method.
- `Rectangle` and `Circle` are concrete subclasses implementing the `area` method.

---

### **Key Points**
- **Abstract Classes**: Serve as a blueprint, ensuring consistency and providing shared functionality.
- **Importance**: Promote code reuse, maintainability, extensibility, and adherence to design principles like Open/Closed Principle.
- **Real-World Analogy**: Think of an abstract class as a form or template. It defines what needs to be done, but the details (implementation) are left to the specific subclasses.

### Specification Design Principle

The **Specification Design Principle** is a behavioral design pattern often used to define and combine business rules or requirements declaratively. It allows you to specify rules or criteria in a reusable and composable way, typically for filtering or validating objects.

The principle revolves around the **Specification Pattern**, where:
- **Specifications** encapsulate business logic or conditions.
- They can be combined using logical operators like AND, OR, and NOT, allowing complex conditions to be built flexibly.

---

### Components of the Specification Pattern
1. **Specification**: Represents a single rule or condition.
2. **Combinators**: Combine multiple specifications (AND, OR, NOT).
3. **Target**: Objects or entities that the specifications are applied to.

---

### Python Implementation of Specification Pattern

**Example Scenario**: Filtering products based on criteria like price, category, and stock availability.

#### Implementation

```python
from abc import ABC, abstractmethod

# Base Specification
class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, item) -> bool:
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)

    def __invert__(self):
        return NotSpecification(self)

# Concrete Specifications
class PriceSpecification(Specification):
    def __init__(self, max_price: float):
        self.max_price = max_price

    def is_satisfied_by(self, item) -> bool:
        return item.price <= self.max_price

class CategorySpecification(Specification):
    def __init__(self, category: str):
        self.category = category

    def is_satisfied_by(self, item) -> bool:
        return item.category == self.category

class InStockSpecification(Specification):
    def is_satisfied_by(self, item) -> bool:
        return item.stock > 0

# Combinators
class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, item) -> bool:
        return self.spec1.is_satisfied_by(item) and self.spec2.is_satisfied_by(item)

class OrSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, item) -> bool:
        return self.spec1.is_satisfied_by(item) or self.spec2.is_satisfied_by(item)

class NotSpecification(Specification):
    def __init__(self, spec):
        self.spec = spec

    def is_satisfied_by(self, item) -> bool:
        return not self.spec.is_satisfied_by(item)

# Product Class
class Product:
    def __init__(self, name: str, price: float, category: str, stock: int):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category}, stock={self.stock})"

# Usage Example
products = [
    Product("Laptop", 1500, "Electronics", 5),
    Product("Phone", 800, "Electronics", 0),
    Product("Shoes", 100, "Fashion", 20),
    Product("Book", 20, "Books", 50),
]

# Specifications
price_spec = PriceSpecification(1000)
category_spec = CategorySpecification("Electronics")
in_stock_spec = InStockSpecification()

# Combine Specifications
electronics_in_stock_spec = category_spec & in_stock_spec
cheap_or_in_stock_spec = price_spec | in_stock_spec

# Filter Products
filtered_electronics_in_stock = [p for p in products if electronics_in_stock_spec.is_satisfied_by(p)]
filtered_cheap_or_in_stock = [p for p in products if cheap_or_in_stock_spec.is_satisfied_by(p)]

print("Electronics in Stock:", filtered_electronics_in_stock)
print("Cheap or In Stock:", filtered_cheap_or_in_stock)
```

---

#### Explanation
1. **Specifications** encapsulate rules for filtering.
2. **Combinators** (`&`, `|`, `~`) allow flexible combinations.
3. **Reusability**: Specifications like `PriceSpecification` can be reused in different combinations.

---

### Test Cases

Using `pytest` to validate the behavior:

```python
import pytest
from product import Product, PriceSpecification, CategorySpecification, InStockSpecification

@pytest.fixture
def products():
    return [
        Product("Laptop", 1500, "Electronics", 5),
        Product("Phone", 800, "Electronics", 0),
        Product("Shoes", 100, "Fashion", 20),
        Product("Book", 20, "Books", 50),
    ]

def test_price_specification(products):
    price_spec = PriceSpecification(1000)
    assert price_spec.is_satisfied_by(products[0]) is False  # Laptop: 1500 > 1000
    assert price_spec.is_satisfied_by(products[1]) is True   # Phone: 800 <= 1000

def test_category_specification(products):
    category_spec = CategorySpecification("Fashion")
    assert category_spec.is_satisfied_by(products[2]) is True  # Shoes are in "Fashion"
    assert category_spec.is_satisfied_by(products[0]) is False  # Laptop is not

def test_in_stock_specification(products):
    in_stock_spec = InStockSpecification()
    assert in_stock_spec.is_satisfied_by(products[0]) is True  # Laptop is in stock
    assert in_stock_spec.is_satisfied_by(products[1]) is False  # Phone is out of stock

def test_combined_specifications(products):
    price_spec = PriceSpecification(1000)
    in_stock_spec = InStockSpecification()

    combined_spec = price_spec & in_stock_spec
    assert combined_spec.is_satisfied_by(products[1]) is True  # Phone: cheap and in stock
    assert combined_spec.is_satisfied_by(products[0]) is False  # Laptop: expensive but in stock
```

---

### Advantages of Specification Design Principle
1. **Composability**: Specifications can be combined in various ways (AND, OR, NOT).
2. **Reusability**: Individual specifications can be reused across different contexts.
3. **Readability**: Makes complex filtering or validation logic easier to understand.

### Disadvantages
1. **Complexity**: Can introduce unnecessary complexity for simple scenarios.
2. **Overhead**: Additional layers of abstraction might affect performance in resource-intensive applications.

---

This pattern is widely used in scenarios requiring flexible rules, like filtering products in e-commerce, access control systems, and data validation pipelines.
