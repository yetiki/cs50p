"""It's not uncommon, in English, at least, to say “um” when trying to, um,
think of a word. The more you do it, though, the more noticeable it tends to
be!

This program implements a function called count() that expects a line of
text, as a str, as input and returns, as an int, the number of times that
“um” appears in that text, case-insensitively, as a word unto itself, not as
a substring of some other word. For instance, given text like 'hello, um,
world', the function returns 1. Given text like 'yummy', though, the
function returns 0.

In a correponding file called test_um.py, a number of functions have
been implemented that collectively test the implementation of count().
"""

import re

def main() -> None:
    print(count(input("Text: ")))

def count(text: str) -> int:
    if matches := re.findall(r"\bum\b", text, flags=re.IGNORECASE):
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    main()