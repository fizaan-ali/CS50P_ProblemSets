import sys
import os.path
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

img1 = sys.argv[1]
img2 = sys.argv[2]

img1_ext = os.path.splitext(img1)[1].lower() # gives us a tuple of filename + ext we use only ext also lowercase
img2_ext = os.path.splitext(img2)[1].lower() 

valid_ext = {".jpg", ".jpeg", ".png"}

if img1_ext not in valid_ext or img2_ext not in valid_ext:
    sys.exit("Invalid file extensions")

if img1_ext != img2_ext:
    sys.exit("Both images have different extensions")


try:
    photo = Image.open(img1)
except FileNotFoundError:
    sys.exit("File doesn't exitst")

shirt = Image.open("shirt.png")
photo = ImageOps.fit(photo, shirt.size) # resize photo to shirt size
photo.paste(shirt, shirt)
photo.save(img2)
