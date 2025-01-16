from typing import Iterable, Any
from datetime import datetime


def filter_by_state(dict_list: Iterable[list[dict[Any, Any]]], state: Any = 'EXECUTED') -> list[list[dict[Any, Any]]]:
    """Функция для выведения данных по значению"""
    executed_list = []
    for i in dict_list:
        if i["state"] == state:
            executed_list.append(i)
    return executed_list


def sort_by_date(data: list, ascending: bool = True) -> list:
    """Функция для сортировки по датам"""

    def parse_date(date_str):
        formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y.%m.%d", "%d %B %Y", "%B %d, %Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None

    valid_data = [(item, parse_date(item.get('date'))) for item in data]
    valid_data = [item for item in valid_data if item[1] is not None]

    sorted_data = sorted(valid_data, key=lambda x: x[1], reverse=not ascending)

    return [item[0] for item in sorted_data]
