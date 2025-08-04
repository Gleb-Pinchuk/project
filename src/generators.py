from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Функция, фильтрующая входящую информацию по валюте"""
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Функция, которая возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Функция, которая возвращает номер карты в виде 0000 0000 0000 0001"""
    for i in range(start, stop+1):
        num = str(i).zfill(16)
        yield f'{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}'
