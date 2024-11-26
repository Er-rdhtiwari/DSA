### **What is `@abstractmethod`?**

The `@abstractmethod` decorator in Python is part of the `abc` module (Abstract Base Classes). It is used to define **abstract methods** in a class, which:
- **Must be implemented** by any subclass inheriting the abstract class.
- Are declared but **not implemented** in the abstract base class.

An abstract class is a class that cannot be instantiated directly and serves as a blueprint for other classes. By using `@abstractmethod`, we enforce that all derived classes provide specific functionality.

---

### **How `@abstractmethod` Works**

1. **Define a Common Interface**:
   - The abstract method acts as a contract that all subclasses must fulfill.

2. **Prevents Instantiation of Abstract Classes**:
   - You cannot create objects of a class that contains `@abstractmethod`.

3. **Forces Implementation in Subclasses**:
   - If a subclass does not implement all `@abstractmethod` methods, it cannot be instantiated.

---

### **Example of `@abstractmethod`**

#### **Abstract Class Example**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """This method must be implemented by all subclasses."""
        pass

# Subclass implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Subclass implementing the abstract method
class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Abstract class cannot be instantiated
animal = Animal()  # Raises TypeError: Can't instantiate abstract class Animal
```

---

### **Relation of `@abstractmethod` to SOLID Principles**

The `@abstractmethod` decorator aligns closely with several SOLID principles:

#### **1. Single Responsibility Principle (SRP)**:
- **How it helps**:
  - By defining abstract methods, it ensures that each subclass implements only the behavior specific to its responsibility.
- **Example**:
  - In the `Animal` abstract class, `make_sound` is the single responsibility for all subclasses. Each subclass (e.g., `Dog`, `Cat`) only implements the method relevant to itself.

#### **2. Open/Closed Principle (OCP)**:
- **How it helps**:
  - Abstract methods enable adding new functionality (new subclasses) without modifying the existing base class or interface.
- **Example**:
  - Adding a new class `Cow` with a specific implementation of `make_sound` does not require modifying the `Animal` base class.

#### **3. Liskov Substitution Principle (LSP)**:
- **How it helps**:
  - Subclasses that implement the `@abstractmethod` can substitute their parent class in any context where the parent class is expected.
- **Example**:
  - A function that works with `Animal` objects can seamlessly handle `Dog`, `Cat`, or `Cow`.

#### **4. Dependency Inversion Principle (DIP)**:
- **How it helps**:
  - Encourages depending on abstractions (abstract classes) rather than concrete implementations.
- **Example**:
  - Functions or modules interacting with `Animal` rely on the abstract `make_sound` method, not the specific implementation of `Dog` or `Cat`.

---

### **Practical Example Related to SOLID Principles**

#### **Abstract Class and Subclasses**
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method to process payment."""
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing bank transfer payment of ${amount}"
```

#### **Using Dependency Inversion**
```python
def process_payment(payment_processor: PaymentProcessor, amount: float):
    print(payment_processor.process_payment(amount))

# Example usage
payment_methods = [CreditCardPayment(), PayPalPayment(), BankTransferPayment()]
for payment_method in payment_methods:
    process_payment(payment_method, 100.0)
```

**Output**:
```
Processing credit card payment of $100.0
Processing PayPal payment of $100.0
Processing bank transfer payment of $100.0
```

---

### **Benefits of `@abstractmethod` in Relation to SOLID**
1. **Encapsulation of Behavior**:
   - Abstract methods encapsulate common behavior in the base class while enforcing customization in subclasses.

2. **Reduces Code Coupling**:
   - Programs rely on abstractions (`ABC` and `@abstractmethod`) rather than specific implementations.

3. **Improves Extensibility**:
   - Adheres to OCP and LSP, allowing new functionalities to be added easily while maintaining compatibility with existing code.

---

### **Test Cases for Abstract Methods**

#### **Testing PaymentProcessor**
```python
import pytest

def test_credit_card_payment():
    payment = CreditCardPayment()
    assert payment.process_payment(100) == "Processing credit card payment of $100"

def test_paypal_payment():
    payment = PayPalPayment()
    assert payment.process_payment(100) == "Processing PayPal payment of $100"

def test_bank_transfer_payment():
    payment = BankTransferPayment()
    assert payment.process_payment(100) == "Processing bank transfer payment of $100"

def test_abstract_class_instantiation():
    with pytest.raises(TypeError):
        PaymentProcessor()  # Abstract class cannot be instantiated
```

---

### **Summary**
- **What is `@abstractmethod`?**:
  - A decorator to define methods in an abstract class that subclasses **must implement**.
- **Why is it useful?**:
  - Enforces a contract or blueprint for subclasses.
  - Ensures consistency across different implementations.
- **Relation to SOLID**:
  - Strongly aligns with OCP, LSP, and DIP by promoting abstraction, extensibility, and substitutability.
- **Practical Use**:
  - Common in scenarios like payment gateways, file handlers, database adapters, etc., where multiple implementations share the same interface.

This makes `@abstractmethod` a critical tool in designing modular, maintainable, and extensible systems.

### Why Use `@property` Decorator in Python?

The `@property` decorator in Python is used to define methods that act like attributes. It allows for encapsulation and controlled access to an object's attributes while providing a clean interface. 

---

### Benefits of Using `@property`
1. **Encapsulation**:
   - Enables control over how attributes are accessed or modified without exposing them directly.
   
2. **Readability**:
   - Simplifies access to methods by allowing them to be accessed like attributes.
   
3. **Backward Compatibility**:
   - You can refactor attributes into methods without breaking the interface.

4. **Data Validation**:
   - Enables validation of values before setting them.

---

### Common Mistakes to Avoid

1. **Not Using Setter/Getter Properly**:
   - Forgetting to define a setter or getter when needed leads to incomplete encapsulation.

2. **Exposing Internal Logic**:
   - Overloading `@property` methods with too much logic can reduce clarity.

3. **Confusion with Regular Methods**:
   - Treating `@property` as a method rather than an attribute.

4. **Accessing a Property in `__init__`**:
   - Accessing a property that depends on attributes not yet initialized can cause errors.

5. **Overuse**:
   - Using `@property` for every attribute unnecessarily increases complexity.

---

### Relation Between `@property` and Abstract Methods

- **Difference**:
  - The `@property` decorator is used for implementing getters, setters, and deleters for an attribute.
  - Abstract methods (via `@abstractmethod`) enforce method implementation in subclasses and are part of the `abc` module.

- **Relation**:
  - They can work together. For example, abstract properties can enforce the implementation of specific getter or setter behaviors in subclasses.

---

### Python Code Example with `@property`

#### Code Implementation

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Abstract base class for employees.
    """

    @property
    @abstractmethod
    def salary(self):
        pass

    @salary.setter
    @abstractmethod
    def salary(self, value):
        pass


class FullTimeEmployee(Employee):
    """
    Represents a full-time employee.
    """

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 30000:
            raise ValueError("Salary must be at least $30,000 for full-time employees.")
        self._salary = value

# Usage
employee = FullTimeEmployee("John Doe", 50000)
print(employee.salary)  # Output: 50000

employee.salary = 60000
print(employee.salary)  # Output: 60000

try:
    employee.salary = 25000  # Should raise ValueError
except ValueError as e:
    print(e)
```

---

### Test Cases with `pytest`

#### Test Code

```python
import pytest
from employee import FullTimeEmployee

def test_salary_getter():
    emp = FullTimeEmployee("Alice", 50000)
    assert emp.salary == 50000

def test_salary_setter():
    emp = FullTimeEmployee("Alice", 50000)
    emp.salary = 60000
    assert emp.salary == 60000

def test_salary_validation():
    emp = FullTimeEmployee("Alice", 50000)
    with pytest.raises(ValueError):
        emp.salary = 25000  # Salary below 30,000 should raise ValueError
```

---

### Key Points to Remember
1. Use `@property` for controlled access to private attributes.
2. Implement both `getter` and `setter` where needed for encapsulation and validation.
3. Avoid using `@property` for attributes that don’t require control logic.
4. Use `@property` with `@abstractmethod` when defining abstract properties in a base class.

This provides a clean, encapsulated, and extensible design for class attributes.

### Execution Order of `@property` and `@setter`

The execution flow for a property and its setter in Python works like this:

1. **`@property` Decorator**:  
   - When an attribute is accessed, the method decorated with `@property` (getter) is executed.

2. **`@<property_name>.setter` Decorator**:  
   - When an attribute is assigned a value, the setter method is executed.

3. **Encapsulation**:  
   - Both the getter and setter operate on private attributes (commonly prefixed with `_`) of the object.

---

### Execution Flow in the Example

#### The Class Code

```python
class FullTimeEmployee:
    """
    Represents a full-time employee.
    """

    def __init__(self, name, salary):
        self._name = name  # Private attribute
        self._salary = salary  # Private attribute

    @property
    def salary(self):
        print("Getter for salary called")
        return self._salary

    @salary.setter
    def salary(self, value):
        print("Setter for salary called")
        if value < 30000:
            raise ValueError("Salary must be at least $30,000 for full-time employees.")
        self._salary = value

# Usage
employee = FullTimeEmployee("John Doe", 50000)
print(employee.salary)  # Access salary (getter)

employee.salary = 60000  # Assign a new value (setter)

try:
    employee.salary = 25000  # Attempt to set an invalid value (setter with exception)
except ValueError as e:
    print(e)
```

---

#### Execution Trace

Here’s the order of operations:

1. **Object Initialization (`__init__`)**:
   - `self._salary = salary` initializes the private attribute `_salary` directly.  
   - At this stage, the `@property` or setter methods are **not called** because `_salary` is directly assigned.

2. **Accessing the Property (`print(employee.salary)`)**:
   - The `@property` decorated method (`salary`) is executed.
   - Output:
     ```plaintext
     Getter for salary called
     50000
     ```

3. **Setting the Property (`employee.salary = 60000`)**:
   - The `@salary.setter` method is executed because the `salary` attribute is assigned a new value.
   - The setter validates the input (checks if it is >= 30000) and updates `_salary` if valid.
   - Output:
     ```plaintext
     Setter for salary called
     ```

4. **Attempting to Set an Invalid Value (`employee.salary = 25000`)**:
   - The `@salary.setter` method is called.
   - The input fails validation (`value < 30000`), so a `ValueError` is raised.
   - Output:
     ```plaintext
     Setter for salary called
     Salary must be at least $30,000 for full-time employees.
     ```

---

#### Full Execution Output

```plaintext
Getter for salary called
50000
Setter for salary called
Setter for salary called
Salary must be at least $30,000 for full-time employees.
```

---

### Key Points on Execution Flow

1. **Direct Access to Private Attributes**:
   - Inside `__init__`, attributes like `_salary` are directly set without invoking the setter.

2. **Getter Execution**:
   - Accessing `employee.salary` invokes the `@property` method.

3. **Setter Execution**:
   - Assigning a value to `employee.salary` invokes the `@salary.setter` method.

4. **Validation in Setter**:
   - The setter ensures only valid values are assigned to `_salary`.

---

### Test the Flow Dynamically

To better visualize the execution order, you can add debugging statements in the getter and setter, as shown above (`print` statements like "Getter called" or "Setter called"). This makes it easy to see when each part is executed during runtime.
