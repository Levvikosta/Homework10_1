from typing import Iterable, Any, List, Dict


def filter_by_state(dict_list: Iterable[list[dict[Any, Any]]], state: Any='EXECUTED')-> list[list[dict[Any, Any]]]:
    '''Функция для выведения данных по значению'''
    executed_list = []
    for i in dict_list:
        if i['state'] == state:
            executed_list.append(i)
    return executed_list


def sort_by_date(dictionaries: Iterable[list[dict[Any, Any]]], reverse: bool =True) -> list[list[dict[Any, Any]]]:
    '''Функция для сортировки по датам'''
    list_by_date = sorted(dictionaries, key = lambda x: x['date'], reverse=reverse)
    return list_by_date


