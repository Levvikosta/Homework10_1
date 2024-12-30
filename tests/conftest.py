import pytest


@pytest.fixture
def filter_data():
    return [
        [{"name": "item1", "state": "active"},
         {"name": "item2", "state": "inactive"},
         {"name": "item3", "state": "active"}],  # Список словарей для фильтрации

        [{"name": "item4", "state": "pending"},
         {"name": "item5", "state": "inactive"},
         {"name": "item6", "state": "pending"}],  # Другой набор словарей

        [{"name": "item7", "state": None}],  # Специальный случай с None

        []  # Пустой список для тестирования
    ]


@pytest.fixture
def sort_data():
    return [
        # Список словарей с корректными датами
        [
            {"name": "item1", "date": "2023-01-05"},
            {"name": "item2", "date": "2021-12-15"},
            {"name": "item3", "date": "2022-11-20"},
        ],

        # Список с одинаковыми датами
        [
            {"name": "item4", "date": "2022-11-20"},
            {"name": "item5", "date": "2022-11-20"},
            {"name": "item6", "date": "2023-01-05"},
        ],

        # Список с некорректными датами
        [
            {"name": "item7", "date": "Not a date"},
            {"name": "item8", "date": "2020-12-25"},
            {"name": "item9", "date": "Invalid"},
        ],

        # Пустой список
        []
    ]