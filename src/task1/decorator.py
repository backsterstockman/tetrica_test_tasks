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
        try:
            for key, value in arguments.items():
                if type(value) is annotations[key]:
                    continue
                else:
                    raise ValueError('Типы параметров, переданных в ф-ию, не соответствуют ожидаемым')
        except ValueError as e:
            print(e)
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
