import pandas as pd

csv_file = "C:/Users/ghlie/Downloads/transactions.csv"
excel_file = "C:/Users/ghlie/Downloads/transactions_excel.xlsx"


def read_transactions_from_csv(path: str) -> pd.DataFrame:
    """Чтение CSV-файла с транзакциями"""
    return pd.read_csv(path)


def read_transactions_from_excel(path: str) -> pd.DataFrame:
    """Чтение Excel-файла с транзакциями"""
    return pd.read_excel(path)
