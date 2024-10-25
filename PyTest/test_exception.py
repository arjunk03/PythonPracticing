import pytest


def divide(dividend, divisor):
    return dividend / divisor


@pytest.mark.num
def test_divide_pass():
    assert divide(10, 2) == 5


@pytest.mark.num
def test_divide_error_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.skip(reason="temp skip")
def test_divide_error_type():
    with pytest.raises(TypeError):
        divide(10, "a") == 5


@pytest.mark.skip
def test_divide_error_type2():
    with pytest.raises(TypeError):
        divide(10, "a") == 5
