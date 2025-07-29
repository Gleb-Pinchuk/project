from src.widget import mask_account_card, get_date
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
    [('2024-03-11T02:26:18.671407', '11.03.2024'),
     ('2022-05-12', '12.05.2022'),
     ('2024-03-11T02:26', '11.03.2024')]
)
def test_get_date(date, expected):
    result = get_date(date)
    assert result == expected
