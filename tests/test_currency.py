import pytest
from unittest.mock import patch
from src.external_api import convert_transaction


def test_convert_rub_transaction() -> None:
    tx = {"operationAmount": {"amount": "123.45", "currency": {"code": "RUB"}}}
    assert convert_transaction(tx) == 123.45


@patch("src.external_api.requests.get")
def test_convert_usd_transaction(mock_get) -> None:
    # Настраиваем фейковый ответ API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    tx = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    result = convert_transaction(tx)

    assert result == 7500.0
    mock_get.assert_called_once()


def test_empty_transaction() -> None:
    with pytest.raises(ValueError):
        convert_transaction({})


def test_unsupported_currency() -> None:
    tx = {"operationAmount": {"amount": "50", "currency": {"code": "GBP"}}}
    with pytest.raises(ValueError):
        convert_transaction(tx)

