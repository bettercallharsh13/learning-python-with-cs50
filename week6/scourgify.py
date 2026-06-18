import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")

    students = []

    try:
        with open(sys.argv[1]) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                last, first = row["name"].split(", ")
                students.append(
                    {
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    }
                )



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w", newline="") as outfile:
        writer = csv.DictWriter(
            outfile,
            fieldnames=["first", "last", "house"]
        )
        writer.writeheader()

        for i in students:
            writer.writerow(i)

if __name__ == "__main__":
    main()
