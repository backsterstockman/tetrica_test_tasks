import inspect
from functools import wraps


def strict(func):
    func_signature = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        print(func_signature)
        arguments = func_signature.bind(*args, **kwargs).arguments
        print(arguments)
        result = func(*args, **kwargs)
        for key, value in arguments.items():
            if type(value) is annotations[key]:
                continue
            else:
                raise TypeError('Типы параметров, переданных в ф-ию, не соответствуют ожидаемым')
        return result
    return wrapper


@strict
def func1(argInt: int):
    return argInt


@strict
def func2(argBool: bool):
    return argBool


@strict
def func3(argFloat: float):
    return argFloat


@strict
def func4(argStr: str):
    return argStr


if __name__ == '__main__':
    func1(1)
    func1('')
