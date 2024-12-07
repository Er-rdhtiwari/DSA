### **Day 3 Notes: DSA (Data Structures and Algorithms) + Flask Advanced Topics**

---

## **Part 1: Data Structures and Algorithms (DSA)**

### **Core Algorithms to Focus On**

#### 1. **Binary Search**
- **Concept**:
  - Efficiently searches for an element in a **sorted array**.
  - Time Complexity: **O(log n)**.

- **Steps**:
  1. Find the middle element.
  2. If the middle element matches the target, return its index.
  3. If the target is less than the middle element, search the left half.
  4. If the target is greater, search the right half.

- **Python Code Example**:
  ```python
  def binary_search(arr, target):
      left, right = 0, len(arr) - 1
      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
      return -1

  # Example usage
  arr = [1, 3, 5, 7, 9, 11]
  print(binary_search(arr, 7))  # Output: 3
  ```

#### 2. **Two-Pointer Technique**
- **Concept**:
  - Uses two pointers to solve problems in linear time.
  - Often used for sorted arrays or strings.

- **Common Problems**:
  - **Palindrome Check**:
    ```python
    def is_palindrome(s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    print(is_palindrome("racecar"))  # Output: True
    ```

  - **Find Pair with Given Sum**:
    ```python
    def two_sum(arr, target):
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return (left, right)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

    print(two_sum([1, 2, 4, 6, 10], 8))  # Output: (1, 3)
    ```

#### 3. **Sliding Window Technique**
- **Concept**:
  - Efficiently handles problems involving **subarrays** or **substrings**.
  - Time Complexity: **O(n)**.

- **Common Problem**: **Maximum Sum of a Subarray of Size `k`**:
  ```python
  def max_sum_subarray(arr, k):
      max_sum, window_sum = 0, 0
      for i in range(len(arr)):
          window_sum += arr[i]
          if i >= k - 1:
              max_sum = max(max_sum, window_sum)
              window_sum -= arr[i - (k - 1)]
      return max_sum

  print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
  ```

#### 4. **Hashing**
- **Concept**:
  - Use a **dictionary** to store frequencies or check for duplicates.

- **Common Problem**: **Check for Anagrams**:
  ```python
  from collections import Counter

  def are_anagrams(str1, str2):
      return Counter(str1) == Counter(str2)

  print(are_anagrams("listen", "silent"))  # Output: True
  ```

---

### **Practical Problems to Solve**
1. **Binary Search**:
   - Find the first and last position of an element in a sorted array.
2. **Two-Pointer**:
   - Merge two sorted arrays.
3. **Sliding Window**:
   - Longest substring without repeating characters.
4. **Hashing**:
   - Find the first non-repeating character in a string.

---

## **Part 2: Flask Advanced Topics**

### **1. Flask-SQLAlchemy (Database Integration)**
- **Core Concepts**:
  - **Models**: Define tables and relationships.
  - **CRUD Operations**:
    - Create, Read, Update, Delete records.
  - **Transactions**:
    - Ensure atomic operations with `session.commit()` and `session.rollback()`.

- **Example**:
  ```python
  from flask import Flask, request, jsonify
  from flask_sqlalchemy import SQLAlchemy

  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///billing.db'
  db = SQLAlchemy(app)

  # Define a Customer model
  class Customer(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100))
      email = db.Column(db.String(100), unique=True)

  @app.route('/customers', methods=['POST'])
  def add_customer():
      data = request.get_json()
      new_customer = Customer(name=data['name'], email=data['email'])
      db.session.add(new_customer)
      db.session.commit()
      return jsonify({"message": "Customer added"}), 201

  if __name__ == '__main__':
      db.create_all()
      app.run(debug=True)
  ```

---

### **2. Flask-JWT (Authentication)**
- **Core Concepts**:
  - Implement token-based authentication to secure APIs.

- **Example**:
  ```python
  from flask import Flask, jsonify, request
  from flask_jwt_extended import JWTManager, create_access_token, jwt_required

  app = Flask(__name__)
  app.config['JWT_SECRET_KEY'] = 'secret-key'
  jwt = JWTManager(app)

  @app.route('/login', methods=['POST'])
  def login():
      username = request.json.get('username')
      if username == 'admin':
          token = create_access_token(identity=username)
          return jsonify(access_token=token)
      return jsonify({"error": "Invalid credentials"}), 401

  @app.route('/protected', methods=['GET'])
  @jwt_required()
  def protected():
      return jsonify({"message": "You are authenticated"})

  if __name__ == '__main__':
      app.run(debug=True)
  ```

---

### **3. Error Handling**
- **Custom Error Responses**:
  ```python
  from flask import Flask, jsonify

  app = Flask(__name__)

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({"error": "Resource not found"}), 404

  if __name__ == '__main__':
      app.run(debug=True)
  ```

---

### **Practical Scenario**
1. **Build a Billing API**:
   - **Secure Endpoints** with JWT.
   - **CRUD Operations** for customers and invoices using SQLAlchemy.
   - **Error Handling** for invalid requests.

---

### **Action Plan for Today**
1. **DSA**:
   - Practice 2-3 coding problems using Binary Search, Two-Pointer, and Sliding Window techniques.
2. **Flask Advanced**:
   - Build a secure CRUD API with Flask-SQLAlchemy and JWT.
   - Implement error handling for your API.
3. **Mock Practice**:
   - Simulate a quick coding round (solve a problem in 15-20 minutes).

---

Let me know if you need further clarification or specific examples for any topic! 🚀😊