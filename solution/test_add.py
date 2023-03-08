from add import value
from pytest import raises

def test_value():
    with raises(ValueError):
        value("ssss")
