from src.math_operations import add, sub, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10


def test_sub():
    assert sub(-1, 1) == -2
    assert sub(5, 3) == 2
    assert sub(-1, -1) == 0


def test_multiply():
    assert multiply(1, 10) == 10
    assert multiply(12, -10) == -120


def test_divide():
    assert divide(10, 2) == 5