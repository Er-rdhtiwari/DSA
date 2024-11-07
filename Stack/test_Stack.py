import pytest
from Stack import Stack

def test_stack():
    stack = Stack()

    assert stack.is_empty() == True, "Stack should be empty Initialy"


