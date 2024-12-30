import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_data


#тест для функции get_mask_card_number
@pytest.mark.parametrize("input_card, expected_output", [
    ("1234567812345678", "1234567** ****5678"),
    ("9876543210123456", "9876543** ****3456"),
    ("1111222233334444", "1111222** ****4444"),
    ("0000111122223333", "0000111** ****3333"),
    ("1234", "1234** ****4"),  # Тест на короткий номер
    ("", "Неверный номер карты"),  # Тест на пустую строку
    ("   ", "Неверный номер карты"),  # Тест на строку с пробелами
    ("123", "Неверный номер карты"),  # Тест на строку с недостаточным количеством цифр
])
def test_mask_card_number(input_card, expected_output):
    assert get_mask_card_number(input_card) == expected_output

# Тесты для функции get_mask_account
@pytest.mark.parametrize("input_account, expected_output", [
    ("1234567890123456", "**3456"),  # Тест на обычный номер счета
    ("9876543210987654", "**7654"),  # Тест на другой номер счета
    ("1111222233334444", "**4444"),  # Тест на номер счета
    ("0000111122223333", "**3333"),  # Тест на номер счета
    ("1234", "**1234"),               # Тест на короткий номер счета
    ("", "**"),                       # Тест на пустую строку
    ("   ", "**"),                    # Тест на строку с пробелами
    ("123", "**123")                  # Тест на строку с недостаточным количеством цифр
])
def test_mask_account(input_account, expected_output):
    assert get_mask_account(input_account) == expected_output
