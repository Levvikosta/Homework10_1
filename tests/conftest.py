import pytest

@pytest.fixture
def func1():
    return '123456 ** **** 0987'
assert func1()

@pytest.fixture
def letters():
    return "olle