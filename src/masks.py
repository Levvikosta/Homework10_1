def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    if not card_number or len(card_number) < 4:
        return "Неверный номер карты"
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return str(card_number[0:7]) + "** ****" + str(card_number[-4:])


# def get_mask_card_number(card_number: str) -> str:
#     """Маскирует номер карты, оставляя видимыми только первые 4 и последние 4 цифры."""
#     if len(card_number) != 16 or not card_number.isdigit():
#         raise ValueError("Номер карты должен содержать 16 цифр")
#
#     return f"{card_number[:4]}** ****{card_number[12:]}"


def get_mask_account(account: str) -> str:
    """Функция маскирующая номера счета"""
    if not account or len(account) < 4:
        return "**"
    return "**" + str(account[-4:])

