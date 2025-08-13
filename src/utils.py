import json
import os


def load_transactions(file_path: str):
    """
    Загружает список транзакций из JSON-файла.

    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []

            data = json.loads(content)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []
