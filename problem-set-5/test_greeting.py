from greeting import hello, goodbye
import pytest

# --- Tests for hello() ---
def test_hello_default():
    assert hello() == "hello, world"

def test_hello_with_name():
    assert hello("Alice") == "hello, Alice"

# --- Tests for goodbye() ---
def test_goodbye_default():
    assert goodbye() == "goodbye, world"

def test_goodbye_with_name():
    assert goodbye("Bob") == "goodbye, Bob"

# --- Tests for hello(), goodbye() default ---
@pytest.mark.parametrize(
    "func,expected", [
        (hello, "hello, world"),
        (goodbye, "goodbye, world"),
    ]
)
def test_default(func, expected):
    assert func() == expected

# --- Tests for hello(), goodbye() with names ---
@pytest.mark.parametrize(
    "func,arg,expected", [
        (hello, "Alice", "hello, Alice"),
        (goodbye, "Bob", "goodbye, Bob")
    ]
)
def test_with_names(func, arg, expected):
    assert func(arg) == expected