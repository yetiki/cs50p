"""Suppose that you're in the habit of making a list of items you need from
the grocery store.

This program prompts the user for items, one per line, until the user inputs
control-d (which is a common way of ending one's input to a program). Then
output the user's grocery list in all uppercase, sorted alphabetically by
item, prefixing each line with the number of times the user inputted that
item (with no need to pluralize the items). The user's input is treated 
case-insensitively."""

def main() -> None:
    groceries: dict[str, int] = {}

    while True:
        try:
            # Prompt the user for an item
            item: str = input().strip().upper()
        except EOFError:
            # Exit the input loop
            break
        else:
            # Add the item to groceries
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1

    # Output groceries
    for key, value in sorted(groceries.items()):
        print(value, key)

if __name__ == "__main__":
    main()