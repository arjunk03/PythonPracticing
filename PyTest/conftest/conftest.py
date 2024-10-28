@pytest.fixture
def test_file():
    print("\n opening file")
    f = open("test_fil.txt", "a+")
    yield f

    print("closing the file")
    f.close()
