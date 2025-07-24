"""In the United States, dates are typically formatted in month-day-year
order (MM/DD/YYYY), otherwise known as middle-endian order, which is
arguably bad design. Dates in that format can't be easily sorted because the
date's year comes last instead of first. Try sorting, for instance,
2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a
spreadsheet). Dates in that format are also ambiguous. Harvard was founded
on September 8, 1636, but 9/8/1636 could also be interpreted as August 9,
1636!

Fortunately, computers tend to use ISO 8601, an international standard that
prescribes that dates should be formatted in year-month-day (YYYY-MM-DD)
order, no matter the country, formatting years with four digits, months with
two digits, and days with two digits, “padding” each with leading zeroes as
needed.

This program prompts the user for a date, anno Domini, in month-day-year
order, formatted like 9/8/1636 or September 8, 1636. The program then
outputs that same date in YYYY-MM-DD format. If the user's input is not a
valid date in either format, the user is prompted again. The program
validates whether a month has 28, 29, 30, or 31 days."""

months: list[str] = ["January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"]

def main() -> None:
    # Prompt the user for a date in numeric: "MM/DD/YYYY", or alphanumeric: "month DD, YYYY" format
    date: str = input_date("Date: ")

    # Split the date into year, month, and day parts
    year: int
    month: int
    day: int
    year, month, day = date_parts(date)

    # Convert the date to ISO 8601 numeric: "YYYY-MM-DD" format
    date_iso: str = convert_to_iso(year, month, day)

    # Output the date in ISO 8601 numeric: "YYYY-MM-DD" format
    print(date_iso)

def input_date(prompt: str) -> str:
    while True:
        date: str = input(prompt).strip()
        if is_valid_date(date):
            return date
        
def is_valid_date(date: str) -> bool:
    try:
        year: int
        month: int
        day: int
        year, month, day = date_parts(date)

    except ValueError:
        return False
    else:
        # Check if the year, month, and day are valid integers
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        
        if is_leap_year(year):
            if month == 2 and day > 29:
                return False
        elif month == 2 and day > 28:
            return False     
        
        return True

def date_parts(date: str) -> tuple[int, int, int]:
    if '/' in date:
        try:
            # Convert date from MM/DD/YYYY format
            month, day, year = map(int, date.split('/', maxsplit=2))
        except Exception:
            raise ValueError("Invalid date format. Must be 'MM/DD/YYYY' or 'Month DD, YYYY'.")
        return year, month, day
    else:
        try:
            # Convert date from "month DD, YYYY" format
            month_name, rest = date.split(' ', maxsplit=1)
            month_name = month_name.title()

            if month_name not in months:
                raise ValueError(f"Invalid month: '{month_name}'.")
            
            # Split rest on comma to get day and year
            day_str, year_str = rest.split(',', maxsplit=1)
            day = int(day_str.strip())
            year = int(year_str.strip())
            month = months.index(month_name) + 1
        except Exception:
            raise ValueError("Invalid date format. Must be 'MM/DD/YYYY' or 'Month DD, YYYY'.")
        return year, month, day

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def convert_to_iso(year: int, month: int, day: int) -> str:
    return f"{year:04}-{month:02}-{day:02}"

if __name__ == "__main__":
    main()