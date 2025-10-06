"""Five hundred twenty-five thousand, six hundred minutes
Five hundred twenty-five thousand moments so dear
Five hundred twenty-five thousand, six hundred minutes
How do you measure, measure a year?
- 'Seasons of Love,' Rent

Assuming there are 365 days in a year, there are 365 x24 x60 =525,600 minutes in
that same year (because there are 24 hours in a day and 60 minutes in an hour). But
how many minutes are there in two or more years? Well, it depends on how many of
those are leap years with 366 days, per the Gregorian calendar, as some of them
could have 1 x24 x60 =1,440 additional minutes. In fact, how many minutes has it
been since you were born? Well, that, too, depends on how many leap years there
have been since! There is an algorithm for such, but let's not reinvent that wheel.
Let's use a library instead. Fortunately, Python comes with a datetime module that
has a class called date that can help, per
docs.python.org/3/library/datetime.html#date-objects.

This program prompts the user for their date of birth in YYYY-MM-DD format and then
prints how old they are in minutes, rounded to the nearest integer, using English
words instead of numerals, just like the song from Rent, without any and between
words. Since a user might not know the time at which they were born, the program
assumes, for simplicity, that the user was born at midnight (i.e., 00:00:00) on
that date. And assumes that the current time is also midnight. In other words, even
if the user runs the program at noon, the program assumes that it's actually
midnight, on the same date.

The program exits via sys.exit if the user does not input a date in YYYY-MM-DD
format.

All implemented functions are tested in a corresponding file called test_seasons.py, 
"""

from sys import exit
import datetime
import re
from inflect import engine

date_pattern: str = r"^(?P<year>\d{1,4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$"

class InvalidDateError(Exception):
    pass

def main() -> None:
    try:
        date_of_birth = parse_date(input("Date of Birth: "))
    except InvalidDateError:
        exit("Invalid date")

    age_minutes = compute_age(date_of_birth, datetime.date.today(), unit="minutes")
    print(minutes_to_words(age_minutes))

def parse_date(date: str) -> datetime.date:
    if match := re.fullmatch(date_pattern, date):
        year = int(match.group("year"))
        month = int(match.group("month"))
        day = int(match.group("day"))
    else:
        raise InvalidDateError(f"Invalid 'date': {date}. 'date' must be of the form: YYYY-MM-DD")
    
    try:
        return datetime.date(year, month, day)
    except ValueError as e:
        raise InvalidDateError(f"Invalid 'date': {date}. {str(e)}")

def compute_age(date_of_birth: datetime.date, current_date: datetime.date, unit="seconds") -> int:
    age_seconds = (current_date - date_of_birth).total_seconds()
    if unit == "seconds":
        return int(age_seconds)
    elif unit == "minutes":
        return int(age_seconds // 60)
    elif unit == "hours":
        return int(age_seconds // 3600)
    else:
        raise ValueError(f"Unsupported 'unit': {unit}, 'unit' must be either: 'hours', 'minutes', or 'seconds'")

def minutes_to_words(minutes: int) -> str:
    inflect_engine = engine()
    words = inflect_engine.number_to_words(minutes).capitalize()
    minute_word = inflect_engine.plural_noun('minute', minutes)
    return f"{words} {minute_word}"

if __name__ == "__main__":
    main()