import pytest
import DSA.Pytest_Testcase.source.my_functions as my_function

def test_add():
    result = my_function.add(1,4)
    assert result == 5