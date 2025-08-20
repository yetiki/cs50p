"""Perhaps the most popular place for pizza in Harvard Square is Pinocchio's
Pizza & Subs, aka Noch's, known for its Sicilian pizza, which is “a deep-dish
or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio's also has whole
pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv,
below:

Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95

See regular.csv for a CSV file of regular pizzas as well.

Of course, a CSV file isn't the most customer-friendly format to look at.
Prettier might be a table, formatted as ASCII art, like this one:

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+

This program expects exactly one command-line argument, the name (or path) of
a CSV file in Pinocchio's format, and outputs a table formatted as ASCII art
using tabulate, a package on PyPI at pypi.org/project/tabulate. The table is
formatted using the library's grid format. If the user does not specify
exactly one command-line argument, or if the specified file's name does not
end in .csv, or if the specified file does not exist, the program instead
exit via sys.exit."""

from sys import argv, exit
from csv import DictReader
from tabulate import tabulate

def main() -> None:
    # Check exactly one command-line argument is parsed
    # (other than the current module)
    if len(argv) > 2:
        exit("Too many command-line arguments")
    elif len(argv) < 2:
        exit("Too few command-line arguments")
    else:
        filename: str = argv[1]

    # Check the parsed file is a CSV file
    extension: str
    _, extension = filename.rsplit(".", maxsplit=1)

    if extension.upper() != "CSV":
        exit("Not a CSV file")

    # Read the contents of the CSV file in Pinocchio's format
    try:
        with open(filename) as file:
            reader: DictReader = DictReader(file)

            # Check if CSV file is empty or missing a header row
            if not reader.fieldnames:
                exit("CSV file is empty or missing a header row")

            table: list[dict[str, str]] = [row for row in reader]
    except FileNotFoundError:
        exit("File does not exist")

    # Output the tables formatted as ASCII art
    print(tabulate(table, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()