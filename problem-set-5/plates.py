"""This program reimplements 'Vanity Plates' from 'Problem Set 2',
restructuring using the function is_valid(), wherein is_valid() expects a str
as input and returns True if that str meets all requirements and False
if it does not.

In a correponding file called test_plates.py, a number of functions that
collectively test the implementation of is_valid thoroughly, to test this
program with:

pytest test_plates.py"""

def main() -> None:
    plate: str = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate: str) -> bool:
    if not isinstance(plate, str):
        raise TypeError(f"Unsupported type: {type(plate)}. 'plate' must be of type str")

    if not plate[:2].isalpha():
        # 1. Must start with at least two letters
        return False
    
    if not (2 <= len(plate) <= 6):
        # 2. Length must be between 2 and 6 characters
        return False
    
    if any(char.isdigit() for char in plate):
        if not plate[plate.index(next(filter(str.isdigit, plate))):].isdigit():
            # 3. Numbers must come at the end   
                return False
        if not next(filter(str.isdigit, plate)) != "0":
            # 3. Numbers cannot start with '0'
            return False
    
    if not plate.isalnum():
        # 4. No periods, spaces, or punctuation marks are allowed
        return False
    
    return True

if __name__ == "__main__":
    main()
