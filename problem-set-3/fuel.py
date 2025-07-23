"""Fuel gauges indicate, often with fractions, just how
much fuel is in a tank. For instance 1/4 indicates that
a tank is 25% full, 1/2 indicates that a tank is 50%
full, and 3/4 indicates that a tank is 75% full.

This program prompts the user for a fraction, formatted
as X/Y, wherein each of X and Y is a positive integer,
and then outputs, as a percentage rounded to the nearest
integer, how much fuel is in the tank. If, though, 1% or
less remains, the program outputs E instead to indicate
that the tank is essentially empty. And if 99% or more
remains, the program outputs F instead to indicate that
the tank is essentially full.

If, though, X or Y is not an integer, X is greater than
Y, or Y is 0, the program instead prompts the user
again. (It is not necessary for Y to be 4.) This
program catches any exceptions like ValueError or
ZeroDivisionError."""

def main() -> None:
    while True:
        # Prompt the user for a fraction (X/Y)
        fuel_fraction: str = input_fraction("Fraction: ")

        # Check the fraction is valid as a fuel gauge (i.e., X >= 0, Y > 0, X <= Y)
        if is_valid(fuel_fraction):
            break

    # Convert the fraction to a percentage
    fuel_percentage: float = fraction_to_percentage(fuel_fraction)

    # Round the percentage to the nearest integer
    rounded_fuel_percentage: int = round(fuel_percentage)

    # Output the appropriate message based on the percentage
    if rounded_fuel_percentage <= 1:
        print("E")
    elif rounded_fuel_percentage >= 99:
        print("F")
    else:
        print(f"{rounded_fuel_percentage}%")

def is_valid(fraction: str) -> bool:
    try:
        numerator: int
        denominator: int
        numerator, denominator = fractional_parts(fraction)
        if numerator < 0:
            raise ValueError("numerator must be positive")
        if denominator < 0:
            raise ValueError("denominator must be positive")
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        if numerator > denominator:
            raise ValueError("numerator must be less than or equal to denominator")
    except (ValueError, ZeroDivisionError):
        return False
    return True

def is_fraction(fraction: str) -> bool:
    try:
        _, _ = fractional_parts(fraction)
    except ValueError:
        return False
    return True

def input_fraction(prompt: str) -> str:
    while True:
        fraction: str = input(prompt).strip()

        if is_fraction(fraction):
            return fraction

def fractional_parts(fraction: str) -> tuple[int, int]:
    try:
        numerator: int
        denominator: int
        numerator, denominator = map(int, fraction.split("/"))
    except Exception:
        raise ValueError("Input must be two integers separated by '/'")
    return numerator, denominator

def fraction_to_percentage(fraction: str) -> float:
    decimal: float = fraction_to_decimal(fraction)
    percentage: float = decimal_to_percentage(decimal)
    return percentage

def fraction_to_decimal(fraction: str) -> float:
    numerator: int
    denominator: int
    numerator, denominator = fractional_parts(fraction)
    if denominator == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    return numerator / denominator

def decimal_to_percentage(decimal: float) -> float:
    return decimal * 100

if __name__ == "__main__":
    main()