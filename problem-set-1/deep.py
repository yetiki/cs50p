"""This program prompts the user for the answer to
the Great Question of Life, the Universe and
Everything, outputting Yes if the user inputs 42
or (case-insensitively) forty-two or forty two.
Otherwise outputs No.

The program should behave as expected, case- and
space-insensitively."""

def main() -> None:
    user_input: str = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    answer: str = user_input.strip().lower()

    if answer in {"42", "forty-two", "forty two"}:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
