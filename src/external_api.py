import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(amount: float, from_currency: str, to_currency: str = "RUB") -> float:
    if not API_KEY:
        raise EnvironmentError("API ключ не найден в переменных окружения")
    params = {"to": to_currency, "from": from_currency, "amount": amount}
    headers = {"apikey": API_KEY}
    response = requests.get(BASE_URL, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    if "result" not in data:
        raise ValueError("Ошибка ответа API: ключ 'result' отсутствует")
    return float(data["result"])


def transaction_amount(transaction: dict) -> float:
    if not transaction:
        raise ValueError("Пустая транзакция")
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency in ("USD", "EUR"):
        return convert_currency(amount, currency)
    else:
        raise ValueError(f"Неподдерживаемая валюта: {currency}")
