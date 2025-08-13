"""This program reimplements 'Home Federal Savings Bank' from
'Problem Set 1', restructured with a function value(), wherein value expects
a str as input and returns an int, namely 0 if that str starts with “hello”,
20 if that str starts with an “h” (but not “hello”), or 100 otherwise,
treating the str case-insensitively. The program assumes that the string
passed to the value function will not contain any leading spaces.

In a correponding file called test_twttr.py, a number of functions have been
implemented that collectively test the implementation of value() thoroughly,
to test this program with:

pytest test_bank.py

"""

def main() -> None:
    greeting: str = input("Greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting: str) -> int:
    if not isinstance(greeting, str):
        raise TypeError(f"Unsupported type: {type(greeting)}. 'greeting' must be of type str")
   
    greeting: str = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()