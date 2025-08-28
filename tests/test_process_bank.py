import pytest

from src.process_bank import process_bank_operations, process_bank_search


@pytest.mark.parametrize(
    "search,expected_ids",
    [
        ("перевод", [1]),
        ("ОПЛАТА", [3]),
        ("не существует", []),
        ("", []),
    ],
)
def test_process_bank_search(search: str, expected_ids: list[int]) -> None:
    data = [
        {"id": 1, "description": "Перевод на карту"},
        {"id": 2, "description": "Снятие наличных"},
        {"id": 3, "description": "Оплата мобильной связи"},
    ]
    result = process_bank_search(data, search)
    assert [op["id"] for op in result] == expected_ids


@pytest.mark.parametrize(
    "data,categories,expected",
    [
        (
            [
                {"id": 1, "description": "Перевод на карту"},
                {"id": 2, "description": "Снятие наличных"},
                {"id": 3, "description": "Оплата мобильной связи"},
                {"id": 4, "description": "Перевод другу"},
            ],
            ["Перевод", "Снятие", "Оплата"],
            {"Перевод": 2, "Снятие": 1, "Оплата": 1},
        ),
        (
            [{"id": 1, "description": "Зачисление зарплаты"}],
            ["Перевод", "Снятие"],
            {"Перевод": 0, "Снятие": 0},
        ),
        (
            [{"id": 1, "description": "оплата ЖКХ"}],
            ["Оплата"],
            {"Оплата": 1},
        ),
    ],
)
def test_process_bank_operations(
    data: list[dict], categories: list[str], expected: dict[str, int]
) -> None:
    result = process_bank_operations(data, categories)
    assert result == expected
