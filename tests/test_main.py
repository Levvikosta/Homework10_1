import pytest
from src.main import divide, reverse_string


def test_divide():
    assert divide(2, 2) == 0
    assert divide(6, 3) == 2

# def test_reverse_string_numbers(numbers):
#     assert reverse_string('123') == numbers
#
# def test_reverse_string_letters(letters):
#     assert reverse_string('hello') == letters


@pytest.mark.parametrize('value, expected', [
    ('123', '321'),
    ('hello', 'olleh'),
    ('world', 'dlrow'),
])
def test_reverse_string(value, expected):
    assert reverse_string(value) == expected
