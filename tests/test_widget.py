from src.widget import mask_account_card
import pytest


@pytest.mark.parametrize(
    'account, expected',
    [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79 ** **** 6361'),
     ('700', 'Некорректный ввод'), ('Счет 73654108430135874305', 'Счет **4305'),
     ('12', 'Некорректный ввод')]
)
def test_mask_account_card(account, expected):
    result = mask_account_card(account)
    assert result == expected


@pytest.mark.parametrize(
    'date, expected',

)
