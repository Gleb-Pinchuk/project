import pytest
from unittest.mock import patch, mock_open
from src.external_api import convert_transaction
from src.utils import load_transactions


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


def test_file_not_found():
    result = load_transactions("nonexistent.json")
    assert result == []


def test_empty_file():
    m = mock_open(read_data="")
    with patch("builtins.open", m), patch("os.path.exists", return_value=True):
        result = load_transactions("dummy.json")
    assert result == []


def test_invalid_json():
    m = mock_open(read_data="not a json")
    with patch("builtins.open", m), patch("os.path.exists", return_value=True):
        result = load_transactions("dummy.json")
    assert result == []


def test_valid_json():
    data = '[{"id": 1}, {"id": 2}]'
    m = mock_open(read_data=data)
    with patch("builtins.open", m), patch("os.path.exists", return_value=True):
        result = load_transactions("dummy.json")
    assert result == [{"id": 1}, {"id": 2}]
