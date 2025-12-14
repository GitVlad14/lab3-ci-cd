from app import add, reverse_string


def test_add():
    assert add(2, 3) == 5


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
