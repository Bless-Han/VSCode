import pytest

from solution import CQueue

def test_cqueue():
    cqueue = CQueue()
    assert cqueue.deleteHead() == -1
    cqueue.appendTail(5)
    cqueue.appendTail(2)
    assert cqueue.deleteHead() == 5
    assert cqueue.deleteHead() == 2
    assert cqueue.deleteHead() == -1

