"""Suppose that a machine sells bottles of Coca-Cola (Coke) for
50 cents and only accepts coins in these denominations: 25 cents,
10 cents, and 5 cents.

This program prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has
inputted at least 50 cents, the program outputs how many cents in
change the user is owed. The program assumes that the user will
only input integers, and ignore any integer that isn't an accepted
denomination."""

def main() -> None:
    amount_due: int = 50
    accepted_coin_amounts: tuple[int, int, int] = (5, 10, 25)

    while amount_due > 0:
        # Output the amount due
        print(f"Amount Due: {amount_due}")

        # Prompt the user to insert a coin
        coin_amount: int = int(input("Insert Coin: "))

        if coin_amount in accepted_coin_amounts:
            amount_due -= coin_amount

    # Compute the change owed to the user
    change_owed: int = abs(amount_due)

    # Output the change owed to the user
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
