import logging
import os
from typing import Union

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "application.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename=LOG_FILE,
    filemode="w",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция возвращает маску номера карты в формате:
    Visa Platinum XXXX XX** **** XXXX
    """
    card_number = str(card_number)
    if len(card_number) == 16:
        return f"Visa Platinum {card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"
    logger.warning("Некорректный ввод номера карты")
    return "Некорректный ввод"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция возвращает маску номера счёта в формате:
    Счет **XXXX
    """
    account_number = str(account_number)
    if len(account_number) >= 4:
        return f"Счет **{account_number[-4:]}"
    logger.warning("Некорректный ввод номера счёта")
    return "Некорректный ввод"


if __name__ == "__main__":
    # Проверка логирования
    print(get_mask_account("12"))
