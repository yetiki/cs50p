"""When creating a Google Form that prompts users for a short answer (or
paragraph), it's possible to enable response validation and require that the
user's input match a regular expression. For instance, you could require that
a user input an email address with a regex Or you could more easily use
Google's built-in support for validating an email address much like you
could use a library in your own code.

This program uses validator-collection/validators from PyPI, to prompt the
user for an email address via input and then prints Valid or Invalid,
respectively, if the input is a syntatically valid email address."""

from validator_collection.checkers import is_email

def main() -> None:
    email: str = input("What's your email address? ")

    if is_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
