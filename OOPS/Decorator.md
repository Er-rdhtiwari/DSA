### What is a Decorator in Python?

A **decorator** in Python is a design pattern that allows you to modify or extend the behavior of a function or method without changing its source code. A decorator is essentially a higher-order function that takes a function as an argument and returns a new function that enhances or modifies the original function's behavior.

### Sequence of Execution with Multiple Decorators

When multiple decorators are applied to a function, they are executed in a **bottom-up** order (from the closest to the farthest). The function is wrapped in the innermost decorator first and then successively by outer decorators.

---

### Real-Life Example: Logging, Authorization, and Validation

Here, we'll create a real-world example where decorators are used in the context of a web application. We'll implement:
1. **Authorization Check**: Ensures the user has the required permissions.
2. **Input Validation**: Validates the input data.
3. **Logging**: Logs the function's execution.

We'll follow **OOP** and **SOLID principles**, especially:
- **Single Responsibility Principle**: Each decorator has a single responsibility.
- **Open/Closed Principle**: New behaviors can be added without modifying existing code.
- **Dependency Inversion Principle**: High-level modules depend on abstractions (functions) rather than low-level details.

---

### Python Code with Explanation

```python
import functools

# Simulated user session for authorization
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Mock user object
current_user = User(username="Radhe", role="admin")

# Authorization Decorator
def authorize(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.role != required_role:
                raise PermissionError(f"User '{current_user.username}' does not have {required_role} privileges.")
            print(f"Authorization passed for user: {current_user.username}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Validation Decorator
def validate_inputs(required_keys):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not all(key in kwargs for key in required_keys):
                raise ValueError(f"Missing required input keys: {required_keys}")
            print(f"Validation passed with inputs: {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Logging Decorator
def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished execution of {func.__name__}, result: {result}")
        return result
    return wrapper

# A service class using the decorators
class PaymentService:
    @log_execution
    @validate_inputs(["amount", "currency"])
    @authorize("admin")
    def process_payment(self, amount, currency, recipient):
        """
        Processes a payment.
        """
        print(f"Processing payment of {amount} {currency} to {recipient}")
        return "Payment successful"

# Usage
try:
    payment_service = PaymentService()
    # The function is wrapped by log_execution -> validate_inputs -> authorize
    print(payment_service.process_payment(amount=100, currency="USD", recipient="John Doe"))
except Exception as e:
    print(f"Error: {e}")
```

---

### Sequence of Execution

In the above code:
1. **`authorize("admin")`**: Checks if the user has admin privileges.
2. **`validate_inputs(["amount", "currency"])`**: Ensures required inputs are provided.
3. **`log_execution`**: Logs the execution of the function.

The **execution order** of the decorators is bottom-up:
1. **`log_execution` wraps the function first.**
2. **`validate_inputs` wraps the result of `log_execution`.**
3. **`authorize` wraps the result of `validate_inputs`.**

When the function is called:
1. **`authorize` is executed first** to check permissions.
2. **`validate_inputs` is executed next** to validate inputs.
3. **`log_execution` is executed last** to log the execution details.

---

### Output Example

```plaintext
Authorization passed for user: Radhe
Validation passed with inputs: {'amount': 100, 'currency': 'USD', 'recipient': 'John Doe'}
Executing process_payment with args: (), kwargs: {'amount': 100, 'currency': 'USD', 'recipient': 'John Doe'}
Processing payment of 100 USD to John Doe
Finished execution of process_payment, result: Payment successful
Payment successful
```

---

### Benefits of This Approach:
1. **Modularity**: Each decorator has a clear, single responsibility.
2. **Reusability**: Decorators can be reused across different methods and classes.
3. **Readability**: Enhances readability by separating concerns.
4. **Extensibility**: Adding a new feature (e.g., caching) only requires creating another decorator.

This structure aligns with OOP and SOLID principles, promoting maintainability and scalability in larger applications.

Here’s a detailed explanation of the code and concepts behind decorators, along with additional comments for better understanding.

---

### Understanding Decorators in Depth

#### What is a Decorator?
- A **decorator** is a function that takes another function (or method) as an argument, wraps additional functionality around it, and returns the enhanced function.
- In essence, decorators allow you to **add behaviors dynamically** without altering the original function's definition.

---

### Step-by-Step Explanation of the Code

```python
import functools
```
- The `functools` module provides tools like `@functools.wraps` to preserve the original function's metadata (e.g., name, docstring) when it is wrapped by a decorator.

---

#### Simulating a User for Authorization
```python
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Mock user object
current_user = User(username="Radhe", role="admin")
```
- The `User` class simulates a logged-in user.
- The `current_user` is a mock object representing a user with the username `Radhe` and the role `admin`.

---

#### Authorization Decorator

```python
def authorize(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check if the user's role matches the required role
            if current_user.role != required_role:
                raise PermissionError(f"User '{current_user.username}' does not have {required_role} privileges.")
            print(f"Authorization passed for user: {current_user.username}")
            return func(*args, **kwargs)  # Call the original function
        return wrapper
    return decorator
```

- **Purpose**: Ensure only users with specific roles can execute the function.
- **Key Points**:
  - The `authorize` function takes the `required_role` as a parameter.
  - Inside the decorator:
    - `if current_user.role != required_role`: Checks if the current user's role matches the required role. If not, it raises a `PermissionError`.
    - `func(*args, **kwargs)`: Calls the original function if authorization passes.

---

#### Input Validation Decorator

```python
def validate_inputs(required_keys):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check if all required keys are in the keyword arguments
            if not all(key in kwargs for key in required_keys):
                raise ValueError(f"Missing required input keys: {required_keys}")
            print(f"Validation passed with inputs: {kwargs}")
            return func(*args, **kwargs)  # Call the original function
        return wrapper
    return decorator
```

- **Purpose**: Ensure the function is called with all required inputs.
- **Key Points**:
  - The `validate_inputs` decorator takes a list of `required_keys`.
  - Inside the decorator:
    - `if not all(key in kwargs for key in required_keys)`: Validates that all required keys are present in the `kwargs` (keyword arguments).
    - If validation passes, it calls the original function.

---

#### Logging Decorator

```python
def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"Finished execution of {func.__name__}, result: {result}")
        return result
    return wrapper
```

- **Purpose**: Log the function's execution details, including arguments and result.
- **Key Points**:
  - `print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")`: Logs the function name and its input arguments.
  - `result = func(*args, **kwargs)`: Calls the original function and stores the result.
  - `print(f"Finished execution of {func.__name__}, result: {result}")`: Logs the function's result.

---

#### Using Decorators in an OOP Context

```python
class PaymentService:
    @log_execution
    @validate_inputs(["amount", "currency"])
    @authorize("admin")
    def process_payment(self, amount, currency, recipient):
        """
        Processes a payment.
        """
        print(f"Processing payment of {amount} {currency} to {recipient}")
        return "Payment successful"
```

- **Decorators Applied**:
  1. **`authorize("admin")`**: Ensures only users with the `admin` role can process payments.
  2. **`validate_inputs(["amount", "currency"])`**: Validates that `amount` and `currency` are provided as inputs.
  3. **`log_execution`**: Logs the function's execution.
  
- **Execution Order**:
  - Decorators are applied bottom-up. The function is first wrapped with `authorize`, then `validate_inputs`, and finally `log_execution`.

---

#### Using the PaymentService Class

```python
# Usage
try:
    payment_service = PaymentService()
    # The function is wrapped by log_execution -> validate_inputs -> authorize
    print(payment_service.process_payment(amount=100, currency="USD", recipient="John Doe"))
except Exception as e:
    print(f"Error: {e}")
```

- This demonstrates how decorators enhance functionality dynamically without modifying the `process_payment` method directly.

---

### Key Points to Remember While Learning Decorators

1. **Order of Execution**:
   - Decorators are executed from bottom to top in the order they are applied.
   - The innermost decorator (closest to the function) is executed first.

2. **Use Cases**:
   - **Logging**: Track function execution.
   - **Validation**: Check inputs or conditions.
   - **Caching**: Cache function results.
   - **Authorization**: Control access to specific functionality.

3. **Good Practices**:
   - Use `@functools.wraps` to preserve the original function’s metadata.
   - Keep each decorator focused on a single responsibility (aligns with SOLID principles).
   - Avoid hardcoding logic in decorators (e.g., use parameters like `required_role`).

4. **Test Your Decorators**:
   - Test each decorator independently.
   - Ensure they work correctly in combination.

5. **Reusability**:
   - Design decorators to be reusable across multiple functions or classes.

---

### Final Thoughts
Decorators are a powerful feature in Python that allow you to write cleaner, modular, and more maintainable code. By applying OOP and SOLID principles, you can design decorators that are reusable and easy to test, making them valuable tools in real-world applications.
Here’s a detailed explanation of the three elements mentioned in the code and their purposes:

---

### 1. `def decorator(func):`

#### **What It Does:**
- This is the definition of the **outer function** in a decorator.
- It takes a function (`func`) as an argument, which is the function being decorated.

#### **Purpose:**
- The outer function wraps the target function (`func`) to enhance or modify its behavior.
- It can:
  - Accept additional parameters (e.g., `authorize(required_role)`).
  - Define an inner function (commonly named `wrapper`) to execute custom logic before or after the target function.

#### **Example:**
```python
def decorator(func):
    print("Decorator is being applied")
    return func
```
When used:
```python
@decorator
def my_function():
    print("Hello from my_function")

my_function()
```

Output:
```plaintext
Decorator is being applied
Hello from my_function
```

---

### 2. `@functools.wraps(func)`

#### **What It Does:**
- `@functools.wraps(func)` is a decorator provided by Python's `functools` module.
- It updates the `wrapper` function to inherit the metadata of the original `func`.

#### **Why It’s Important:**
- Without `@functools.wraps`, the `wrapper` function would replace the original function's name, docstring, and other metadata. This can lead to confusion in debugging and introspection tools.

#### **How It Works:**
- It ensures that the decorated function retains the following:
  - **`__name__`**: The original function's name.
  - **`__doc__`**: The original function's docstring.
  - **`__module__`**: The module in which the original function is defined.

#### **Example Without `@functools.wraps`:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper executed")
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_function():
    """This is my_function docstring."""
    print("Hello from my_function")

print(my_function.__name__)  # Output: wrapper
print(my_function.__doc__)   # Output: None
```

#### **Example With `@functools.wraps`:**
```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper executed")
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_function():
    """This is my_function docstring."""
    print("Hello from my_function")

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: This is my_function docstring.
```

---

### 3. `def wrapper(*args, **kwargs):`

#### **What It Does:**
- The `wrapper` function is the **inner function** inside the decorator.
- It takes `*args` (positional arguments) and `**kwargs` (keyword arguments), ensuring the decorator can work with any function, regardless of its signature.

#### **Purpose:**
- The `wrapper` function provides the logic that gets executed **around** the original function. It "wraps" the original function to:
  - Add pre-processing logic (e.g., logging, validation).
  - Add post-processing logic (e.g., caching, cleanup).
  - Decide whether or not to call the original function (e.g., based on authorization).

#### **Key Points:**
- The `wrapper` function:
  - Calls the original function with `func(*args, **kwargs)`.
  - Returns the result of the original function if needed.

#### **Example:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper: Before the function call")
        result = func(*args, **kwargs)
        print("Wrapper: After the function call")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Radhe")
```

Output:
```plaintext
Wrapper: Before the function call
Hello, Radhe!
Wrapper: After the function call
```

---

### How They Work Together in the Code

1. **Outer Function (`def decorator(func):`)**:
   - Accepts the function to be decorated (`func`).
   - Returns the `wrapper` function to replace the original.

2. **Inner Function (`def wrapper(*args, **kwargs):`)**:
   - Wraps the original function to add extra logic.
   - Executes the logic before or after calling `func(*args, **kwargs)`.

3. **`@functools.wraps(func)`**:
   - Ensures that the `wrapper` function retains the original function's metadata, like `__name__` and `__doc__`.

---

### Conceptual Workflow
1. You define a decorator using `def decorator(func):`.
2. Inside the decorator:
   - You define the `wrapper` function to implement the additional behavior.
   - You use `@functools.wraps(func)` to preserve the original function’s identity.
   - You call the original function using `func(*args, **kwargs)`.
3. When you use `@decorator` above a function:
   - Python replaces the original function with the returned `wrapper` function.

---

### Key Takeaways While Learning Decorators
1. **Understand the Role of `*args` and `**kwargs`:**
   - Decorators must be flexible to handle any function signature.

2. **Use `@functools.wraps`:**
   - Always use `@functools.wraps(func)` in your decorators to retain the original function's metadata.

3. **Learn the Execution Order:**
   - Decorators are applied from bottom to top but executed from top to bottom.

4. **Practice with Simple Use Cases:**
   - Start with basic examples (like logging or timing a function) before tackling complex scenarios like nested decorators or parameterized decorators.

5. **Focus on Reusability:**
   - Design decorators to handle generic use cases, making them reusable.

6. **Debugging with Decorators:**
   - Use `@functools.wraps` and test the `__name__` and `__doc__` of decorated functions to ensure clarity in debugging.

Decorators are a powerful way to modify function behavior dynamically. By understanding their structure and purpose in detail, you can leverage them effectively in Python projects!

The use of `*args` and `**kwargs` in decorators is crucial because they ensure that the decorator can handle functions with any number of arguments and keyword arguments. Let’s break this down in detail.

---

### **What are `*args` and `**kwargs`?**

1. **`*args`**:
   - Allows a function to accept any number of **positional arguments**.
   - It collects all positional arguments into a tuple.

2. **`**kwargs`**:
   - Allows a function to accept any number of **keyword arguments**.
   - It collects all keyword arguments into a dictionary.

---

### **Why Use `*args` and `**kwargs` in Decorators?**

#### 1. **Flexibility with Function Signatures**
   - A decorator should work with any function, regardless of the number or type of arguments it takes.
   - By using `*args` and `**kwargs`, the decorator doesn’t need to know or hard-code the exact signature of the decorated function.

   **Example:**
   ```python
   def log_execution(func):
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__} with args={args} and kwargs={kwargs}")
           return func(*args, **kwargs)  # Pass arguments to the original function
       return wrapper
   ```

   - This decorator works for any function, whether it has:
     - No arguments.
     - Positional arguments only.
     - Keyword arguments only.
     - A mix of both.

#### 2. **Preserving the Function’s Behavior**
   - Without `*args` and `**kwargs`, the decorator would need to explicitly define and match the arguments of the decorated function.
   - This would make the decorator inflexible and harder to maintain.

   **Without `*args` and `**kwargs` (Incorrect Approach):**
   ```python
   def log_execution(func):
       def wrapper(arg1, arg2):  # Must know the exact arguments
           print(f"Executing {func.__name__} with arg1={arg1}, arg2={arg2}")
           return func(arg1, arg2)  # Must pass them explicitly
       return wrapper
   ```

   **Problem:**
   - This decorator can only work for functions with exactly two arguments.

#### 3. **Reusability**
   - Decorators with `*args` and `**kwargs` can be reused across multiple functions, making them versatile and reducing duplication of code.

   **Example of Reusability:**
   ```python
   @log_execution
   def add(a, b):
       return a + b

   @log_execution
   def greet(name="Radhe"):
       return f"Hello, {name}!"
   ```

   - The same decorator works for both `add` (which takes two positional arguments) and `greet` (which takes a keyword argument).

---

### **Common Mistakes When Using `*args` and `**kwargs` in Decorators**

#### 1. **Forgetting to Pass Arguments to the Original Function**
   - A common mistake is to call the decorated function without passing the collected arguments back.

   **Incorrect:**
   ```python
   def log_execution(func):
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__}")
           return func()  # Arguments are ignored
       return wrapper
   ```

   - This will cause errors if the original function requires arguments.

   **Correct:**
   ```python
   def log_execution(func):
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__} with args={args}, kwargs={kwargs}")
           return func(*args, **kwargs)  # Pass the arguments correctly
       return wrapper
   ```

---

#### 2. **Not Handling Return Values Correctly**
   - Decorators must return the output of the original function to preserve its behavior.

   **Incorrect:**
   ```python
   def log_execution(func):
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__}")
           func(*args, **kwargs)  # Return value is ignored
       return wrapper
   ```

   - If the original function returns a value, this decorator will lose it.

   **Correct:**
   ```python
   def log_execution(func):
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__}")
           result = func(*args, **kwargs)  # Capture the return value
           return result  # Return it to the caller
       return wrapper
   ```

---

#### 3. **Not Using `@functools.wraps`**
   - Without `@functools.wraps`, the decorated function will lose its metadata, such as its name and docstring.

   **Incorrect:**
   ```python
   def log_execution(func):
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__}")
           return func(*args, **kwargs)
       return wrapper
   ```

   **Correct:**
   ```python
   import functools

   def log_execution(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
           print(f"Executing {func.__name__}")
           return func(*args, **kwargs)
       return wrapper
   ```

---

### **Detailed Example Demonstrating Importance of `*args` and `**kwargs`**

```python
import functools

# Logging decorator
def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result of {func.__name__}: {result}")
        return result
    return wrapper

# Function with positional arguments
@log_execution
def add(a, b):
    return a + b

# Function with keyword arguments
@log_execution
def greet(name="Radhe", greeting="Hello"):
    return f"{greeting}, {name}!"

# Function with mixed arguments
@log_execution
def order_item(item, quantity=1):
    return f"Ordered {quantity} x {item}"

# Test
print(add(3, 5))               # Positional arguments
print(greet(name="John"))      # Keyword arguments
print(order_item("Pizza", 2))  # Mixed arguments
```

**Output:**
```plaintext
Executing add with args=(3, 5) and kwargs={}
Result of add: 8
8
Executing greet with args=() and kwargs={'name': 'John'}
Result of greet: Hello, John!
Hello, John!
Executing order_item with args=('Pizza', 2) and kwargs={}
Result of order_item: Ordered 2 x Pizza
Ordered 2 x Pizza
```

---

### **Key Takeaways**
1. **Why Use `*args` and `**kwargs`?**
   - They ensure the decorator can handle any function signature.
   - They make the decorator reusable for functions with different argument types and numbers.

2. **Avoid These Common Mistakes:**
   - Forgetting to pass `*args` and `**kwargs` to the original function.
   - Ignoring the return value of the decorated function.
   - Skipping `@functools.wraps`, which causes loss of metadata.

3. **Best Practices:**
   - Always pass `*args` and `**kwargs` to ensure the original function executes as intended.
   - Use `@functools.wraps` to retain function metadata.
   - Test the decorator with various functions (no arguments, only positional, only keyword, and mixed arguments) to confirm its flexibility.

By following these guidelines, you can design robust and reusable decorators in Python!
