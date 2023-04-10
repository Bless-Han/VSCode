from pytest import raises

def get_number(s):
    return int(s)


def test_get_number():
    with raises(ValueError):
        get_number("9")
