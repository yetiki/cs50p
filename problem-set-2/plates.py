"""In Massachusetts, home to Harvard University, it's
possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of
random ones. Among the requirements, though, are:

1. “All vanity plates must start with at least two letters.”

2. “All vanity plates may contain a maximum of 6 characters
(letters or numbers) and a minimum of 2 characters.”

3. “Numbers cannot be used in the middle of a plate; they
must come at the end. For example, AAA222 would be an
acceptable vanity plate; AAA22A would not be acceptable. The
first number used cannot be a '0'.”

4. “No periods, spaces, or punctuation marks are allowed.”

This program prompts the user for a vanity plate and then
outputs Valid if meets all of the requirements or Invalid
if it does not. The program assumes that any letters in
the user's input will be uppercase."""

def main():
    # Prompt the user for vanity plate
    plate: str = input("Plate: ")

    # Ouput Valid if meets all of the requirements
    # or Invalid if it does not
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if not satisfies_first_condition(s):
        # Condition 1: Must start with at least two letters
        return False
    if not satisfies_second_condition(s):
        # Condition 2: Length must be between 2 and 6 characters
        return False
    if not satisfies_third_condition(s):
        # Condition 3: Numbers must come at the end and cannot start with "0"
        return False
    if not satisfies_fourth_condition(s):
        # Condition 4: No periods, spaces, or punctuation marks are allowed
        return False
      
    return True

def satisfies_first_condition(s: str) -> bool:
    return s[:2].isalpha()

def satisfies_second_condition(s: str) -> bool:
    return (2 <= len(s) <= 6)

def satisfies_third_condition(s: str) -> bool:
    return satisfies_condition_3a(s) and satisfies_condition_3b(s)

def satisfies_condition_3a(s: str) -> bool:
    # Condition 3a: All numbers must come at the end of the plate
    for char in s:
        if char.isdigit():
            return s[s.index(char):].isdigit()
    return True

def satisfies_condition_3b(s: str) -> bool:
    # Condition 3b: The first number used cannot be a "0"
    for char in s:
        if char.isdigit():
            return char != "0"
    return True

def satisfies_fourth_condition(s: str) -> bool:
    return s.isalnum()

if __name__ == "__main__":
    main()