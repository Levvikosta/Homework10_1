from datetime import datetime


def mask_account_card(account_number: str) -> str:
    account_number = ''.join(filter(str.isdigit, account_number))

    if len(account_number) == 16:  # если это номер карты
        return f"**** **** **** {account_number[-4:]}"
    elif len(account_number) >= 10:  # если это номер счета
        return '*' * (len(account_number) - 4) + account_number[-4:]

    else:
        raise ValueError("Неверный формат номера. Должен содержать как минимум 10 чисел.")


def get_data(date_str: str) -> str:
    """Функция преобразования даты из строки в формат 'YYYY-MM-DD'."""
    if not date_str:
        return "Нет даты"

    formats = [
        "%Y-%m-%d",  # формат: 2023-10-25
        "%d-%m-%Y",  # формат: 25-10-2023
        "%m/%d/%Y",  # формат: 10/25/2023
        "%Y.%m.%d",  # формат: 2023.10.25
        "%B %d, %Y",  # формат: October 25, 2023
    ]

    for fmt in formats:
        try:
            date_object = datetime.strptime(date_str, fmt)
            return date_object.strftime('%Y-%m-%d')
        except ValueError:
            continue

    return "Неверный формат даты"
