import pytest
from src.masks import get_mask_card_number, get_mask_account


# тест для функции get_mask_card_number
@pytest.mark.parametrize("card_number, expected_output", [
    ("1234123412341234", "123412** ****1234"),
    ("5678567856785678", "567856** ****5678"),
    ("", "Неверный номер карты"),  # Тест на пустую строку
    ("   ", "Неверный номер карты"),  # Тест на строку с пробелами
    ("123", "Неверный номер карты"),  # Тест на строку с недостаточным количеством цифр
])
def test_mask_card_number(card_number, expected_output):
    assert get_mask_card_number(card_number) == expected_output


# Тесты для функции get_mask_account
@pytest.mark.parametrize("input_account, expected_output", [
    ("1234567890123456", "**3456"),  # Тест на обычный номер счета
    ("9876543210987654", "**7654"),  # Тест на другой номер счета
    ("1111222233334444", "**4444"),  # Тест на номер счета
    ("0000111122223333", "**3333"),  # Тест на номер счета
    ("1234", "**1234"),  # Тест на короткий номер счета
    ("", "**"),  # Тест на пустую строку
    ("   ", "**"),  # Тест на строку с пробелами
])
def test_mask_account(input_account, expected_output):
    assert get_mask_account(input_account) == expected_output
