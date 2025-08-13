import time
from functools import wraps
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            start_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                end_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
                duration = end_time - start_time
                log_message = (
                    f"Начало: {start_str}\n"
                    f"Функция {func_name} ок. Результат: {result}\n"
                    f"Конец: {end_str}\n"
                    f"Время выполнения: {duration:.4f} сек.\n\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message)

                return result

            except Exception as e:
                end_time = time.time()
                end_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
                error_message = (
                    f"Начало: {start_str}\n"
                    f"{func_name} error: {e}. Inputs: {args}, {kwargs}\n"
                    f"Конец: {end_str}\n\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator


@log()
def my_function(x: int, y: int) -> int:
    return x + y


@log()
def second_fun(x: float, y: float) -> float:
    return x / y
