from datetime import datetime


def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению
    """

    filtered_list = []

    for x in list_of_dict:
        if x.get("state") == state:
            filtered_list.append(x)
    return filtered_list


def sort_by_date(data_list: list, data_key="date", descending=True) -> list:
    """Функция, возвращает список, отсортированный по дате"""

    
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending)


