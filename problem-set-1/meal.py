"""Suppose that you're in a country where it's customary to
eat breakfast between 7:00 and 8:00, lunch between 12:00 and
13:00, and dinner between 18:00 and 19:00. Wouldn't it be
nice if you had a program that could tell you what to eat when?

This program prompts the user for a time and outputs whether
it's breakfast time, lunch time, or dinner time. If it's not
time for a meal, the program doesn't output anything at all.

This program assumes that the user's input will be formatted in
24-hour time as #:## or ##:##. And assumes that each meal's
time range is inclusive. For instance, whether it's 7:00, 7:01,
7:59, or 8:00, or anytime in between, it's time for breakfast.

This program is structure using a convert function that converts
time, a str in 24-hour format, to the corresponding number of
hours as a float. For instance, given a time like "7:30"
(i.e., 7 hours and 30 minutes), convert should return 7.5
(i.e., 7.5 hours).

This program additionally supports 12-hour times, allowing the
user to input times in these formats too:
#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m."""

def main() -> None:
    # Prompt the user for a time in 24-hour or 12-hour format
    time: str = input("What time is it? ")

    # Convert the time to the corresponding number of hours
    hours: float = convert(time)

    # Output the meal time based on the number of hours
    print_meal_time(hours)

def print_meal_time(hours: float) -> None:
    meal_times: dict[tuple[float, float], str] = {(7.00, 8.00): "breakfast",
                                                  (12.00, 13.00): "lunch",
                                                  (18.00, 19.00): "dinner"}
    
    for (start, end), meal in meal_times.items():
        if start <= hours <= end:
            print(f"{meal} time")
            break

def convert(time: str) -> float:
    hours: int
    minutes: int

    if is_12_hour_format(time):
        hours, minutes = convert_12_hour(time)
    
    hours, minutes = convert_24_hour(time)
    return hours + minutes / 60

def is_12_hour_format(time: str) -> bool:
    return "a.m." in time or "p.m." in time

def convert_24_hour(time: str) -> tuple[int, int]:
    hours: int
    minutes: int
    hours, minutes = map(int, time.split(sep=":", maxsplit=1))
    return hours, minutes

def convert_12_hour(time: str) -> tuple[int, int]:
    hour_minute: str
    meridiem: str
    hour_minute, meridiem = time.split(sep=" ", maxsplit=1)

    hours: int
    minutes: int
    hours, minutes = convert_24_hour(hour_minute)

    if meridiem == "p.m.":
        hours += 12
    return hours, minutes

if __name__ == "__main__":
    main()
