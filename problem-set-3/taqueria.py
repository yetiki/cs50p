"""One of the most popular places to eat in Harvard Square is Felipe's
Taqueria, which offers a menu of entrees.

This program enables a user to place an order, prompting them for items, one
per line, until the user inputs control-d (which is a common way of ending
one's input to a program). After each inputted item, the program displays 
the total cost of all items inputted thus far, prefixed with a dollar sign
($) and formatted to two decimal places. The user's input are treated case
insensitively, and any input that isn't an item is ignored. The program
assume that every item on the menu will be titlecased."""

entrees: dict[str, float] = {"Baja Taco": 4.25,
                             "Burrito": 7.50,
                             "Bowl": 8.50,
                             "Nachos": 11.00,
                             "Quesadilla": 8.50,
                             "Super Burrito": 8.50,
                             "Super Quesadilla": 9.50,
                             "Taco": 3.00,
                             "Tortilla Salad": 8.00}

def main() -> None:
    total_cost: float = 0.00
    while True:
        try:
            # Prompt the user to place an order
            item: str = input("Item: ").strip().title()

            # Do not display the total running cost if the item is not in entrees
            if item not in entrees:
                continue
        except EOFError:
            # Exit the program
            break
        else:
            # Compute the total running cost of the order
            total_cost += entrees.get(item, 0.00)

            # Output the total running cost of the order
            print(f"Total: ${total_cost:.2f}")

if __name__ == "__main__":
    main()