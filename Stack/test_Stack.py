import pytest
from Stack import Stack

def test_stack():
    stack = Stack()
    print("Hi...........")
    assert stack.is_empty() == True, "Stack should be empty Initialy"

    # Push Eliment To stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # check the peek functionality
    assert stack.peek() == 30, "Top os stack should be 30"

    # Pop the eliment
    assert stack.pop() == 30, "pop item should be 30"
    assert stack.pop() == 20, "pop item should be 20"
    assert stack.pop() == 10, "pop item should be 10"

    # Test stack is empty after poping all eliment
    assert stack.is_empty() == True, "Stack should be empty after poping all items"

    # Test pop and peek on Empty Stack
    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.peek()




if __name__ == "__main__":
    pytest.main(["-s", "-v", "--log-cli-level=DEBUG"])