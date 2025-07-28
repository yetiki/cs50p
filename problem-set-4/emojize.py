"""Because emoji aren't quite as easy to type as text, at least on laptops
and desktops, some programs support “codes,” whereby you can type, for
instance, :thumbs_up:, which will be automatically converted to 👍. Some
programs additionally support aliases, whereby you can more succinctly type,
for instance, :thumbsup:, which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a
list of codes with aliases.

This program prompts the user for a str in English and then outputs the
“emojized” version of that str, converting any codes (or aliases) therein
to their corresponding emoji."""

from emoji import emojize

def main() -> None:
    # Prompt the user for a message
    message: str = input("Input: ")

    # Convert any codes (or aliases) therein to their corresponding emoji
    emojized_message: str = emojize(message, language='alias')

    # Output the converted message
    print(emojized_message)

if __name__ == "__main__":
    main()