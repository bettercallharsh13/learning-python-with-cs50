import sys
from PIL import Image, ImageOps
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    if not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    input_ext = sys.argv[1].split(".")[-1].lower()
    output_ext = sys.argv[2].split(".")[-1].lower()
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])

        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt)

        photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
