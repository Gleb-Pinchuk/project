import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


@pytest.mark.parametrize("currency", ["USD", "RUB", "EUR"])
def test_filter_by_currency(currency):
    result = list(filter_by_currency(transactions, currency))
    assert all(t["operationAmount"]["currency"]["code"] == currency for t in result)
    expected = [t for t in transactions if t["operationAmount"]["currency"]["code"] == currency]
    assert result == expected


@pytest.mark.parametrize(
    "input_transactions, expected",
    [
        (transactions, ["Перевод организации", "Перевод со счета на счет"]),
        ([], []),
    ],
)
def test_transaction_descriptions(input_transactions, expected):
    result = list(transaction_descriptions(input_transactions))
    assert result == expected


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (12, 12, ["0000 0000 0000 0012"]),
        (5, 4, []),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
