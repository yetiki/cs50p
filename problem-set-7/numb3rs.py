"""In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on
screen, '275.3.6.28', which isn't actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker)
uses to communicate on the internet, akin to a postal address in the real
world, typically formatted in dot-decimal notation as #.#.#.#. But each #
should be a number between 0 and 255, inclusive. Suffice it to say 275 is
not in that range! If only NUMB3RS had validated the address in that scene!

This program implements a function called validate that expects an IPv4
address as input as a str and then returns True or False, respectively, if
that input is a valid IPv4 address or not.

In a correponding file called test_numb3rs.py, a number of functions have
been implemented that collectively test the implementation of validate()
thoroughly, to test this program with:

pytest test_numb3rs.py
"""

import re

ipv4_pattern: str = r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})"

def main() -> None:
    print(validate(input("IPv4 Address: ")))

def validate(address: str) -> bool:
    if matches := re.fullmatch(ipv4_pattern, address):
        for match in matches.groups():
            if match.startswith("0") and len(match) > 1:
                return False
            if not (0 <= int(match) <= 255):
                return False
        return True
    return False

if __name__ == "__main__":
    main()