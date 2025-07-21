"""Python already supports math, whereby you can write code to
add, subtract, multiply, or divide values and even variables.
But let's write a program that enables users to do math, even
without knowing Python.

This program implements a program that prompts the user for an
arithmetic expression and then calculates and outputs the
result as a floating-point value formatted to one decimal place.

This program assumes that the user's input will be formatted as
x y z, with one space between x and y and one space between y
and z, wherein:
x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should
output 2.0. Assume that, if y is /, then z will not be 0.
"""

def main() -> None:
    user_input: str = input("Expression: ")
    expression: str = user_input.strip()

    x, y, z = expression.split(" ")
    x: int = int(x)
    z: int = int(z)

    match y:
        case "+":
            result: float = x + z
        case "-":
            result: float = x - z
        case "*":
            result: float = x * z
        case "/":
            result: float = x / z
        # case _:
        #     raise ValueError("Invalid operator")

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()

