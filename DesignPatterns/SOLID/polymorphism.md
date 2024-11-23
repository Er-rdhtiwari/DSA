### **What is Polymorphism?**

Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common base class. It enables a single interface to represent different types of objects, and methods in derived classes can override methods in the base class while maintaining the same interface.

In Greek, "polymorphism" means "many shapes," and it refers to the ability of different objects to respond to the same method call in their unique way.

---

### **Importance of Polymorphism in OOP**
1. **Promotes Code Reusability**: Enables writing generic code that works with different object types.
2. **Enhances Maintainability**: Reduces duplication by using a common interface or abstract class.
3. **Supports Extensibility**: Makes it easier to add new types of objects without modifying existing code.
4. **Tightly Coupled to SOLID Principles**:
   - **Open/Closed Principle (OCP)**: Polymorphism allows extending a system's functionality without modifying its code.
   - **Liskov Substitution Principle (LSP)**: Polymorphism ensures that a subclass can replace its parent class without breaking the system.

---

### **Types of Polymorphism in Python**
1. **Compile-Time Polymorphism** (Method Overloading): Not natively supported in Python but achievable through default arguments or `*args`/`**kwargs`.
2. **Run-Time Polymorphism** (Method Overriding): Supported through inheritance and dynamic method resolution.

---

### **Polymorphism with Python Code Example**

#### **Example: Polymorphism with Inheritance**
```python
from abc import ABC, abstractmethod

# Abstract class (common interface)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Concrete implementations
class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

# Polymorphic behavior
def animal_sound(animal: Animal):
    return animal.make_sound()
```

#### **Usage Example**
```python
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__} sound: {animal_sound(animal)}")
```

**Output**:
```
Dog sound: Bark
Cat sound: Meow
Cow sound: Moo
```

---

### **Polymorphism Without Inheritance**

Polymorphism can also be achieved without inheritance, using duck typing. Python follows the "duck typing" philosophy: **"If it walks like a duck and quacks like a duck, it must be a duck."**

```python
class Car:
    def start(self):
        return "Car engine starting"

class Boat:
    def start(self):
        return "Boat engine starting"

def start_vehicle(vehicle):
    return vehicle.start()

# Using duck typing
vehicles = [Car(), Boat()]
for vehicle in vehicles:
    print(start_vehicle(vehicle))
```

**Output**:
```
Car engine starting
Boat engine starting
```

---

### **Test Cases for Polymorphism**

#### **Unit Test Example with `pytest`**
```python
import pytest

# Polymorphism via inheritance
def test_dog_sound():
    dog = Dog()
    assert dog.make_sound() == "Bark"

def test_cat_sound():
    cat = Cat()
    assert cat.make_sound() == "Meow"

def test_cow_sound():
    cow = Cow()
    assert cow.make_sound() == "Moo"

def test_animal_sound():
    animals = [Dog(), Cat(), Cow()]
    sounds = [animal_sound(animal) for animal in animals]
    assert sounds == ["Bark", "Meow", "Moo"]

# Polymorphism via duck typing
def test_duck_typing():
    class Plane:
        def start(self):
            return "Plane engine starting"

    plane = Plane()
    assert start_vehicle(plane) == "Plane engine starting"
```

---

### **Polymorphism and SOLID Principles**

#### **Relation to SOLID Principles**
1. **Single Responsibility Principle (SRP)**:
   - Polymorphism helps keep responsibilities isolated by defining clear interfaces for different behaviors.
   
2. **Open/Closed Principle (OCP)**:
   - Polymorphism allows extending functionality without modifying the base code. For example, adding a new `Animal` subclass like `Bird` doesn’t require changes to `animal_sound`.

3. **Liskov Substitution Principle (LSP)**:
   - Polymorphism ensures that objects of derived classes can replace objects of the base class without breaking the system.

4. **Interface Segregation Principle (ISP)**:
   - Polymorphism allows creating smaller, specific interfaces that each subclass can implement.

5. **Dependency Inversion Principle (DIP)**:
   - By programming to an interface or abstract class, polymorphism allows high-level modules to remain independent of low-level implementations.

---

### **Summary**

- **Definition**: Polymorphism allows objects of different classes to be treated uniformly, adhering to a common interface or behavior.
- **Importance**: Enhances code flexibility, maintainability, and extensibility.
- **Relation to SOLID**: Polymorphism is a cornerstone of OOP and directly supports SOLID principles, especially OCP, LSP, and DIP.
- **Example**: You can achieve polymorphism through inheritance or duck typing in Python, and test it with common scenarios to ensure flexibility and correctness in your design.

Polymorphism is a **key enabler of SOLID design principles**, making it an essential concept for clean, extensible, and maintainable codebases.