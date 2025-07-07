from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция, которая возвращает маску номера XXXX XX** **** XXXX"""

    card_number = str(card_number)
    if len(card_number) == 16:
        mask_number = f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"
        return mask_number
    return "Некорректный ввод"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция, которая возвращает маску номера ** XXXX"""
    account_number = str(account_number)
    if len(account_number) >= 4:
        mask_account = f"**{account_number[-4:]}"
        return mask_account
    return "Некорректный ввод"


def get_date(date_str: str) -> str:
    """ Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ' """
    new_date_str = f'{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}'
    return new_date_str

