import pytest

def func(x):
    return x + 1

def test_addition():
    assert func(3) == 4

def f():
    raise SystemExit(1)

def test_raises():
    with pytest.raises(SystemExit):
        f()

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert "h" in x
