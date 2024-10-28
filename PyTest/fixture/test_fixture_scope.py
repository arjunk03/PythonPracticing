import pytest
import os


@pytest.fixture(scope="module")
def test_file():
    print("\n opening file")
    f = open("test_fil.txt", "a+")
    yield f

    print("closing the file")
    f.close()


def test_fix(test_file):
    num_lines_before = len([line for line in open(test_file.name)])

    for val in range(10):
        test_file.write(str(val) + "\n")
    test_file.flush()
    num_lines_after = len([line for line in open(test_file.name)])

    assert (num_lines_after - num_lines_before) == 10
    test_file.close()
