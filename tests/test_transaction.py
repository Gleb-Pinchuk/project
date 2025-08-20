from unittest.mock import patch

import pandas as pd

from src.transaction import read_transactions_from_csv, read_transactions_from_excel

csv_file = "C:/Users/ghlie/Downloads/transactions.csv"
excel_file = "C:/Users/ghlie/Downloads/transactions_excel.xlsx"


def test_read_transactions_from_csv_with_mock():
    mock_df = pd.DataFrame({"amount": [100, 200], "currency": ["USD", "EUR"]})
    with patch("pandas.read_csv", return_value=mock_df) as mock_read_csv:
        df = read_transactions_from_csv(csv_file)
        mock_read_csv.assert_called_once_with(csv_file)
        assert df.equals(mock_df)


def test_read_transactions_from_excel_with_mock():
    mock_df = pd.DataFrame({"amount": [300, 400], "currency": ["GBP", "JPY"]})
    with patch("pandas.read_excel", return_value=mock_df) as mock_read_excel:
        df = read_transactions_from_excel(excel_file)
        mock_read_excel.assert_called_once_with(excel_file)
        assert df.equals(mock_df)
