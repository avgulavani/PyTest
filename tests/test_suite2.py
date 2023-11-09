import pytest

@pytest.mark.regression
def test_1():
    a=5
    b=5
    assert  a==b

@pytest.mark.regression
def test_2():
    assert False

def test_3():
    assert ""=="TEST"

def test_4():
    a= "demo"
    assert a.upper()==a