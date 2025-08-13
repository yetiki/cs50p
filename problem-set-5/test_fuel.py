from fuel import convert, gauge
import pytest

# --- Tests for convert() ---
def test_convert_invalid_values():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("-1/1")
    with pytest.raises(ValueError):
        convert("1/-1")
    with pytest.raises(ValueError):
        convert("-1/-1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_format():
    with pytest.raises(TypeError):
        convert(1/2)
    with pytest.raises(ValueError):
        convert("1\\1")
    with pytest.raises(ValueError):
        convert("/1")
    with pytest.raises(ValueError):
        convert("1/")
    with pytest.raises(ValueError):
        convert("1/2/3")

def test_convert_whitespace():
    assert convert(" 1/2 ") == 50
    assert convert("2/ 5") == 40
    assert convert(" 11/20 ") == 55

def test_convert_large_values():
    assert convert("1000/2000") == 50
    assert convert("500/1000") == 50
    assert convert("999/1000") == 100

def test_convert_full_feul():
    assert convert("1/1") == 100
    assert convert("5/5") == 100
    assert convert("100/100") == 100

def test_convert_empty_feul():
    assert convert("1/100") == 1
    assert convert("0/100") == 0
    assert convert("5/1000") == 0

def test_convert_percentage_feul():
    assert convert("2/100") == 2
    assert convert("98/100") == 98
    assert convert("1/2") == 50
    assert convert("1/3") == 33

# --- Tests for gauge() ---
def test_gauge_invalid_values():
    with pytest.raises(ValueError):
        gauge(-1)
    with pytest.raises(ValueError):
        gauge(101)
    with pytest.raises(TypeError):
        gauge(1.5)
    with pytest.raises(TypeError):
        gauge("50")
    with pytest.raises(TypeError):
        gauge(None)

def test_gauge_empty_feul():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full_feul():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_percentage_feul():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"