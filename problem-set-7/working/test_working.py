import pytest
from working import convert

def test_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

    with pytest.raises(ValueError):
        convert("foo")
    with pytest.raises(ValueError):
        convert("9:00AMto5:00PM")
    with pytest.raises(ValueError):
        convert("from 9:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_mixed_formats():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"

def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

    assert convert("11:59 AM to 11:59 PM") == "11:59 to 23:59"

def test_meridiem_cases():
    with pytest.raises(ValueError):
        convert("9:00 am to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 Am to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 aM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 pm")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 Pm")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 pM")

def test_mixed_meridiem():
    assert convert("9:00 AM to 5:00 AM") == "09:00 to 05:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9:00 PM to 5:00 PM") == "21:00 to 17:00"

def test_hour_ranges():
    with pytest.raises(ValueError):
        convert("00:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 0:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")

    assert convert("6:00 AM to 6:00 PM") == "06:00 to 18:00"

def test_minute_ranges():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")

    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"