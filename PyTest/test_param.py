import cal
import pytest


@pytest.mark.parametrize(
    "a, b, c", [(1, 2, 3), (5.2, 2.4, 7.6), ("the", " end", "the end")]
)
def test_add(a, b, c):
    assert cal.add(a, b) == c
