"""
Suppose that you'd like to implement a CS50 “shirtificate,” a PDF with an
image of an 'I took CS50' t-shirt, shirtificate.png, customized with a
user's own name.

This program prompts the user for their name and outputs, using fpdf2, a
CS50 shirtificate in a file called shirtificate.pdf with these
specifications:

- The orientation of the PDF should be Portrait.
- The format of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as text, centered
   horizontally.
- The shirt's image should be centered horizontally.
- The user's name should be on top of the shirt, in white text.
"""
from fpdf import FPDF, Align

class Shirtificate(FPDF):
    def __init__(self, name: str="I"):
        self.name: str = name
        super().__init__(orientation="portrait", unit="mm", format="A4", font_cache_dir="DEPRECATED")
        self._draw_page()

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name: str = name.strip()

        if hasattr(self, "pages"): # if name is updated
            # clear previous pages
            super().__init__(orientation="portrait", unit="mm", format="A4")

            # draw a fresh page using the updated name
            self._draw_page()
    
    def _draw_page(self) -> None:
        super().add_page()
        
        # set title font style
        self.set_font("helvetica", size=48)

        # add title centred horizontally
        self.set_y(28.5) # adjust y position to be 28.5 mm from top
        self.cell(w=0, h=20, text="CS50 Shirtificate", align=Align.C)

        # add shirt image centered horizontally
        self.image("shirtificate.png", x=Align.C, y=70, w=190, keep_aspect_ratio=True)

        # set t-shirt text font style
        self.set_font("helvetica", size=24)

        # add t-shirt text on top of t-shirt in white text
        self.set_text_color(255, 255, 255)
        self.set_y(126)  # adjust y position to be on top of the shirt
        self.cell(w=0, h=20, text=f"{self.name} took CS50", align=Align.C)

def main() -> None:
    # prompt user for their name
    name: str = input("Name: ").strip()

    # construct shirtificate pdf
    shirtificate: Shirtificate = Shirtificate(name=name)

    # save shirtificate pdf
    shirtificate.output("shirtificate.pdf")

if __name__ == "__main__":
    main()