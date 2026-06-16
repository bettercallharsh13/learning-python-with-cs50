from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
    figlet.setFont(f=font)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")



text = input("Input: ")
print("Output:")
print(figlet.renderText(text))
