from src.data_structures.stack import Stack


def test_stack_push():
    s = Stack()

    s.push(5)
    s.push(7)
    s.push(9)

    assert s.length == 3


def test_stack_pop():
    s = Stack()

    s.push(5)
    s.push(7)
    s.push(9)

    assert s.pop() == 9
    assert s.length == 2

    s.push(11)
    assert s.pop() == 11
    assert s.pop() == 7
    assert s.pop() == 5
    assert s.pop() is None


def test_stack_peek():
    s = Stack()

    s.push(5)
    s.push(7)
    s.push(9)
    assert s.peek() == 9
    assert s.length == 3
    assert s.pop() == 9

    assert s.peek() == 7
    assert s.length == 2
    assert s.pop() == 7

    assert s.peek() == 5
    assert s.length == 1
    assert s.pop() == 5
    assert s.length == 0

    assert s.peek() is None
    assert s.pop() is None
