import pytest
from generators import transaction_descriptions

import pytest
from generators import transaction_descriptions

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "amount": 100, "currency": "USD", "description": "Pay"},
        {"id": 2, "amount": None, "currency": "  ", "note": "no currency"},
        {"id": 3, "amount": 50},  # нет description
        {"id": 4, "amount": 75, "currency": "eur", "note": "lowercase currency"},
        {"id": 5, "amount": 0, "currency": 123, "description": "numeric currency"},
        "not-a-dict"  # не словарь
    ]

@pytest.mark.parametrize(
    "tx_index, expected",
    [
        (0, "Pay"),  # Просто description из первой транзакции
        (1, "numeric currency"),  # description из последней транзакции
    ],
)
def test_transaction_descriptions_basic(sample_transactions, tx_index, expected):
    descs = list(transaction_descriptions(sample_transactions))
    assert descs[tx_index] == expected

def test_transaction_descriptions_skips_non_dict(sample_transactions):
    descs = list(transaction_descriptions(sample_transactions))
    # Должны остаться только 2 транзакции с description (индексы 0 и 4)
    assert len(descs) == 2
    assert descs == ["Pay", "numeric currency"]