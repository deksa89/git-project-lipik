from PIL import Image

# show image
# x = Image.open("vehicle.jpg")

# rotate image
# x90 = x.rotate(90)

# save image as vehicle90.jpg
# x90 = x90.save("vehicle90.jpg")

# crop rotated image
x90 = Image.open("vehicle90.jpg")

# Size of the image in pixels (size of original image)
width, height = x90.size
print(width, height)

# Setting the points for cropped image
left = 389 / 2
right = 1589 - (389 / 2)
top = 0
bottom = 1200

cropped = x90.crop((left, top, right, bottom))
cropped = cropped.save("kropana.jpg")
