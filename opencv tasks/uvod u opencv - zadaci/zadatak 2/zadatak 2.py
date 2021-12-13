from PIL import Image, ImageOps
import glob

#path is where we are going to look for photos
path = "images"
# (prouci glob funkciju)
files = glob.glob(path + "/**/*.jpg", recursive=True)

brojac = 0
for i in files:
    brojac += 1
    slika = Image.open(i)
    siva = ImageOps.grayscale(slika)
    siva.save("output/img_" + str(brojac) + ".jpg")
