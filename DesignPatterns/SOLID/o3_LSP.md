### **Liskov Substitution Principle (LSP)**

The **Liskov Substitution Principle (LSP)** is the "L" in the SOLID principles of software design. It states:

> **"Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program."**

In simpler terms:
- A subclass should **extend** the behavior of its parent class without changing its meaning or breaking its functionality.
- Code that uses a base class should work seamlessly when a derived class is substituted in its place.

### **Key Points of LSP**
1. Subclasses must adhere to the **contract** defined by the parent class.
2. Subclasses should **not violate assumptions** made by the parent class.
3. Substituting a subclass for the parent should not result in unexpected behavior.

---

### **Why LSP is Important?**
- **Maintains Polymorphism**: Enables polymorphic behavior without breaking the program.
- **Improves Maintainability**: Ensures that extending functionality via inheritance doesn't introduce bugs.
- **Enhances Reusability**: Subclasses can be used interchangeably with their base class.

---

### **Example: Violating LSP**

Let’s consider an example involving a rectangle and a square.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

# Square is a subclass of Rectangle
class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # A square must have equal width and height

    def set_height(self, height):
        self.width = height  # A square must have equal width and height
        self.height = height
```

Here, substituting `Square` for `Rectangle` violates LSP. Let’s see why.

#### **Test Case**
```python
def test_rectangle_area(rect):
    rect.set_width(4)
    rect.set_height(5)
    assert rect.area() == 20, f"Expected area to be 20 but got {rect.area()}"

# Using Rectangle works fine
rect = Rectangle(0, 0)
test_rectangle_area(rect)

# Substituting Square for Rectangle breaks the test
square = Square(0, 0)
test_rectangle_area(square)
```

- **Problem**: The test fails for `Square` because setting the width or height modifies both dimensions, breaking the expected behavior.

---

### **Correct Example (Following LSP)**

To follow LSP, the design should avoid inheritance when the subclass cannot truly extend the behavior of the base class. Instead, use composition or interfaces.

#### **Refactored Code**
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

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

# Square class (Separate from Rectangle)
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

#### **Test Case**
```python
def test_shape_area(shape):
    if isinstance(shape, Rectangle):
        shape.set_width(4)
        shape.set_height(5)
        assert shape.area() == 20, f"Expected area to be 20 but got {shape.area()}"
    elif isinstance(shape, Square):
        shape.set_side(4)
        assert shape.area() == 16, f"Expected area to be 16 but got {shape.area()}"

# Using Rectangle
rect = Rectangle(0, 0)
test_shape_area(rect)

# Using Square
square = Square(0)
test_shape_area(square)
```

---

### **Explanation of Fix**

1. **Abstraction via `Shape`**:
   - Both `Rectangle` and `Square` implement `Shape` but don’t share a direct inheritance relationship.
   - This avoids the issue of misrepresenting `Square` as a `Rectangle`.

2. **Behavior Consistency**:
   - `Rectangle` and `Square` now have their own behaviors consistent with their definitions.

3. **Preserves Substitutability**:
   - Polymorphism is preserved at the `Shape` level because both `Rectangle` and `Square` adhere to the `Shape` interface.

---

### **Summary of LSP**
- **Definition**: Subclasses should be substitutable for their parent classes without altering the program's correctness.
- **Common Violations**: Occur when subclasses override behavior in ways that break the parent class’s expectations.
- **Solution**: Use abstraction and interfaces properly. Avoid inheritance when a "is-a" relationship doesn’t truly exist.

By following LSP, you create systems that are flexible, maintainable, and predictable.