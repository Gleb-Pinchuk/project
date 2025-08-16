import os
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY: str | None = os.getenv("EXCHANGE_API_KEY")
URL = "https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view?pli=1"


def convert_transaction(transaction: dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.

    - Если валюта RUB — возвращает исходное значение.
    - Если валюта USD или EUR — конвертирует в рубли через API.
    - Если транзакция пустая или валюта не поддерживается — ошибка.
    """
    if not transaction:
        raise ValueError("Пустая транзакция")

    amount: float = float(transaction["operationAmount"]["amount"])
    currency: str = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        if not API_KEY:
            raise EnvironmentError("API ключ не найден в переменных окружения")

        params: dict[str, str] = {
            "to": "RUB",
            "from": currency,
            "amount": str(amount),
        }
        headers: dict[str, str] = {"apikey": API_KEY}

        response = requests.get(URL, params=params, headers=headers)
        response.raise_for_status()
        data: dict[str, Any] = response.json()

        if "result" not in data:
            raise ValueError("Ошибка ответа API: ключ 'result' отсутствует")

        return float(data["result"])

    raise ValueError(f"Неподдерживаемая валюта: {currency}")

