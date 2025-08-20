"""“Ah, well,” said Tonks, slamming the trunk's lid shut, “at least it's all
in. That could do with a bit of cleaning, too.” She pointed her wand at
Hedwig's cage. “Scourgify.” A few feathers and droppings vanished.

— Harry Potter and the Order of the Phoenix

Data, too, often needs to be “cleaned,” as by reformatting it, so that values
are in a consistent, if not more convenient, format. Consider, for instance,
this CSV file of students, before.csv, below:

name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
...

Even though each “row” in the file has three values (last name, first name,
and house), the first two are combined into one “column” (name), escaped with
double quotes, with last name and first name separated by a comma and space.
Not ideal if Hogwarts wants to send a form letter to each student, as via
mail merge, since it'd be strange to start a letter with:

Dear Potter, Harry,

Rather than with, for instance:

Dear Harry,

This program:
- Expects the user to provide two command-line arguments:
  - the name of an existing CSV file to read as input, whose columns are
    assumed to be, in order, name and house, and
  - the name of a new CSV to write as output, whose columns should be, in
    order, first, last, and house.
- Converts that input to that output, splitting each name into a first name
  and last name. The program assumes that each student will have both a first
  name and last name.

If the user does not provide exactly two command-line arguments, or if the
first cannot be read, the program exits via sys.exit with an error message."""

from sys import argv, exit
from csv import DictReader, DictWriter

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

    # Check both files are CSV files
    for filename in [import_filename, export_filename]:
        try:
            _, extension = filename.rsplit(".", maxsplit=1)
        except ValueError:
            exit(f"'{filename}' not a file")
        else:
            if extension.upper() != "CSV":
                exit(f"'{filename}' not a CSV file")

    # Read the contents of the first CSV file
    try:
        with open(import_filename) as import_file, open(export_filename, mode="w", newline="") as export_file:
            reader: DictReader = DictReader(import_file)
            writer: DictWriter = DictWriter(export_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            # Write contents into the second CSV file
            for row in reader:
                try:
                    row["last"], row["first"] = row["name"].split(", ", maxsplit=1)
                except ValueError:
                    exit(f"'name' invalid format in {import_filename}")
                else:
                    row.pop("name")
                    writer.writerow(row)

    except FileNotFoundError:
        exit(f"Could not read {import_filename}")

if __name__ == "__main__":
    main()