'''
Klasifikacija slika koje sadrze rukom pisane brojeve

'''

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



# TODO:
# - transformirajte sliku u vektor odgovarajuce velicine za neuronsku mrezu



# TODO:
# - ucitajte spremljenu neuronsku mrezu pomocu funkcije keras.models.load_model()



# TODO:
# - napravi predikciju za ucitanu sliku i ispisi u terminal koju znamenku je prepoznala mreza


