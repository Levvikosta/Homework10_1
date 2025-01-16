import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("input_data, state, expected_output", [
    ([{"name": "item1", "state": "active"},
      {"name": "item2", "state": "inactive"},
      {"name": "item3", "state": "active"}],
     "active",
     [{"name": "item1", "state": "active"}, {"name": "item3", "state": "active"}]),

    ([{"name": "item1", "state": "active"},
      {"name": "item2", "state": "inactive"}],
     "inactive",
     [{"name": "item2", "state": "inactive"}]),

    ([{"name": "item1", "state": "active"},
      {"name": "item2", "state": "inactive"},
      {"name": "item3", "state": "inactive"}],
     "active",
     [{"name": "item1", "state": "active"}]),

    ([{"name": "item1", "state": "pending"},
      {"name": "item2", "state": "pending"}],
     "pending",
     [{"name": "item1", "state": "pending"}, {"name": "item2", "state": "pending"}]),

    ([{"name": "item1", "state": "active"},
      {"name": "item2", "state": "inactive"}],
     "archived",
     []),  # Тест на отсутствие статуса

    ([{"name": "item1", "state": None}],
     None,
     [{"name": "item1", "state": None}]),  # Проверка None как валидный статус

    ([], "active", []),  # Пустой список
])
def test_filter_by_state(input_data, state, expected_output):
    assert filter_by_state(input_data, state) == expected_output


@pytest.mark.parametrize("input_data, ascending, expected_output", [
    ([
         {"name": "item1", "date": "2023-01-05"},
         {"name": "item2", "date": "2021-12-15"},
         {"name": "item3", "date": "2022-11-20"},
     ], True, [
         {"name": "item2", "date": "2021-12-15"},
         {"name": "item3", "date": "2022-11-20"},
         {"name": "item1", "date": "2023-01-05"},
     ]),
    ([
         {"name": "item1", "date": "2023-01-05"},
         {"name": "item2", "date": "2021-12-15"},
         {"name": "item3", "date": "2022-11-20"},
     ], False, [
         {"name": "item1", "date": "2023-01-05"},
         {"name": "item3", "date": "2022-11-20"},
         {"name": "item2", "date": "2021-12-15"},
     ]),
    ([
         {"name": "item1", "date": "2023-01-05"},
         {"name": "item2", "date": "2023-01-05"},
         {"name": "item3", "date": "2022-11-20"},
     ], True, [
         {"name": "item3", "date": "2022-11-20"},
         {"name": "item1", "date": "2023-01-05"},
         {"name": "item2", "date": "2023-01-05"},
     ]),
    ([
         {"name": "item1", "date": "Not a date"},
         {"name": "item2", "date": "2020-12-25"},
         {"name": "item3", "date": "Invalid"},
     ], True, [
         {"name": "item2", "date": "2020-12-25"},
     ]),
    ([], True, []),  # Пустой список
])
def test_sort_by_date(input_data, ascending, expected_output):
    assert sort_by_date(input_data, ascending) == expected_output
