import pytest
from src.task1.decorator import func1, func2, func3, func4


@pytest.mark.parametrize(
    "func, arg", 
    [
        (func1, 1),
        (func2, True),
        (func3, 1.0),
        (func4, 'Hello')
    ]
)
def test_strict(func, arg):
    assert func(arg) == arg
