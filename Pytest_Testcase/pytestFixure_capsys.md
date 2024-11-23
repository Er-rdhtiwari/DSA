The use of `pytest.fixture` and `capsys` in pytest provides important functionalities that help make tests more modular, readable, and efficient. Here’s why they are valuable:
### full Lecture: https://youtu.be/cHYq1MRoyI0?si=1nt6YmiFsVRtvkIi
### https://www.youtube.com/watch?v=inf7AaZWJcY&list=PLhH3UpV2flrxYmbhZ3V7C0bfrl2pAt3i6&ab_channel=rithmic
### 1. `pytest.fixture`

- **Purpose**: `pytest.fixture` is used to create setup code that can be shared across multiple test functions. It allows you to define common objects or states that tests need to run, ensuring code reusability and consistency.
- **Benefits**:
  - **Reusability**: Instead of initializing objects or setting up state repeatedly in each test, you can define the setup once in a fixture and use it across multiple tests.
  - **Modularity**: Fixtures can be parameterized or modified easily without changing the test cases, making your tests more modular and maintainable.
  - **Consistency**: Ensures that all tests using the fixture start with the same initial state, reducing the chances of flaky or inconsistent test results.

In the example, the `stack` fixture initializes a `Stack` object that can be used in multiple test functions, making the tests clean and DRY (Don't Repeat Yourself).

### 2. `capsys`

- **Purpose**: `capsys` is a pytest-provided fixture used to capture standard output (`stdout`) and standard error (`stderr`) during the execution of a test. It allows you to validate the output of functions that print to the console.
- **Benefits**:
  - **Output Verification**: Helps to verify that functions produce the correct output, which is essential for testing functions that use `print()` statements.
  - **Cleaner Tests**: Avoids modifying the original code to return values just for testing purposes. You can test the printed output directly.

In the example, `capsys` captures the output from the `print_stack()` method to verify that it outputs the expected stack values.

### Summary

- **`pytest.fixture`** helps in setting up test states or objects consistently and efficiently.
- **`capsys`** allows capturing and asserting output printed to the console, making it easy to test functions that produce console output.

Using these features in your tests leads to better-organized, more maintainable, and cleaner test code.