import json
import os
from typing import Any, Dict, List
from src.masks import LOG_FILE
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename=LOG_FILE,
    filemode="w",
    encoding="utf-8"
)
logger = logging.getLogger()


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Если файл не найден, пустой или содержит не список — возвращает пустой список.
    """
    if not os.path.exists(file_path):
        logger.warning("Файл %s не найден", file_path)
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                logger.info("Файл %s пустой", file_path)
                return []

            data = json.loads(content)
            if isinstance(data, list):
                logger.debug("Загружено %d транзакций", len(data))
                return [item for item in data if isinstance(item, dict)]
            else:
                logger.warning("Файл %s содержит некорректный формат", file_path)
                return []
    except (json.JSONDecodeError, OSError) as e:
        logger.error("Ошибка при загрузке файла %s: %s", file_path, e)
        return []


transactions = load_transactions("data/operations.json")
print(transactions)
