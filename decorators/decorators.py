import functools
import time


def null_decorator(func):
    return func


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def strong(func):
    @functools.wraps(func)
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    @functools.wraps(func)
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


@null_decorator
@strong
@uppercase
@emphasis
def greet():
    return 'Hello!'


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


def timer(func):
    def wrapper(*args, **kwargs):
        # записать время перед вызовом функции
        start_time = time.time()
        # вызвать функцию
        result = func(*args, **kwargs)
        # записать время после выполнения функции
        end_time = time.time()
        # рассчитать время выполнения и вывести значение
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time} секунд")
        # вернуть результат выполнения функции
        return result

    # вернуть результат функции wrapper
    return wrapper


@timer
def train_model():
    print("Запуск выполнения функции ...")
    # имитируйте выполнение функции, приостановив выполнение программы на 3 секунд
    time.sleep(3)
    print("Выполнение функции завершено!")



if __name__ == '__main__':
    # print(greet())
    # print(say('Jane', 'Hello, World'))
    # print(say)
    train_model()
