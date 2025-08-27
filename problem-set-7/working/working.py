"""Whereas most countries use a 24-hour clock, the United States tends to use
a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans
would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM”
is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post
meridiem”, wherein “meridiem” means midday (i.e., noon).

This program implements a function called convert() that expects a str in any
of the 12-hour formats below and returns the corresponding str in 24-hour
format (i.e., 09:00 to 17:00). The program expects that AM and PM will be
capitalized (with no periods therein) and that there will be a space before
each. The program also assumes that these times are representative of actual
times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM

A ValueError is raised if the input to convert is not in either of those
formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). The
program does not assume that someone's hours will start ante meridiem and end
post meridiem; someone might work late and even long hours (e.g., 5:00 PM to
9:00 AM).

In a correponding file called test_working.py, a number of functions have
been implemented that collectively test the implementation of convert()
thoroughly."""

import re

work_hours_pattern: str = r"^(?P<start_hours>\d{1,2})(:(?P<start_minutes>\d{2}))? (?P<start_meridiem>AM|PM) to (?P<end_hours>\d{1,2})(:(?P<end_minutes>\d{2}))? (?P<end_meridiem>AM|PM)$"

def main() -> None:
    print(convert(input("Hours: ")))

def convert(work_hours: str) -> str:
    if matches := re.search(work_hours_pattern, work_hours):
        # Extract start and end times from work_hours
        start_hours: int = int(matches.group('start_hours'))
        start_meridiem: str = matches.group('start_meridiem')

        if matches.group('start_minutes') is None:
            start_minutes: int = 0
        else:
            start_minutes: int = int(matches.group('start_minutes'))

        end_hours: int = int(matches.group('end_hours'))
        end_meridiem: str = matches.group('end_meridiem')

        if matches.group('end_minutes') is None:
            end_minutes: int = 0
        else:
            end_minutes: int = int(matches.group('end_minutes'))

        # Validate start and end times
        validate_time(start_hours, start_minutes, format="12-hour")
        validate_time(end_hours, end_minutes, format="12-hour")

        # Convert start time to 24-hour format
        start_time: str = convert_to_24_hour(start_hours, start_minutes, start_meridiem)
        end_time: str = convert_to_24_hour(end_hours, end_minutes, end_meridiem)

        # Return work_hours in 24-hour format
        return f"{start_time} to {end_time}"
    else:
        raise ValueError(f"Unsupported 'work_hours' format: '{work_hours}'. 'work_hours' must be of the form:\n'9:00 AM to 5:00 PM',\n'9 AM to 5 PM',\n'9:00 AM to 5 PM', or\n'9 AM to 5:00 PM'.")

def validate_time(hours: int, minutes: int, format="12-hour"):
    if format == "12-hour":
        min_hours: int = 1
        max_hours: int = 12
    elif format == "24-hour":
        min_hours: int = 0
        max_hours: int = 23
    else:
        raise ValueError(f"Unsupported 'format' value '{format}. 'format' must be either '12-hour', or '24-hour'.")

    if not (min_hours <= hours <= max_hours):
        raise ValueError(f"Unsupported 'hours' value '{hours}'. 'hours' must be between {min_hours} and {max_hours}, for format='{format}'.")
    if not (0 <= minutes <= 59):
        raise ValueError(f"Unsupported 'minutes' value '{minutes}'. 'minutes' must be between 0 and 59.")

def convert_to_24_hour(hours: int, minutes: int, meridiem: str) -> str:
    match meridiem.upper():
        case ("AM"):
            hours: int = hours % 12
        case ("PM"):
            if hours != 12:
                hours: int = hours + 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()