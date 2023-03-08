from pytest import raises

def value(s):
    try:
        return int(s)
    except:
        raise ValueError("Enter a number")

def test_value():
    assert value("5") == 5
    with raises(ValueError):
        value(9)


