"""This script takes user input and replaces each space
with '...' before printing it."""

def main() -> None:
    user_input: str = input("Please enter a string: ")
    result: str = user_input.replace(" ", "...")
    print(result)

if __name__ == "__main__":
    main()