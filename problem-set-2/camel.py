"""In some languages, it's common to use camel case (otherwise
known as “mixed case”) for variables' names when those names
comprise multiple words, whereby the first letter of the first
word is lowercase but the first letter of each subsequent word
is uppercase. For instance, whereas a variable for a user's
name might be called name, a variable for a user's first name
might be called firstName, and a variable for a user's
preferred first name (e.g., nickname) might be called
preferredFirstName.

Python, by contrast, recommends snake case, whereby words are
instead separated by underscores (_), with all letters in
lowercase. For instance, those same variables would be called
name, first_name, and preferred_first_name, respectively, in
Python.

This program prompts the user for the name of a variable in
camel case and outputs the corresponding name in snake case.
The program assumes that the user's input will indeed be in
camel case."""

def main() -> None:
    # Prompt the user for a name in camelCase
    camel_case_name: str = input("camelCase: ")

    # Get words from camelCase name
    words: list[str] = get_words(camel_case_name)
   
    # Convert the name from camelCase to snake_case
    snake_case_name: str = convert_to_snake_case(words)

    # Ouput the snake_case name
    print(snake_case_name)

def convert_to_snake_case(words: list[str]) -> str:
    return "_".join([word.lower() for word in words])

def get_words(camel_case_name: str) -> list[str]:
    words: list[str] = []
    word_start_index: int = 0

    for index, char in enumerate(camel_case_name):
        if char.isupper():
            words.append(camel_case_name[word_start_index: index])
            word_start_index = index
    
    words.append(camel_case_name[word_start_index:])
    return words

if __name__ == "__main__":
    main()

