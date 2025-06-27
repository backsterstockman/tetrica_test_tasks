import pytest
from src.task3.solution import time_together, tests


@pytest.mark.parametrize(
        "tests",
        [tests]
)
def test_time_together(tests):
    for test in tests:
        result = time_together(test['intervals'])
        assert result == test['answer']
