from PIL import Image, ImageOps
import os
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(sys.argv[1])[1].lower() not in [".jpeg", ".jpg", ".png"]:
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[2])[1].lower() not in [".jpeg", ".jpg", ".png"]:
    sys.exit("Invalid output")
elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")
else:
    shirt = Image.open("shirt.png")
    input_image = ImageOps.fit(input_image, size=shirt.size)
    input_image.paste(shirt, shirt)
    input_image.save(sys.argv[2])