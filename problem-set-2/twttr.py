"""When texting or tweeting, it's not uncommon to shorten
words to save time or space, as by omitting vowels, much
like Twitter was originally called twttr.

This program prompts the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O,
and U) omitted, whether inputted in uppercase or
lowercase."""

def main() -> None:
    # Prompt the user for text
    user_input: str = input("Input: ")

    # Convert user text to tweet
    tweet: str = convert_to_tweet(user_input)

    # Output tweet
    print(f"Output: {tweet}")

def convert_to_tweet(message: str) -> str:
    vowels: list[str] = ("A", "E", "I", "O", "U")
    tweet: str = "".join([char for char in message if char.upper() not in vowels])
    return tweet

if __name__ == "__main__":
    main()
