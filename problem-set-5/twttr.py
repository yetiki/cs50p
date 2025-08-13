"""This program reimplements 'Setting up my twttr' from 'Problem Set 2',
restructured with a function shorten() - which expects a str as input and
returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.

In a correponding file called test_twttr.py, a number of functions have been
implemented that collectively test the implementation of shorten()
thoroughly, to test this program with:

pytest test_twttr.py"""

VOWELS: list[str] = ("A", "E", "I", "O", "U")

def main() -> None:
    # Prompt the user for a text message
    user_input: str = input("Input: ")

    # Convert the user's text to a tweet
    tweet: str = shorten(user_input)

    # Output the user's message as a tweet
    print(f"Output: {tweet}")

def shorten(word: str) -> str:
    tweet: str = "".join([char
                          for char in word
                          if char.upper() not in VOWELS])
    return tweet

if __name__ == "__main__":
    main()