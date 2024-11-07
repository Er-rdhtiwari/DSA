To see detailed logs when running `pytest` tests, you can use the `-s` or `--capture=no` option, and to see test progress with verbose output, add the `-v` option.

Here’s how you can enable different levels of output:

1. **Show Print Statements** (`-s`):
   The `-s` option tells `pytest` not to capture output, so any `print` statements inside your tests will display in the console.

   ```bash
   pytest -s
   ```

2. **Verbose Mode** (`-v`):
   The `-v` option provides more detailed information about each test, showing each test's name and status (pass/fail).

   ```bash
   pytest -v
   ```

3. **Combine Both Options** (`-s -v`):
   For detailed logs and test names, use both `-s` and `-v`:

   ```bash
   pytest -s -v
   ```

4. **Log Output to a File**:
   You can also direct output to a log file by redirecting the console output.

   ```bash
   pytest -s -v > test_log.txt
   ```

5. **Using `--log-cli-level`**:
   If you are using Python’s built-in `logging` module in your tests, you can set a logging level to display log messages with `--log-cli-level`. For example, to show debug-level logs:

   ```bash
   pytest --log-cli-level=DEBUG
   ```

### Example Command
To see detailed output with all `print` statements and logging information, you might use:

```bash
pytest -s -v --log-cli-level=DEBUG
```

This will give you a full view of test progress, logging information, and any `print` statements.

Yes, you can set `pytest` flags directly within your Python test file by adding a configuration in the `pytest` setup, using `pytest.ini`, `conftest.py`, or programmatically with `pytest.main()`.

Here are a few methods:

### 1. Using `pytest.ini` or `conftest.py`
If you want to control the logging output for all tests in your project, you can create a `pytest.ini` file or a `conftest.py` file in your project directory and set logging options there.

**Example `pytest.ini` file:**

```ini
# pytest.ini
[pytest]
log_cli = true
log_cli_level = DEBUG
addopts = -v -s
```

This configuration:
- Enables logging in the command line with `log_cli = true`.
- Sets the logging level to `DEBUG`.
- Adds `-v` (verbose) and `-s` (show print statements) flags automatically.

### 2. Programmatically Setting Flags in a Test File

If you want to set logging options programmatically within a specific test file (like `test_stack.py`), you can use `pytest.main()` and pass the arguments in a `__name__ == "__main__"` block.

```python
import pytest

# Example test functions
def test_example():
    print("This is a print statement for debugging.")
    assert 1 == 1

if __name__ == "__main__":
    # Run pytest programmatically with flags
    pytest.main(["-s", "-v", "--log-cli-level=DEBUG"])
```

This approach lets you execute `pytest` with the specified flags whenever the file is run directly, enabling detailed logs (`-s` for print statements, `-v` for verbosity, and `--log-cli-level=DEBUG` for debug logging level).

### 3. Setting Up Logging in the Test Code
If you're using the `logging` module, you can set up logging in each test file to show logs without needing additional `pytest` arguments.

```python
import logging

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def test_with_logging():
    logger.debug("This is a debug log.")
    logger.info("This is an info log.")
    assert 1 == 1
```

### Summary
For adding logs without modifying `pytest` command-line behavior:
- Use `pytest.ini` or `conftest.py` for global settings.
- Use `pytest.main()` within a test file for local control.
- Set up logging within your test functions for module-level logs.