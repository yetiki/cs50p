"""After finishing CS50 itself, students on campus at Harvard traditionally
receive their very own I took CS50 t-shirt. No need to buy one online, but
like to try one on virtually?

This program expects exactly two command-line arguments:
- in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as
  input
- in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save)
  as output

The program overlays shirt.png (which has a transparent background) on the
input after resizing and cropping the input to be the same size, saving the
result as its output.

This program:
- opens the input with Image.open,(per
  pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open),
- resizes and crops the input (with ImageOps.fit per
  pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit),
- overlays the shirt (with Image.paste using default values for method,
  bleed, and centering, per
  pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste)
- and saves the result (with Image.save, per
  pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save).

The program exits via sys.exit:
- if the user does not specify exactly two command-line arguments,
- if the input's and output's names do not end in .jpg, .jpeg, or .png,
  case-insensitively,
- if the input's name does not have the same extension as the output's name, or
- if the specified input does not exist.

This program assumes that the input will be a photo of someone posing in just
the right way, so that, when they're resized and cropped, the shirt appears
to fit perfectly.

If you'd like to run your program on a photo of yourself, first drag the
photo over to VS Code's file explorer, into the same folder as shirt.py. No
need to submit any photos with your code. But, if you would like, you're
welcome (but not expected) to share a photo of yourself wearing your virtual
shirt in any of CS50's communities!"""

from sys import argv, exit
from os.path import splitext
from PIL import Image, ImageOps

VALID_EXTENSIONS: list[str] = {".JPG", ".JPEG", ".PNG"}

def main() -> None:
    # Check exactly two command-line arguments are parsed
    # (excluding the current module)
    if len(argv) > 3:
        exit("Too many command-line arguments")
    elif len(argv) < 3:
        exit("Too few command-line arguments")
    else:
        import_filename: str = argv[1]
        export_filename: str = argv[2]

    # Check import and export filetypes
    _, import_extension = splitext(import_filename)
    _, export_extension = splitext(export_filename)

    if import_extension.upper() not in VALID_EXTENSIONS:
      exit("Invalid input")

    elif export_extension.upper() not in VALID_EXTENSIONS:
        exit("Invalid output")

    elif import_extension.upper() != export_extension.upper():
        exit("Input and output have different extensions")

    # Import the shirt image
    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        with Image.open(import_filename) as img:
            # Crop and resize imported image
            img = ImageOps.fit(img, size)

            # Overlay shirt on imported image
            img.paste(shirt, shirt)

            # Save/export image
            img.save(export_filename)
    except FileNotFoundError:
        exit("Input does not exist")

if __name__ == "__main__":
    main()