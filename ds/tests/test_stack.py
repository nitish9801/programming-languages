from ds.ds.stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()

def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0

def test_push(stack):
    stack.push(2)
    assert len(stack) == 1
    stack.push(4)
    assert len(stack) == 2

def test_pop(stack):
    stack.push(3)
    stack.push('hello')
    assert stack.pop() == 'hello'
    assert stack.pop() == 3
    assert stack.pop() is None
