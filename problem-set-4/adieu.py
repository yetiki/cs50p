"""In The Sound of Music, there's a song sung largely in English, So Long,
Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:
Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn't grammatically correct, since it would typically be
written (with an Oxford comma) as:
Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn't even a word; it just rhymes with “you”!

This program prompts the user for names, one per line, until the user inputs
control-d. Assuming that the user will input at least one name, the program 
then bids adieu to those names, separating two names with one 'and', three
names with two ',' and one 'and', and 'n' names with 'n-1' ',' and one 'and',
as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl"""

import inflect
import sys

def main() -> None:
    # Prompt the user for names
    names: list[str] = input_str_list("Name: ")

    if not names:
        sys.exit("No names entered.")

    # Bid adieu to the provided names
    bid_adieu(names)

def input_str_list(prompt: str) -> list[str]:
    user_inputs: list[str] = []
    while True:
        try:
            user_input: str = input(prompt).strip()
        except EOFError:
            return user_inputs
        else:
            if user_input:
                user_inputs.append(user_input)

def bid_adieu(names: list[str]) -> None:
    engine = inflect.engine()
    print("Adieu, adieu, to " + engine.join(names))

if __name__ == "__main__":
    main()