"""One way to measure the complexity of a program is to count its number of
lines of code (LOC), excluding blank lines and comments. For instance, a
program like

# Say hello

name = input("What's your name? ")
print(f"hello, {name}")

has just two lines of code, not four, since its first line is a comment, and
its second line is blank (i.e., just whitespace). That's not that many, so
odds are the program isn't that complex. Of course, just because a program
(or even function) has more lines of code than another doesn't necessarily
mean it's more complex. For instance, a function like

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

isn't really twice as complex as a function like

def is_even(n):
    return n % 2 == 0

even though the former has (more than) twice as many lines of code. In fact,
the former might arguably be simpler if it's easier to read! So lines of code
should be taken with a grain of salt.

Even so, this program expects exactly one command-line argument, the name (or
path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines. If the user does not specify exactly one
command-line argument, or if the specified file's name does not end in .py,
or if the specified file does not exist, the program instead exits via
sys.exit.

This program assumes that any line that starts with #, optionally preceded by
whitespace, is a comment. (A docstring is not considered a comment.) The
programs also assumes that any line that only contains whitespace is blank.
"""

import sys

def is_comment(line: str) -> bool:
    return line.lstrip().startswith("#")

def is_empty(line: str) -> bool:
    return line.rstrip("\n").strip() == ""

def main() -> None:
    # Check exactly one command-line argument is parsed
    # (other than the current module)
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        filename: str = sys.argv[1]

    # Check the parsed file is a Python file
    _, extension = filename.rsplit(".", 1)

    if extension != "py":
        sys.exit("Not a Python file")

    try:
        # Read the contents of the Python file
        with open(filename) as file:
            # Count the number of lines in the python file
            # (excluding comments and blank lines)
            n_lines: int = len([line.rstrip()
                                for line in file
                                if not is_comment(line) and not is_empty(line)])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        # Output the number of lines of "code" in the Python file
        print(n_lines)

if __name__ == "__main__":
    main()