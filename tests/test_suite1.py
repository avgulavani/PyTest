import pytest

def test_1():
    a = 3
    b = 4
    assert a == b

@pytest.mark.regression
def test_2():
    assert True

def test_3():
    assert "test" == "TEST"
@pytest.mark.smoke
def test_4():
    a = "demo"
    assert a.upper() == a
