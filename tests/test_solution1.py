import pytest
from src.task1.solution import func1, func2, func3, func4


@pytest.mark.parametrize(
    "func, arg, expected_error",
    [
        (func1, 1, False),
        (func2, True, False),
        (func3, 1.0, False),
        (func4, 'Hello', False),
        (func1, 'Hello', True),
        (func2, "", True),
        (func3, True, True),
        (func4, 1, True),
    ]
)
def test_strict(func, arg, expected_error):
    if expected_error:
        with pytest.raises(TypeError):
            func(arg)
    else:
        assert func(arg) == arg
