import pyfiglet
import random
import sys

all_fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    font = random.choice(all_fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in all_fonts:
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(pyfiglet.figlet_format(text, font=font))
