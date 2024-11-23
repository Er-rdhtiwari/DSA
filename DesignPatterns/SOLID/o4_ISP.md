### **Interface Segregation Principle (ISP)**

The **Interface Segregation Principle (ISP)** is the "I" in the SOLID principles. It states:

> **"A class should not be forced to implement interfaces it does not use."**

In simpler terms:
- An interface (or abstract class in Python) should have only the methods that are relevant to the client using it.
- Instead of creating a single large interface with many methods, create smaller, more focused interfaces that are specific to the needs of the client.

---

### **Why is ISP Important?**
1. **Avoids Code Pollution**: Prevents classes from implementing unnecessary methods.
2. **Improves Maintainability**: Reduces the impact of changes to an interface.
3. **Encourages Cohesion**: Focuses on creating interfaces that are cohesive and tailored to specific roles.

---

### **Example: Violating ISP**

Here’s an example of an interface that violates ISP by being too large and forcing classes to implement irrelevant methods.

```python
from abc import ABC, abstractmethod

# Large interface with methods irrelevant to some clients
class Machine(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

    @abstractmethod
    def fax_document(self, document):
        pass

# Printer needs only `print_document`, but is forced to implement all methods
class Printer(Machine):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        raise NotImplementedError("Printer cannot scan documents")

    def fax_document(self, document):
        raise NotImplementedError("Printer cannot fax documents")
```

#### **Problem**
- The `Printer` class is forced to implement `scan_document` and `fax_document`, even though it does not support these functionalities. This violates ISP.

---

### **Correct Example: Following ISP**

To follow ISP, split the `Machine` interface into smaller, more focused interfaces.

#### **Refactored Code**
```python
# Separate smaller interfaces
class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

# Printer only implements Printable
class Printer(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")

# Scanner only implements Scannable
class Scanner(Scannable):
    def scan_document(self, document):
        print(f"Scanning: {document}")

# Multifunction machine implements multiple interfaces
class MultiFunctionMachine(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

    def fax_document(self, document):
        print(f"Faxing: {document}")
```

---

### **Test Case Example**

Here’s how to test the solution with pytest.

#### **Test Cases**
```python
def test_printer():
    printer = Printer()
    assert printer.print_document("Document1") is None  # No exception expected

    # Ensure Printer does not support scanning or faxing
    try:
        printer.scan_document("Document1")
    except NotImplementedError:
        pass  # Expected behavior

    try:
        printer.fax_document("Document1")
    except NotImplementedError:
        pass  # Expected behavior

def test_scanner():
    scanner = Scanner()
    assert scanner.scan_document("Document2") is None  # No exception expected

    # Ensure Scanner does not support printing or faxing
    try:
        scanner.print_document("Document2")
    except NotImplementedError:
        pass  # Expected behavior

    try:
        scanner.fax_document("Document2")
    except NotImplementedError:
        pass  # Expected behavior

def test_multifunction_machine():
    mfm = MultiFunctionMachine()
    assert mfm.print_document("Document3") is None
    assert mfm.scan_document("Document3") is None
    assert mfm.fax_document("Document3") is None  # Multifunction should support all
```

---

### **Explanation of Test Cases**
1. **`test_printer`**:
   - Confirms that `Printer` supports printing and raises `NotImplementedError` for scanning and faxing.
2. **`test_scanner`**:
   - Verifies that `Scanner` supports scanning and raises `NotImplementedError` for printing and faxing.
3. **`test_multifunction_machine`**:
   - Ensures the `MultiFunctionMachine` supports all functionalities.

---

### **Summary of ISP**
- **Problem**: A single large interface can force classes to implement methods they don’t need.
- **Solution**: Split the large interface into smaller, more focused interfaces.
- **Benefits**:
  - Increases cohesion.
  - Makes the system easier to maintain and extend.
  - Adheres to client-specific needs without introducing unnecessary complexity.

By following ISP, your code becomes cleaner, more modular, and easier to maintain!