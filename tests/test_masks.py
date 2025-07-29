from src.masks import get_mask_account, get_mask_card_number
import pytest


@pytest.mark.parametrize(
    'account, expected',
    [(1111222233334444, 'Visa Platinum 1111 22 ** **** 4444'),
     (1111, 'Некорректный ввод'), (11112222333344445, 'Некорректный ввод')]
)
def test_get_mask_card_number(account, expected):
    result = get_mask_card_number(account)
    assert result == expected


@pytest.fixture()
def card_numbers():
    return 112222


@pytest.fixture()
def card_numbers_1():
    return 12345678


def test_get_mask_account_2(card_numbers_1):
    result = get_mask_account(card_numbers_1)
    assert result == 'Счет **5678'


def test_get_mask_account(card_numbers):
    result = get_mask_account(card_numbers)
    assert result == 'Счет **2222'


def test_get_mask_account_1():
    result = get_mask_account(' ')
    assert result == 'Некорректный ввод'
