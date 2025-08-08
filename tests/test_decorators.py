import pytest
from src.decorators import log, my_function, second_fun


def test_my_function_success(capsys):
    """Тест: успешное выполнение my_function — проверка вывода в консоль."""
    result = my_function(2, 3)
    assert result == 5

    captured = capsys.readouterr()

    assert "Функция my_function ок. Результат: 5" in captured.out
    assert "Начало:" in captured.out
    assert "Конец:" in captured.out
    assert "Время выполнения:" in captured.out


def test_second_fun_exception(capsys):
    """Тест: вызов ошибки в second_fun — проверка лога ошибки."""
    with pytest.raises(ZeroDivisionError):
        second_fun(5, 0)

    captured = capsys.readouterr()

    assert "second_fun error: division by zero" in captured.out
    assert "Inputs: (5, 0)" in captured.out
    assert "Начало:" in captured.out
    assert "Конец:" in captured.out


def test_log_to_file(tmp_path):
    """Тест: запись лога в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def temp_func(a, b):
        return a - b

    result = temp_func(10, 3)
    assert result == 7

    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    assert "Функция temp_func ок. Результат: 7" in content
    assert "Начало:" in content
    assert "Конец:" in content


def test_log_file_exception(tmp_path):
    """Тест: ошибка и запись в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def bad_func():
        raise RuntimeError("Ошибка!")

    with pytest.raises(RuntimeError):
        bad_func()

    content = log_file.read_text(encoding="utf-8")
    assert "bad_func error: Ошибка!" in content
    assert "Inputs: (), {}" in content
