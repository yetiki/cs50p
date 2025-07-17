"""This script is takes user input and converts it to
lowercase before printing it."""

def main() -> None:
    user_input: str = input("Please enter a string: ")
    result: str = user_input.lower()
    print(result)

if __name__ == "__main__":
    main()
