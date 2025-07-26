from masks import get_mask_card_number, get_mask_account

from masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """ Функция обрабатывает информацию о картах и счетах, возвращает замаскированный номер """
    info_card_split = info_card.split()
    number_card = info_card_split[-1]
    if info_card_split[0] == "Счет":
        result = get_mask_account(number_card)
    else:
        result = get_mask_card_number(number_card)
    return result


def get_date(date_str: str) -> str:
    """ Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ' """
    new_date_str = f'{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}'
    return new_date_str
