import pytest
from unittest.mock import patch
from src.external_api import transaction_amount


@patch("external_api.currency.convert_currency", return_value=7500.0)
def test_transaction_usd(mock_convert):
    tx = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    assert transaction_amount(tx) == 7500.0
    mock_convert.assert_called_once_with(100.0, "USD")


def test_transaction_rub():
    tx = {"operationAmount": {"amount": "123.45", "currency": {"code": "RUB"}}}
    assert transaction_amount(tx) == 123.45


def test_empty_transaction():
    with pytest.raises(ValueError):
        transaction_amount({})


def test_unsupported_currency():
    tx = {"operationAmount": {"amount": "50", "currency": {"code": "GBP"}}}
    with pytest.raises(ValueError):
        transaction_amount(tx)
