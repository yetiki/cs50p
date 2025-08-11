"""One of David's first toys as a child, funny enough, was Little Professor,
a “calculator” that would generate ten different math problems for David to
solve. For instance, if the toy were to display '4 + 0 = ', David would
(hopefully) answer with '4'. If the toy were to display '4 + 1 = ', David
would (hopefully) answer with '5'. If David were to answer incorrectly, the
toy would display 'EEE'. And after three incorrect answers for the same
problem, the toy would simply display the correct answer (e.g., '4 + 0 = 4'
or '4 + 1 = 5').

This program:
- Prompts the user for a level, n. If the user does not input '1', '2', or
'3', the program prompts again.
- Randomly generates ten math problems formatted as 'X + Y = ', wherein
each of 'X' and 'Y' is a non-negative integer with n digits.
Note: The order in which x and y are generated matters. The program generates
random numbers in x, y pairs to simulate generating one math question at a
time (e.g., x0 with y0, x1 with y1, and so on).

- Prompts the user to solve each of those problems. If an answer is not
correct (or not even a number), the program outputs 'EEE' and prompts the
user again, allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program
outputs the correct answer.
- The program ultimately outputs the user's score: the number of correct
answers out of 10."""

from random import randint

N_PROBLEMS: int = 10
MAX_ATTEMPTS: int = 3
OPERAND: str = "+"

def main() -> None:
    # Prompt the user for a level
    level: int = get_level()
    score: int = 0

    for _ in range(N_PROBLEMS):
        # Generate a maths problem
        x: int
        y: int
        solution: int
        x, y, solution = generate_problem(level, OPERAND)

        for attempt in range(MAX_ATTEMPTS):
            # Prompt the user for an answer
            user_answer: int | None = get_answer(x, y, OPERAND)

            # Check if the user answered the problem correctly
            if user_answer == solution:
                score += 1
                break
            else:
                print("EEE")

            # Check if the user has exceeded the maximum number of attempts
            if attempt == MAX_ATTEMPTS - 1:
                print(f"{x} {OPERAND} {y} = {solution}")

    # Output the user's score
    print('Score: ', score)

def get_level(min_level: int = 1, max_level: int = 3):
    while True:
        try:
            level: int = int(input("Level: ").strip())
        except ValueError:
            continue
        if min_level <= level <= max_level:
            return level

def generate_problem(level: int, operand: str) -> tuple[int, int]:
    x: int = generate_integer(level)
    y: int = generate_integer(level)
    solution: float = apply_operation(x, y, operand)
    return x, y, solution

def generate_integer(level: int) -> int:
    if level < 1:
        raise ValueError(f"Unsupported level: {level}. Level must be at least 1.")
    if level == 1:
        lower_bound: int = 0
    else:
        lower_bound: int = 10 ** (level - 1)
    upper_bound: int = (10 ** level) - 1
    return randint(lower_bound, upper_bound)

def apply_operation(x: int, y: int, operand: str) -> float:
    match operand:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            if y == 0:
                raise ZeroDivisionError(f"Unsupported denominator: {y}. Division by zero is not allowed.")
            return x / y
        case _:
            raise ValueError(f"Unsupported operand: {operand}. Supported operands: +, -, *, /")

def get_answer(x: int, y: int, operand: str) -> int | None:
    try:
        answer: int = int(input(f"{x} {operand} {y} = ").strip())
        return answer
    except ValueError:
        return None

if __name__ == "__main__":
    main()
