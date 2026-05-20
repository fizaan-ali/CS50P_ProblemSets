import sys
import random

from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    my_font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    my_font = sys.argv[2]
else:
    sys.exit("Invalid usage")

line = input("Input: ")
figlet.setFont(font=my_font)

print(figlet.renderText(line))
