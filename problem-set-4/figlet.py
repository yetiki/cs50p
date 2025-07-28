"""FIGlet, named after Frank, Ian, and Glen's letters, is a program from the
early 1990s for making large letters out of ordinary text, a form of ASCII
art. Among the fonts supported by FIGlet are those at
figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

This program:
- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which
      case the first of the two should be -f or --font, and the second of the
      two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or
--font or the second is not the name of a font, the program exits via
sys.exit with an error message.
"""

import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fonts: list[str] = figlet.getFonts()

def main() -> None:
    # Set ASCII font
    set_ascii_font()

    # Prompt the user for a message
    message: str = input("Input: ")

    if not message:
        sys.exit("Error: No message provided.")
    
    # Output the message as ASCII art of the desired font
    print(figlet.renderText(message))

def set_ascii_font() -> None:
    if len(sys.argv) == 1:
        font: str = choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        font: str = sys.argv[2]
        if font not in fonts:
            sys.exit(f"Error: Font '{font}' not found.\n"
                     "See available fonts at http://www.figlet.org/fontdb.cgi.")
    else:
        sys.exit(f"Invalid arguments '{' '.join(sys.argv[1:])}'\n"
                 "Usage:\n"
                 "\tpython figlet.py                # random font\n"
                 "\tpython figlet.py -f <font>      # specific font\n"
                 "\tpython figlet.py --font <font>  # specific font"
                 )

    figlet.setFont(font=font)

if __name__ == "__main__":
    main()