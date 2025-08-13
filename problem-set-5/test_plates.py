from plates import is_valid
import pytest

# --- Tests for is_valid() ---
def test_is_valid_int():
    with pytest.raises(TypeError):
        is_valid(1)

def test_is_valid_plate_starts_with_two_letters():
    assert is_valid("cs50") == True
    assert is_valid("abc1") == True
    assert is_valid("1abc") == False
    assert is_valid("a113") == False
    assert is_valid("1234") == False

def test_is_valid_plate_length():
    assert is_valid("a") == False
    assert is_valid("ab") == True
    assert is_valid("abc") == True
    assert is_valid("abcd") == True
    assert is_valid("abcde") == True
    assert is_valid("abcdef") == True
    assert is_valid("abcdefg") == False

def test_is_valid_plate_numbers_at_end():
    assert is_valid("zy98") == True
    assert is_valid("98zy") == False
    assert is_valid("zy9x8") == False

def test_is_valid_plate_zeros():
    assert is_valid("mn10") == True
    assert is_valid("op01") == False

def test_is_valid_plate_alphanumeric():
    assert is_valid("ab ") == False
    assert is_valid("cd?") == False
    assert is_valid("ef.12") == False
    assert is_valid("gh,34") == False
    assert is_valid("ij!56") == False

def test_is_valid_char_cases():
    assert is_valid("hello") == True
    assert is_valid("BYE") == True
    assert is_valid("WoRlD") == True