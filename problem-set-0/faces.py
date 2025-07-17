"""This script implements a function called convert
that accepts a str as input and returns that same
input with any ':)' converted to '🙂' (otherwise
known as a slightly smiling face) and any ':('
converted to '🙁' (otherwise known as a slightly
frowning face). All other text should be returned
unchanged.

This script also implements a function called main
that prompts the user for input, calls convert on
that input, and prints the result."""

def convert(text: str) -> str:
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main() -> None:
    user_input: str = input("Please enter a string: ")
    result: str = convert(user_input)
    print(result)

if __name__ == "__main__":
    main()