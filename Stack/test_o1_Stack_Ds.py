# test_stackDs.py
import pytest
from o1_Stack_DS import Stack, Node

@pytest.fixture
def stack():
    # Setup: Create a Stack instance with an initial value
    return Stack(4)

def test_node_initialization():
    # Test Node initialization
    node = Node(10)
    assert node.value == 10, "Node value should be initialized correctly."
    assert node.next is None, "Node next should be None by default."

def test_stack_initialization(stack):
    # Test Stack initialization
    assert stack.top is not None, "Stack top should not be None after initialization."
    assert stack.top.value == 4, "Stack top value should be equal to the initialized value."
    assert stack.height == 1, "Stack height should be 1 after initialization."

def test_print_stack(capsys, stack):
    # Capture the output of print_stack
    stack.print_stack()
    captured = capsys.readouterr()
    assert captured.out == "4\n", "Print stack should output the values in the stack."

# Edge cases can be added later as new functionalities are implemented in the Stack class
