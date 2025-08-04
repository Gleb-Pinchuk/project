from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает список словарей, содержащий только те словари,
    у которых ключ "state" соответствует указанному значению.
    """
    return [item for item in list_of_dict if item.get("state") == state]


def sort_by_date(
    data_list: List[Dict[str, Any]],
    data_key: str = "date",
    descending: bool = True,
) -> List[Dict[str, Any]]:
    """
    Возвращает список словарей, отсортированный по дате (по умолчанию — в порядке убывания).
    """
    return sorted(
        data_list,
        key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=descending,
    )
