import pytest
from src.widget import mask_data


# Параметризованные тесты для функции mask_account_card
@pytest.mark.parametrize("input_data, data_type, expected_output", [
    # Тесты для номера карты
    ("1234567812345678", "card", "1234567** ****5678"),
    ("9876543210123456", "card", "9876543** ****3456"),
    ("1111222233334444", "card", "1111222** ****4444"),
    ("0000111122223333", "card", "0000111** ****3333"),
    ("1234", "card", "1234** ****4"),
    ("", "card", "Неверный номер карты"),
    ("   ", "card", "Неверный номер карты"),
    # Тесты для номера счета
    ("1234567890123456", "account", "**3456"),
    ("9876543210987654", "account", "**7654"),
    ("", "account", "**"),
    ("   ", "account", "**"),
    ("123", "account", "**123"),

    # Тесты на неверный тип данных
    ("1234567890123456", "unknown", "Неверный тип данных"),
    ("", "unknown", "Неверный тип данных"),
    ("123", "unknown", "Неверный тип данных")
])
def test_mask_account_card(input_data, data_type, expected_output):
    assert mask_account_card(input_data, data_type) == expected_output


#тест для функции get_data
@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-01-05", "2023-01-05"),
    ("05/01/2023", "2023-01-05"),
    ("01-05-2023", "2023-01-05"),
    ("5 January 2023", "2023-01-05"),
    ("January 5, 2023", "2023-01-05"),
    ("2023.01.05", "2023-01-05"),
    ("31-12-2020", "2020-12-31"),
    ("", "Дата отсутствует"),
    ("   ", "Дата отсутствует"),
    ("Not a date", "Некорректный формат даты"),
    ("2023/01/05", "Некорректный формат даты"),
    ("05/13/2023", "Некорректный формат даты"),  # Неверный месяц
])
def test_get_data(input_date, expected_output):
    assert get_data(input_date) == expected_output
