import pytest
from collections.abc import Iterator
from generators import filter_by_currency

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"},
        {"id": 3, "amount": 50,  "currency": "USD"},
        {"id": 4, "amount": 75,  # no currency
         },
        {"id": 5, "amount": 10, "currency": None},
        {"id": 6, "amount": 5,  "currency": "usd"},  # lowercase
    ]

@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),        # базовый кейс, чувствительность к регистру: только "USD"
        ("EUR", [2]),           # одна запись
        ("usd", [6]),          # поиск по lowercase
        ("GBP", []),            # отсутствующая валюта -> пусто
    ],
)
def test_filter_by_currency_parametrized(sample_transactions, currency, expected_ids):
    result_iter = filter_by_currency(sample_transactions, currency)
    # возвращаемый объект должен быть итератором (ленивый)
    assert isinstance(result_iter, Iterator)
    result = list(result_iter)
    assert [tx["id"] for tx in result] == expected_ids

def test_filter_skips_missing_and_none_currency(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    # id 4 (no currency) и id 5 (None) не должны быть в результате
    ids = [tx["id"] for tx in result]
    assert 4 not in ids and 5 not in ids

def test_accepts_generator_input(sample_transactions):
    # создаём generator-источник
    def gen():
        for tx in sample_transactions:
            yield tx

    result = list(filter_by_currency(gen(), "EUR"))
    assert [tx["id"] for tx in result] == [2]