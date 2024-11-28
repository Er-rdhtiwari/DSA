### Dependency Injection (DI) in Python

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