import pytest


def value(s):
    return int(s)


def test_value():
    with pytest.raises(ValueError):
        value(20)
