from bank import value
import pytest

# --- Tests for value() ---
def test_value_with_int():
    with pytest.raises(TypeError):
        value(1)

def test_value_with_lowercase():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("morning") == 100

def test_value_with_uppercase():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("AFTERNOON") == 100

def test_value_with_mixedcase():
    assert value("HeLlo") == 0
    assert value("HoWdY") == 20
    assert value("EvEnInG") == 100

def test_value_with_empty_string():
    assert value("") == 100
    assert value(" ") == 100

def test_value_with_trailing_spaces():
    assert value("hello   ") == 0
    assert value("how do   ") == 20
    assert value("good day   ") == 100

def test_value_with_hello():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("hellothere") == 0
    assert value("well hello") == 100
    assert value("well hello friend") == 100
    assert value("h ello") == 20
