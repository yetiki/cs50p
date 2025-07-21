"""In the United States, it's customary to leave a tip for your
server after dining in a restaurant, typically an amount equal to
15% or more of your meal's cost.
This program prompts the user for the cost of the meal (formatted
as $##.##, wherein each # is a decimal digit for the cost of the
meal), and percentage of the meal to tip (formatted as ##%,
wherein each # is a decimal digit for the percentage to tip)
and returns the tip as a float.

This program assumes that the user will input values in the expected
formats (formatted as $##.##, wherein each # is a decimal digit for
the cost of the meal, and formatted as ##%, wherein each # is a
decimal digit for the percentage to tip).
"""

def main() -> None:
    dollars: float = dollars_to_float(input("How much was the meal? "))
    percent: float = percent_to_float(input("What percentage would you like to tip? "))
    tip: float = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d: str) -> float:
    """Accepts a str as input (formatted as $##.##, wherein each # is a decimal digit),
    removes the leading $, and returns the amount as a float.
    For instance, given $50.00 as input, it should return 50.0.
    Args:
        d (str): The input dollars string to convert.
    Returns:
        float: The converted dollars float value."""
    return float(d.replace("$", ""))

def percent_to_float(p: str) -> float:
    """Accepts a str as input (formatted as ##%, wherein each # is a decimal digit),
    removes the trailing %, and returns the percentage as a float.
    For instance, given 15% as input, it should return 0.15.
    Args:
        p (str): The input percentage string to convert.
    Returns:
        float: The converted percentage float value."""
    return float(p.replace("%", "")) / 100.0

if __name__ == "__main__":
    main()