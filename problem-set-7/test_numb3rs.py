import pytest
from numb3rs import validate

@pytest.mark.parametrize("address", [
    "0.0.0.0",
    "255.255.255.255",
    "1.2.3.4",
    "0.1.12.123",
])
def test_validate_valid_addresses(address):
    assert validate(address) is True

@pytest.mark.parametrize("address", [
    "foo",
    "....",
    "a.a.a.a",
    "256.256.256.256",
    "01.02.03.04",
    "1.",
    "1.2.",
    "1.2.3",
    "1.2.3.4.5",
    "0.0.0.256"
])
def test_validate_invalid_addresses(address):
    assert validate(address) is False