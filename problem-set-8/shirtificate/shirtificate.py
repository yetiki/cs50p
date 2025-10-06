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

def main() -> None:
    # prompt the user for their name
    name: str = input("Name: ").strip()

    if name == "":
        name: str = "I"

    # construct a portrait A4 PDF 
    pdf: FPDF = FPDF(orientation="P", unit="mm", format="A4")

    # add a page to the PDF
    pdf.add_page()

    # set title font style
    pdf.set_font("helvetica", size=48)

    # add title centred horizontally
    pdf.set_y(28.5) # adjust y position to be 28.5 mm from top
    pdf.cell(w=0, h=20, text="CS50 Shirtificate", align=Align.C)

    # add shirt image centered horizontally
    pdf.image("shirtificate.png", x=Align.C, y=70, w=190, keep_aspect_ratio=True)

    # set name font style
    pdf.set_font("helvetica", size=24)

    # add name on top of shirt in white text
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(126)  # adjust y position to be on top of the shirt
    pdf.cell(w=0, h=20, text=f"{name} took CS50", align=Align.C)

    # output the PDF to a file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()