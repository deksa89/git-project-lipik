'''
Problem klasifikacije rukom pisanih brojeva, MNIST podatkovni skup
Izgradnja, treniranje i evaluacija potpuno povezane neuronske mreze u Kerasu.

'''

# TODO:
# - ucitajte potrebne biblioteke
from tensorflow import _keras_module
from  tensorflow.keras import layers
import numpy as np
from matplotlib import pyplot as plt



# TODO:

# - ucitajte podatke pomocu funkcije keras.datasets.mnist.load_data
# - podaci trebaju biti spremljeni u numpy polja naziva x_train, y_train, x_test, y_test




# TODO:
# - pomocu matplotlib prikazite primjere slika iz trening skupa
# - koristite funkciju subplot i prikazite npr. devet ulaznih slika na jednoj figure




# TODO:
# - skaliraj ulazne podatke (x_train i x_test) na raspon [0,1]



# TODO:
# - reshapeaj x_train i x_test na oblik pogodan za potpuno povezanu mrezu (slika treba biti vektor od 28*28 elemenat)




# TODO:
# - pretvori y_train i y_test koji sadrze labele (0, 1, ... 9) u one hot encoding
# - koristi funkciju keras.utils.to_categorical




# TODO;
# - izgradi sekvencijalni model od dva skrivena sloja (128 neurona i 32 neurona), te jednim izlaznim slojem (softmax)
# - najprije razmisli koliko svaki sloj ima parametara, a tek onda pokreni metodu .summary()




# TODO:
# - podesi proces treniranja pomocu metode .compile




# TODO:
# - provedi ucenje mreze pomocu naredbe: history = model.fit(....
# - pomocu argumenta validation_split odvojite 10% podataka za validaciju




# TODO:
# - u objektu history nalaze se vrijednosti lossa i tocnosti tijekom ucenja
# - prikazite na istoj slici trening loss i validacijski loss tijekom ucenja
# - prikazite na istoj slici tocnost na trening skupu i tocnost na validacijskom skupu tijekom ucenja
# - na obje slike dodajte odgovarajucu legendu





# TODO: 
# - evaluacija mreze na testnim podacima
# - ispisi tocnost na testnim podacima u terminal




# TODO:
# - predikcije na testnim podacima
# - izdvojite indekse slika koje su dobro klasificirani i koje su pogresno u dva numpy polja




# TODO:
# - nacrtajte sliku koja sadrzi nekoliko primjera dobro klasificiranih slika
# - nacrtajte sliku koja sadrzi nekoliko primjera pogresno klasificiranih slika (iznad svake slike u title naznacite stvarnu klasu i predikciju)




# TODO:
# - koristite iz sklearn.metrics funkciju confusion_matrix za izracun matrice zabune
# - koristite iz sklearn.metrics funkciju classification_report za prikaz precision, recall, f1 mjere
# - prikazite dobivenu matricu zabune i metrike precision, recall, f1
# - rucno izracunajte precision i recall iz matrice zabune za jednu znamenku. Poklapa li se to s vrijednostima u classification reportu?




# TODO:
# - spremite model na disk u TensorFlow SavedModel obliku


