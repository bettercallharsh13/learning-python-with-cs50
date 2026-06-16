import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    filename = sys.argv[1]

    try:
        with open(filename) as file:
            reader = csv.reader(file)

            table = []
            for row in reader:
                table.append(row)

            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
