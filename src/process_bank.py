import re
from typing import List, Dict
from collections import Counter


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует список операций по слову/регулярному выражению в поле description.
    """
    if not search.strip():
        return []

    pattern = re.compile(search, re.IGNORECASE)
    return [op for op in data if "description" in op and pattern.search(op["description"])]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям (по description).
    """
    # приводим категории к нижнему регистру для поиска
    categories_lower = [cat.lower() for cat in categories]
    counter = Counter()

    for op in data:
        desc = op.get("description", "").lower()
        for i, cat in enumerate(categories_lower):
            if cat in desc:
                counter[categories[i]] += 1
                break

    return {cat: counter.get(cat, 0) for cat in categories}
