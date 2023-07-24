from src.data_structures.queue import MyQueue


def test_enqueue():
    q = MyQueue()

    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(9)

    assert q.getlength() == 3


def test_deque():
    q = MyQueue()

    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(9)

    assert q.getlength() == 3

    assert q.deque() == 5
    assert q.deque() == 7
    assert q.deque() == 9
    assert q.deque() is None

    assert q.getlength() == 0


def test_peek():
    q = MyQueue()

    q.enqueue(5)
    assert q.peek() == 5
    assert q.deque() == 5
    assert q.getlength() == 0

    q.enqueue(7)
    assert q.getlength() == 1
    assert q.peek() == 7

    assert q.deque() == 7

    q.enqueue(9)
    assert q.peek() == 9
    assert q.deque() == 9

    assert q.getlength() == 0
