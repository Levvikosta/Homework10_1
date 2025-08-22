from typing import Iterator, List, Dict, Any, Union

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Возвращает итератор, который поочередно выдает транзакции,
    у которых поле 'currency' совпадает с указанной валютой"""

    for tx in transactions:
        parts = []

        tx_id = tx.get("id")
        if tx_id is not None:
            parts.append(f"Transaction {tx_id}")

        ttype = tx.get("type")
        if ttype:
            parts.append(f"Type: {ttype}")

        amount = tx.get("amount")
        currency = tx.get("currency")
        if amount is not None:
            if currency:
                parts.append(f"Summa: {amount} {currency}")
            else:
                parts.append(f"Summa: {amount}")

        date = tx.get("date")
        if date:
            parts.append(f"date: {date}")

        description = tx.get("description")
        if description:
            parts.append(f"description: {description}")  # можно оставить 'описание'

        yield ", ".join(parts) if parts else "Transaction"


def _parse_card_number(value: Union[int, str]) -> int:
    """Преобразует входное значение к целому числу, удаляя пробелы.
    Принимает либо int, либо строку вида 'XXXX XXXX XXXX XXXX' или 'XXXXXXXXXXXXXXXX'"""
    if isinstance(value, int):
        if value < 0:
            raise ValueError("Карта не может иметь отрицательный номер.")
        return value
    if isinstance(value, str):
        digits = value.replace(" ", "")
        if not digits.isdigit():
            raise ValueError(f"Некорректный номер карты: {value!r}")
        return int(digits)
    raise TypeError("start и end должны быть int или str")

def _format_card(n: int) -> str:
    """Форматирует 16-значное число в вид 'XXXX XXXX XXXX XXXX' с ведущими нулями"""
    s = f"{n:016d}"
    groups = [s[i:i+4] for i in range(0, 16, 4)]
    return " ".join(groups)

def card_number_generator(start: Union[int, str], end: Union[int, str]) -> Iterator[str]:
    """Генератор: выдает номера банковских карт в диапазоне [start, end].
    Формат вывода: 'XXXX XXXX XXXX XXXX'.
    Диапазон считается по целочисленным значениям 16-цифровых номеров."""
    s = _parse_card_number(start)
    e = _parse_card_number(end)

    if s > e:
        raise ValueError("Начальное значение диапазона должно быть не больше конечного.")

    for n in range(s, e + 1):
        yield _format_card(n)
