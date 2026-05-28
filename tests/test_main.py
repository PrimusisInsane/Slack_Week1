from app.db import total, average

def test_total():
    assert total([10, 20, 30]) == 60

def test_average():
    assert average([10, 20, 30]) == 20