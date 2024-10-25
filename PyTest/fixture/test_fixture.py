import pytest
import os


@pytest.fixture
def test_file():
    print("\n creating a  file")
    f = open("test_file", "a+")
    return f


def test_fix(test_file):
    num_lines_before = len([line for line in open(test_file.name)])

    for val in range(10):
        test_file.write(str(val) + "\n")
    test_file.flush()
    num_lines_after = len([line for line in open(test_file.name)])

    assert (num_lines_after - num_lines_before) == 10
    test_file.close()
