import pytest
from typing import List, Dict, Any
from generators import *


@pytest.fixture
def sample_transactions_with_descriptions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "amount": 100, "currency": "USD", "description": "Payment"},
        {"id": 2, "amount": 200, "currency": "EUR", "description": "Transfer"},
        {"id": 3, "amount": 50, "currency": "USD"},  # Нет description
        {"id": 4, "description": "Refund"},  # Только description
    ]

def test_transaction_descriptions_basic(sample_transactions_with_descriptions):
    result = list(transaction_descriptions(sample_transactions_with_descriptions))
    # Если функция возвращает пустые строки - включаем их в ожидание
    assert result == ["Payment", "Transfer", "Refund"]

def test_transaction_descriptions_empty():
    transactions = [{"id": 1}, {"amount": 100}]  # Нет description
    result = list(transaction_descriptions(transactions))
    assert result == []  # Пустой список, т.к. нет description


# Тесты для card_number_generator
@pytest.mark.parametrize("start,end,expected_first,expected_last,expected_count", [
    ("0000 0000 0000 0001", "0000 0000 0000 0003", "0000 0000 0000 0001", "0000 0000 0000 0003", 3),
    (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003", 3),
    ("0000 0000 0000 0005", "0000 0000 0000 0005", "0000 0000 0000 0005", "0000 0000 0000 0005", 1),
])
def test_card_number_generator_basic(start, end, expected_first, expected_last, expected_count):
    result = list(card_number_generator(start, end))
    assert len(result) == expected_count
    assert result[0] == expected_first
    assert result[-1] == expected_last


def test_card_number_generator_invalid_input():
    with pytest.raises(ValueError):
        list(card_number_generator("0000 0000 0000 0005", "0000 0000 0000 0001"))  # start > end

    with pytest.raises(ValueError):
        list(card_number_generator("ABCD 0000 0000 0001", "0000 0000 0000 0002"))  # нечисловые символы


def test_transaction_descriptions_invalid_input():
    """Тест на некорректный ввод"""
    # Пустой список
    assert list(transaction_descriptions([])) == []
    # None вместо списка
    assert list(transaction_descriptions([None])) == []


def test_card_number_edge_cases():
    """Тест граничных случаев для генератора карт"""
    # Одна карта
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]

    # Неправильный формат номера
    with pytest.raises(ValueError):
        list(card_number_generator("invalid", 1))
