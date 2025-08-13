import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Если файл не найден, пустой или содержит не список — возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []

            data = json.loads(content)
            if isinstance(data, list):
                # Проверяем, что каждый элемент — словарь
                return [item for item in data if isinstance(item, dict)]
            return []
    except (json.JSONDecodeError, OSError):
        return []
