import pytest
from src.generators import transaction_descriptions, filter_by_currency, card_number_generator
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
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
    [(transactions,[
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),(transactions[:3],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
            ],
        ),
        (
            [],
            [],
        ),
    ],
)
def test_transaction_descriptions(input_transactions, expected):
    result = list(transaction_descriptions(input_transactions))
    assert result == expected


@pytest.mark.parametrize(
        "start, stop, done",
        [
            (1, 1, ["0000 0000 0000 0001"]),
            (1, 3, [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ]),
            (12, 12, ["0000 0000 0000 0012"]),
            (5, 4, []),
        ]
    )
def test_card_number_generator(start, stop, done):
    result_1 = list(card_number_generator(start, stop))
    assert result_1 == done