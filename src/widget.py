from datetime import datetime


# функция для определения типа входных данных и применения соответствующей маскировки
def mask_account_card(data: str, data_type: str) -> str:
    if data_type == "card":
        return get_mask_card_number(data)
    elif data_type == "account":
        return get_mask_account(data)
    else:
        return "Неверный тип данных"


def get_data(date_str: str) -> str:
    """Преобразует строку с датой в формат 'YYYY-MM-DD'."""
    if not date_str.strip():
        return "Дата отсутствует"

    # Попробуем распознать дату в нескольких форматах
    formats = [
        "%Y-%m-%d",  # Часть форматов, которые мы ожидаем.
        "%d/%m/%Y",
        "%m-%d-%Y",
        "%d-%m-%Y",
        "%Y.%m.%d",
        "%d %B %Y",  # Например: '5 January 2023'
        "%B %d, %Y",  # Например: 'January 5, 2023'
    ]

    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            continue

    return "Некорректный формат даты"