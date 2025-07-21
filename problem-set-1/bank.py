"""This program that prompts the user for a greeting.
If the greeting starts with “hello”, the program
outputs $0. If the greeting starts with an “h” (but
not “hello”), the program outputs $20. Otherwise,
the program outputs $100.

The program ignores any leading whitespace in the
user's greeting, and treats the user's greeting
case-insensitively."""

def main() -> None:
    user_input: str = input("Greeting: ")
    greeting: str = user_input.strip().lower()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()