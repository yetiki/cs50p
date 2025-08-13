"""This program reimplements 'Fuel Gauge' from 'Problem Set 3' using:

- convert() - which expects a str in 'X/Y' format as input, wherein each of
'X' and 'Y' is a positive integer, and returns that fraction as a percentage
rounded to the nearest int between 0 and 100, inclusive. If 'X' and/or 'Y'
is not an integer, or if 'X' is greater than 'Y', then convert() raises a
'ValueError'. If 'Y' is 0, then convert() raises a 'ZeroDivisionError'.

- gauge() - which expects an int and returns a str that is:
  - "E" if that int is less than or equal to 1,
  - "F" if that int is greater than or equal to 99,
  - and "Z%" otherwise, wherein Z is that same int.

In a correponding file called test_fuel.py, a number of functions that
collectively test the implementations of convert() and gauge() thoroughly
are implemented ."""

def main() -> None:
    while True:
        # Prompt the user for the fuel gauge as a fraction 'X/Y'
        print("Please enter a fuel gauge as a fraction.")
        fuel_fraction: str = input("Fraction: ").strip()
        try:
            # Convert the fraction to a percentage
            fuel_percentage: float = convert(fuel_fraction)
        except (ValueError, ZeroDivisionError):
            print("Please enter the fraction in the form: X/Y for integers X, and Y, where X >= 0, Y > 0, and X < Y.")
        else:
            break
    
    # Output an appropriate message based on the percentage
    print(gauge(fuel_percentage))

def convert(fraction: str) -> float:
    numerator: int
    denominator: int
    numerator, denominator = fractional_parts(fraction)

    if numerator < 0:
        raise ValueError(f"Unsupported value: {fraction=}, {numerator=}. 'numerator' must be positive.")
    if denominator < 0:
        raise ValueError(f"Unsupported value: {fraction=}, {denominator=}. 'denominator' must be positive.")
    if denominator == 0:
        raise ZeroDivisionError(f"Unsupported value: {fraction=}, {denominator=}. 'denominator' cannot be zero.")
    if numerator > denominator:
        raise ValueError(f"Unsupported values: {fraction=}, {numerator=}, {denominator=}. 'numerator' must be less than or equal to 'denominator'.")
    
    decimal: float = fraction_to_decimal(fraction)
    percentage: float = decimal_to_percentage(decimal)
    return round(percentage)

def fractional_parts(fraction: str) -> tuple[int, int]:
    try:
        numerator: int
        denominator: int
        numerator, denominator = map(int, fraction.split("/"))
    except (TypeError, AttributeError):
        raise TypeError(f"Unsupported type: {type(fraction)}. 'fraction' must be of type str.") 
    except ValueError:
        raise ValueError(f"Unsupported value: {fraction=}. 'fraction' must be of the form: 'X/Y' for integers X, and Y.")
    return numerator, denominator

def fraction_to_decimal(fraction: str) -> float:
    numerator: int
    denominator: int
    numerator, denominator = fractional_parts(fraction)
    if denominator == 0:
        raise ZeroDivisionError(f"Unsupported value: {denominator=}. 'denominator' cannot be zero.")
    return numerator / denominator

def decimal_to_percentage(decimal: float) -> float:
    return decimal * 100

def gauge(fuel_percentage: int) -> str:
    if not isinstance(fuel_percentage, int):
        raise TypeError(f"Unsupported type: {type(fuel_percentage)}. 'fuel_percentage' must be of type int.")

    if fuel_percentage < 0:
        raise ValueError(f"Unsupported value: {fuel_percentage=}. 'fuel_percentage' must be >= 0.")
    if fuel_percentage > 100:
        raise ValueError(f"Unsupported value: {fuel_percentage=}. 'fuel_percentage' must be <= 100.")

    if fuel_percentage <= 1:
        return "E"
    elif fuel_percentage >= 99:
        return "F"
    else:
        return f"{fuel_percentage}%"

if __name__ == "__main__":
    main()