from datetime import date
from seasons import InvalidDateError, parse_date, compute_age, minutes_to_words
from pytest import raises

def test_parse_date_edge_cases() -> None:
    # test first date
    assert parse_date("0001-01-01") == date(1, 1, 1)

    # test last date
    assert parse_date("9999-12-31") == date(9999, 12, 31)

    # test valid leap year
    assert parse_date("2020-02-29") == date(2020, 2, 29)

    # test invalid leap year
    with raises(InvalidDateError):
        parse_date("2021-02-29")

def test_parse_date_error() -> None:
    # test non-numeric
    with raises(InvalidDateError):
        parse_date("abcd-ef-gh")

    # test invalid format
    with raises(InvalidDateError):
        parse_date("2020/01/01")

    with raises(InvalidDateError):
        parse_date("01-01-2020")

    with raises(InvalidDateError):
        parse_date("20200101")

    with raises(InvalidDateError):
        parse_date("January 1, 2020")

    # test invalid year
    with raises(InvalidDateError):
        parse_date("10000-01-01")
    with raises(InvalidDateError):
        parse_date("0000-01-01")

    # test invalid month
    with raises(InvalidDateError):
        parse_date("2020-13-01")

    with raises(InvalidDateError):
        parse_date("2020-00-01")

    # test invalid day
    with raises(InvalidDateError):
        parse_date("2020-02-31")
    with raises(InvalidDateError):
        parse_date("2020-02-30")

def test_compute_age_units() -> None:
    # test seconds
    assert compute_age(date(2025, 1, 1), date(2025, 1, 2), unit="seconds") == 86400

    # test minutes
    assert compute_age(date(2025, 1, 1), date(2025, 1, 2), unit="minutes") == 1440

    # test hours
    assert compute_age(date(2025, 1, 1), date(2025, 1, 2), unit="hours") == 24

    # test invalid units
    with raises(ValueError):
        compute_age(date(2025, 1, 1), date(2025, 1, 2), unit="days")

def test_compute_age_edge_cases() -> None:
    # test minimum age in minutes
    assert compute_age(date(2025, 1, 1), date(2025, 1, 1), unit="minutes") == 0

    # test maximum age in minutes
    assert compute_age(date(1, 1, 1), date(9999, 12, 31), unit="minutes") == 5258963520

    # test one year ago from today in minutes
    assert compute_age(date(2024, 9, 1), date(2025, 9, 1), unit="minutes") == 525600

    # test two years ago from today in minutes
    assert compute_age(date(2023, 9, 1), date(2025, 9, 1), unit="minutes") == 1052640

def test_minutes_to_words() -> None:
    # test zero minutes
    assert minutes_to_words(0) == "Zero minutes"

    # test singular minute
    assert minutes_to_words(1) == "One minute"

    # test plural
    assert minutes_to_words(2) == "Two minutes"

    # test hour
    assert minutes_to_words(60) == "Sixty minutes"

    # test day
    assert minutes_to_words(1140) == "One thousand, one hundred and forty minutes"

    # test week
    assert minutes_to_words(10080) == "Ten thousand and eighty minutes"

    # test month
    assert minutes_to_words(43200) == "Forty-three thousand, two hundred minutes"

    # test year
    assert minutes_to_words(525600) == "Five hundred and twenty-five thousand, six hundred minutes"

    # test decade
    assert minutes_to_words(5256000) == "Five million, two hundred and fifty-six thousand minutes"

    # test century
    assert minutes_to_words(52560000) == "Fifty-two million, five hundred and sixty thousand minutes"
