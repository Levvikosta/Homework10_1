import pytest
from widget import mask_account_card, get_data

@pytest.mark.parametrize("input_data, expected_output", [
    ("1234123412341234", "**** **** **** 1234"),  # Номер карты
    ("9876543210123456", "**** **** **** 3456"),  # Номер карты
    ("1234567890", "******7890"),                # Номер счета
    ("100200300400", "********0400"),              # Номер счета
    ("123456789", "Неверный формат номера. Должен содержать как минимум 10 чисел.")  # Ошибка
])
def test_mask_account_card(input_data, expected_output):
    if "Неверный формат" in expected_output:
        with pytest.raises(ValueError, match=expected_output):
            mask_account_card(input_data)
    else:
        assert mask_account_card(input_data) == expected_output

# Тесты для функции get_data
@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-10-25", "2023-10-25"),         # Корректный формат
    ("25-10-2023", "2023-10-25"),         # Корректный формат
    ("10/25/2023", "2023-10-25"),         # Корректный формат
    ("2023.10.25", "2023-10-25"),         # Корректный формат
    ("October 25, 2023", "2023-10-25"),   # Корректный формат
    ("25/10/2023", "Неверный формат даты"),  # Некорректный формат
    ("", "Нет даты"),                      # Пустая строка
    ("Hello World", "Неверный формат даты"), # Нет даты
    ("2023-13-25", "Неверный формат даты"),  # Некорректный месяц
    ("2023-10-32", "Неверный формат даты"),  # Некорректный день
])
def test_get_data(input_date, expected_output):
    assert get_data(input_date) == expected_output