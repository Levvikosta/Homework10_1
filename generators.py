"""Module for transaction data generators."""

from typing import Iterator, Dict, Any, Union, Iterable


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]], currency: str
) -> Iterator[Dict[str, Any]]:
    """Filter transactions by currency."""
    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        # Вариант 1: Простая структура {"currency": "USD"}
        if transaction.get("currency") == currency:
            yield transaction

        # Вариант 2: Вложенная структура operationAmount.currency.code
        elif (transaction.get("operationAmount") and
                isinstance(transaction["operationAmount"], dict) and
                transaction["operationAmount"].get("currency") and
                isinstance(transaction["operationAmount"]["currency"], dict) and
                transaction["operationAmount"]["currency"].get("code") == currency):
            yield transaction


def _parse_card_number(value: Union[int, str]) -> int:
    """Parse card number to integer."""
    if isinstance(value, int):
        if value < 0:
            raise ValueError("Card number cannot be negative.")
        return value
    if isinstance(value, str):
        digits = value.replace(" ", "")
        if not digits.isdigit():
            raise ValueError(f"Invalid card number: {value!r}")
        return int(digits)
    raise TypeError("start and end must be int or str")


def _format_card(number: int) -> str:
    """Format card number as XXXX XXXX XXXX XXXX."""
    card_str = f"{number:016d}"
    groups = [card_str[i:i + 4] for i in range(0, 16, 4)]
    return " ".join(groups)


def card_number_generator(
    start: Union[int, str], end: Union[int, str]
) -> Iterator[str]:
    """Generate card numbers in range [start, end]."""
    start_num = _parse_card_number(start)
    end_num = _parse_card_number(end)

    if start_num > end_num:
        raise ValueError("Start must be <= end.")

    for number in range(start_num, end_num + 1):
        yield _format_card(number)


def transaction_descriptions(
    transactions: Iterable[Dict[str, Any]]
) -> Iterator[str]:
    """Extract descriptions from transactions."""
    for transaction in transactions:
        if isinstance(transaction, dict):
            description = transaction.get("description")
            if description is not None:
                yield str(description)
