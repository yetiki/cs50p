import pytest
from jar import Jar

# test __str__ method
def test_str_empty_and_full():
    jar = Jar(capacity=12)
    assert str(jar) == ""

    jar.deposit(6)
    assert str(jar) == "🍪" * 6

def test_repr():
    jar = Jar(capacity=6)
    assert repr(jar) == "Jar(capacity=6, size=0)"

    jar.deposit(3)
    assert repr(jar) == "Jar(capacity=6, size=3)"

# test capacity property
@pytest.mark.parametrize("cap,should_raise", [
    (0, False),
    (24, False),
    ("foo", True),
    (0.5, True),
    (-1, True),
    (0, True),
])
def test_capacity_values(cap, should_raise):
    if should_raise:
        with pytest.raises(ValueError):
            Jar(capacity=cap)
    else:
        assert Jar(capacity=cap).capacity == cap

# test size property
def test_size_property():
    jar = Jar(capacity=10)
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2

# test deposit method
def test_deposit_maximum():
    jar = Jar(capacity=12)
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(12)
    assert jar.size == 12

def test_deposit_incremental():
    jar = Jar(capacity=12)
    jar.deposit(6)
    with pytest.raises(ValueError):
        jar.deposit(7)
    jar.deposit(6)
    assert jar.size == 12

@pytest.mark.parametrize("n,should_raise", [
    (0, False),
    (-1, True),
    ("foo", True),
    (0.5, True),
])
def test_deposit_types(n, should_raise):
    jar = Jar(capacity=12)
    if should_raise:
        with pytest.raises(ValueError):
            jar.deposit(n)
    else:
        jar.deposit(n)
        assert jar.size == n

# test withdraw method
def test_withdraw_maximum():
    jar = Jar(capacity=12)
    jar.deposit(6)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    with pytest.raises(ValueError):
        jar.withdraw(7)
    jar.withdraw(6)
    assert jar.size == 0

@pytest.mark.parametrize("n,should_raise", [
    (0, False),
    (-1, True),
    ("foo", True),
    (0.5, True),
])
def test_withdraw_types(n, should_raise):
    jar = Jar(capacity=12)
    jar.deposit(6)
    if should_raise:
        with pytest.raises(ValueError):
            jar.withdraw(n)
    else:
        jar.withdraw(n)
        assert jar.size == 6 - n



