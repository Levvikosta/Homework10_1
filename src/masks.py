def get_mask_card_number(card_number: str) -> str:
    '''Функция маскировки номера карты'''
    if not card_number or len(card_number) < 4:
        return "Неверный номер карты"
    return str(card_number[0:7]) + "** ****" + str(card_number[-4:])


def get_mask_account(account: str) -> str:
    '''Функция маскирующая номера счета'''
    if not account or len(account) < 4:
        return "**"
    return "**" + str(account[-4:])


