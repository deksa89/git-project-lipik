'''
Klasifikacija slika koje sadrze rukom pisane brojeve

'''
import keras.models
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np

# ucitavanje slike sa diska
filename = 'test.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


# TODO:
# - prikazi ucitanu sliku pomocu matplotlib
# - uvjerite se da slika ima oblika kao u MNIST datasetu -> (bijela znamenka na crnoj pozadini)
img = 1 - img.astype("float32")
plt.figure()
plt.imshow(img, cmap=plt.get_cmap("gray"))
plt.show()


# TODO:
# - transformirajte sliku u vektor odgovarajuce velicine za neuronsku mrezu
img = img.reshape(1, 28*28)


# TODO:
# - ucitajte spremljenu neuronsku mrezu pomocu funkcije keras.models.load_model()
model = keras.models.load_model("FCN")


# TODO:
# - napravi predikciju za ucitanu sliku i ispisi u terminal koju znamenku je prepoznala mreza
net_output = model.predict(img)
print(net_output)

label = np.argmax(model.predict(img))
label = str(int(label))
print("Na slici je znamenka: ", label)
