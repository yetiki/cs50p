"""This script prompts the user for mass as an integer
(in kilograms) and then outputs the equivalent number
of Joules as an integer.
This script assumes that the user will input an integer."""

def main() -> None:
    mass: int = int(input("Please enter a mass as an integer (in kilograms): "))
    SPEED_OF_LIGHT: int = 300000000

    energy: int = mass * SPEED_OF_LIGHT**2
    print(str(energy))

if __name__ == "__main__":
    main()