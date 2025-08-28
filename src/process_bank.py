import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует список банковских операций по строке поиска в описании.
    """
    pattern = re.compile(search, re.IGNORECASE)
    result = [op for op in data if "description" in op and pattern.search(op["description"])]
    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по категориям.
    """
    stats = {cat: 0 for cat in categories}

    for op in data:
        desc = op.get("description", "").lower()
        for cat in categories:
            if cat.lower() in desc:
                stats[cat] += 1
                break  # если операция подходит под одну категорию, дальше не проверяем

    return stats
