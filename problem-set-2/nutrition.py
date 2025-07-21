"""The U.S. Food & Drug Adminstration (FDA) offers
downloadable/printable posters that “show nutrition
information for the 20 most frequently consumed raw fruits
in the United States. Retail stores are welcome to
download the posters, print, display and/or distribute them
to consumers in close proximity to the relevant foods in
the stores.”

This program prompts consumers users to input a fruit
(case-insensitively) and then outputs the number of calories
in one portion of that fruit, per the FDA's poster for
fruits, which is also available as text. Capitalization
aside, assume that users will input fruits exactly as
written in the poster (e.g., strawberries, not strawberry).
The program ignores any input that isn't a fruit."""

def main() -> None:
    # Prompt the user for an item
    user_input: str = input("Item: ")
    item: str = user_input.lower()

    # Output the number of calories per portion of fruit
    fruit: dict[str: int] = {"apple": 130,
                             "avocado": 50,
                             "banana": 110,
                             "cantaloupe": 50,
                             "grapefruit": 60,
                             "grapes": 90,
                             "honeydew melon": 50,
                             "kiwifruit": 90,
                             "lemon": 15,
                             "lime": 20,
                             "nectarine": 60,
                             "orange": 80,
                             "peach": 60,
                             "pear": 100,
                             "pineapple": 50,
                             "plums": 70,
                             "strawberries": 50,
                             "sweet cherries": 100,
                             "tangerine": 50,
                             "watermelon": 80}

    if item in fruit.keys():
        calories: int = fruit.get(item, None)
        print(f"Calories: {calories}")

if __name__ == "__main__":
    main()