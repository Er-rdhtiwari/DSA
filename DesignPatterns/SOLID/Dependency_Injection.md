s### Dependency Injection (DI) in Python

**Dependency Injection (DI)** is a design pattern where an object receives its dependencies (objects it needs to function) from an external source rather than creating them internally. This promotes flexibility, testability, and adherence to SOLID principles.

---

### Relationship with SOLID Principles

- **Dependency Inversion Principle (DIP)**:
  - DI directly supports DIP by ensuring high-level modules depend on abstractions (e.g., interfaces) rather than low-level implementations.
  
- **Single Responsibility Principle (SRP)**:
  - DI separates the responsibility of creating dependencies from their usage.

---

### Advantages of Dependency Injection
1. **Improved Testability**: Dependencies can be mocked or replaced in unit tests.
2. **Flexibility**: Makes it easy to swap implementations (e.g., switching between a file-based and database-based repository).
3. **Loose Coupling**: Objects are not tightly coupled to specific implementations.

---

### Common Mistakes to Avoid
1. **Injecting Too Many Dependencies**:
   - Keep the number of dependencies minimal to avoid complex constructors.
2. **Using Global State for Dependencies**:
   - Avoid tightly coupling DI with singletons or global variables.
3. **Not Using Abstractions**:
   - Injecting concrete implementations directly reduces flexibility.

---

### Python Example: Dependency Injection

#### Implementation

```python
from abc import ABC, abstractmethod


# Abstract class (Dependency)
class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Concrete implementations
class EmailNotification(NotificationService):
    def send(self, message: str):
        print(f"Sending Email: {message}")


class SMSNotification(NotificationService):
    def send(self, message: str):
        print(f"Sending SMS: {message}")


# High-level class that depends on the abstraction
class OrderProcessor:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier

    def process_order(self, order_id: int):
        print(f"Processing order {order_id}")
        self.notifier.send(f"Order {order_id} processed successfully.")


# Dependency Injection in action
email_notifier = EmailNotification()
sms_notifier = SMSNotification()

# Using different notifiers via DI
processor_with_email = OrderProcessor(email_notifier)
processor_with_sms = OrderProcessor(sms_notifier)

# Process orders
processor_with_email.process_order(101)
processor_with_sms.process_order(102)
```

---

#### Test Cases with `pytest`

```python
import pytest
from unittest.mock import MagicMock
from your_module import OrderProcessor, NotificationService


# Mocking the dependency
class MockNotificationService(NotificationService):
    def __init__(self):
        self.sent_messages = []

    def send(self, message: str):
        self.sent_messages.append(message)


def test_order_processor_with_mock_notifier():
    # Arrange
    mock_notifier = MockNotificationService()
    processor = OrderProcessor(mock_notifier)
    
    # Act
    processor.process_order(101)
    
    # Assert
    assert len(mock_notifier.sent_messages) == 1
    assert mock_notifier.sent_messages[0] == "Order 101 processed successfully."


def test_order_processor_with_magic_mock():
    # Arrange
    mock_notifier = MagicMock(spec=NotificationService)
    processor = OrderProcessor(mock_notifier)
    
    # Act
    processor.process_order(101)
    
    # Assert
    mock_notifier.send.assert_called_once_with("Order 101 processed successfully.")
```

---

### Key Points to Remember
1. **Inject Abstractions, Not Implementations**:
   - Depend on interfaces or abstract classes rather than concrete classes.

2. **Constructor Injection**:
   - Inject dependencies via the constructor, as shown in the example.

3. **Testability**:
   - Use mocks or stubs for testing dependencies.

4. **Avoid Overcomplicating**:
   - Only use DI when it simplifies the design or improves testability.

5. **Relation to Frameworks**:
   - Frameworks like `Flask` and `FastAPI` support DI for services or configurations.

---

This approach ensures adherence to SOLID principles, especially DIP, while keeping your code modular and maintainable.

In software design, particularly when discussing the **Dependency Inversion Principle** (one of the SOLID principles) or system architecture, the terms **high-level modules** and **low-level modules** refer to different layers of abstraction and responsibility within a system.

Here’s a clear explanation of each concept with examples:

---

## 🏗️ **High-Level Modules**

- **Definition**: High-level modules are the **abstract components** of a system responsible for defining the core logic, business rules, or high-level policies.
- **Purpose**: They orchestrate and make use of low-level modules to perform specific tasks.
- **Characteristics**:
  - Deal with broader functionalities.
  - Have minimal implementation details.
  - Focus on **what** needs to be done rather than **how** it is done.
  - Are typically more stable and change less frequently.
  - Depend on **interfaces** or **abstractions** rather than concrete implementations.

### Example of a High-Level Module

```python
class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway  # Dependency Injection

    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        self.payment_gateway.make_payment(amount)
```

In this example:
- `PaymentProcessor` is a high-level module that defines the logic for processing payments.
- It delegates the actual payment action to a lower-level module via `payment_gateway`.

---

## 🔧 **Low-Level Modules**

- **Definition**: Low-level modules are the **detailed implementations** that perform specific tasks, often interacting with system resources, libraries, or APIs.
- **Purpose**: Provide concrete functionality to be used by high-level modules.
- **Characteristics**:
  - Handle specific, detailed operations.
  - Tend to change more frequently due to implementation details.
  - Focus on **how** a task is performed.
  - Implement the abstractions defined by high-level modules.

### Example of a Low-Level Module

```python
class StripeGateway:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via Stripe")

class PayPalGateway:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via PayPal")
```

In this example:
- `StripeGateway` and `PayPalGateway` are low-level modules that provide concrete implementations of making payments through Stripe or PayPal.

---

## 🔄 **High-Level and Low-Level Interaction**

Let’s see how high-level and low-level modules interact:

```python
# High-Level Module
class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        self.payment_gateway.make_payment(amount)

# Low-Level Modules
class StripeGateway:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via Stripe")

class PayPalGateway:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via PayPal")

# Using Dependency Injection
stripe_gateway = StripeGateway()
paypal_gateway = PayPalGateway()

processor = PaymentProcessor(stripe_gateway)
processor.process_payment(100)  # Payment via Stripe

processor = PaymentProcessor(paypal_gateway)
processor.process_payment(200)  # Payment via PayPal
```

### Output:

```
Processing payment of $100
Payment of $100 made via Stripe
Processing payment of $200
Payment of $200 made via PayPal
```

---

## 🧩 **Key Differences**

| **Aspect**                | **High-Level Modules**                           | **Low-Level Modules**                               |
|----------------------------|--------------------------------------------------|-----------------------------------------------------|
| **Abstraction Level**     | Higher-level abstraction                         | Detailed implementation                            |
| **Purpose**               | Define core logic or policies                    | Execute specific tasks                             |
| **Dependence**            | Depend on abstractions or interfaces             | Implement abstractions defined by high-level       |
| **Change Frequency**      | Less likely to change                            | More likely to change due to implementation details|
| **Examples**              | Business logic classes, service classes          | Utility classes, API clients, database drivers     |

---

## ⚖️ **Dependency Inversion Principle**

In a well-architected system:

- High-level modules **should not depend** on low-level modules.
- Both should depend on **abstractions** (interfaces or abstract classes).

This principle helps in making the system **flexible**, **maintainable**, and **testable**.

### Example of Dependency Inversion

```python
from abc import ABC, abstractmethod

# Abstraction
class PaymentGateway(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

# High-Level Module
class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        self.payment_gateway.make_payment(amount)

# Low-Level Modules
class StripeGateway(PaymentGateway):
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via Stripe")

class PayPalGateway(PaymentGateway):
    def make_payment(self, amount):
        print(f"Payment of ${amount} made via PayPal")

# Usage
stripe = StripeGateway()
paypal = PayPalGateway()

processor = PaymentProcessor(stripe)
processor.process_payment(50)

processor = PaymentProcessor(paypal)
processor.process_payment(100)
```

This design ensures that **high-level modules** (`PaymentProcessor`) depend on **abstractions** (`PaymentGateway`), not on **concrete implementations** (`StripeGateway`, `PayPalGateway`).

---

### ✅ **Summary**

- **High-Level Modules**: Define business logic and higher-level policies.
- **Low-Level Modules**: Provide detailed, specific implementations.
- **Dependency Inversion Principle**: High-level and low-level modules should both depend on abstractions to promote flexibility and maintainability.