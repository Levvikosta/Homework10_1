import pytest
from generators import card_number_generator

def test_card_number_generator_basic_range_string_format():
    start = "0000 0000 0000 0001"
    end = "0000 0000 0000 0010"
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
        "0000 0000 0000 0007",
        "0000 0000 0000 0008",
        "0000 0000 0000 0009",
        "0000 0000 0000 0010",
    ]
    produced = list(card_number_generator(start, end))
    assert produced == expected

def test_card_number_generator_basic_range_int_inputs():
    start, end = 1, 3
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]
    produced = list(card_number_generator(start, end))
    assert produced == expected

def test_card_number_generator_invalid_range_raises():
    # start > end должен приводить к ValueError
    with pytest.raises(ValueError):
        list(card_number_generator("0000 0000 0000 0010", "0000 0000 0000 0001"))

def test_card_number_generator_formatting_and_leading_zeros():
    # проверяем нулевой номер и продолжение
    start = "0000 0000 0000 0000"
    end = "0000 0000 0000 0002"
    out = list(card_number_generator(start, end))
    assert out[0] == "0000 0000 0000 0000"
    assert out[1] == "0000 0000 0000 0001"
    assert out[2] == "0000 0000 0000 0002"

def test_card_number_generator_large_range_behaviour():
    # небольшой, но более широкий диапазон для проверки производительности и корректности
    start = "0000 0000 0000 0090"
    end = "0000 0000 0000 0999"  # 90 до 999
    out = list(card_number_generator(start, end))
    assert out[0] == "0000 0000 0000 0090"
    assert out[-1] == "0000 0000 0000 0999"
    assert len(out) == 910  # 999 - 90 + 1