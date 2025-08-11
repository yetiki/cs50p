"""I'm thinking of a number between 1 and 100…

What is it?
It's 50! But what if it were more random?

This program:
- Prompts the user for a level, n. If the user does not input a
positive integer, the program prompts again.
- Randomly generates an integer between 1 and n, inclusive.
- Prompts the user to guess that integer. If the guess is not a positive
integer, the program prompts the user again.
- If the guess is smaller than that integer, the program outputs 'Too
small!' and prompts the user again.
- If the guess is larger than that integer, the program outputs 'Too large!'
and prompts the user again.
- If the guess is the same as that integer, the program outputs 'Just right!'
and exits."""

from random import randint
from sys import exit

def main() -> None:
    # Prompt the user for a positive integer
    level: int = input_positive_integer("Level: ")

    # Randomly generate a target integer according to the level
    target: int = randint(1, level)

    while True:
        # Prompt the user to guess the target integer
        guess: int = input_positive_integer("Guess: ")

        # Check the guess against the target
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            exit()

def input_positive_integer(prompt: str) -> int:
    while True:
        try:
            integer: int = int(input(prompt).strip())
        except ValueError:
            pass
        else:
            if integer > 0:
                return integer

if __name__ == "__main__":
    main()