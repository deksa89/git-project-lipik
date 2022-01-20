'''
Problem klasifikacije rukom pisanih brojeva, MNIST podatkovni skup
Izgradnja, treniranje i evaluacija potpuno povezane neuronske mreze u Kerasu.
'''

# TODO:
# - ucitajte potrebne biblioteke
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D


# TODO:

# - ucitajte podatke pomocu funkcije keras.datasets.mnist.load_data
# - podaci trebaju biti spremljeni u numpy polja naziva x_train, y_train, x_test, y_test

(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
print("X_train shape: ", X_train.shape)
print("y_train shape: ", y_train.shape)


# TODO:
# - pomocu matplotlib prikazite primjere slika iz trening skupa
# - koristite funkciju subplot i prikazite npr. devet ulaznih slika na jednoj figure
# for i in range(9):
#     plt.subplot(3,3, i+1)
#     plt.imshow(X_train[i], cmap=plt.get_cmap("gray"))
# #plt.show()



# TODO:
# - skaliraj ulazne podatke (x_train i x_test) na raspon [0,1]
X_train_s = X_train.astype("float32") / 255
X_test_s = X_test.astype("float32") / 255


# TODO:
# - reshapeaj x_train i x_test na oblik pogodan za potpuno povezanu mrezu (slika treba biti vektor od 28*28 elemenat)
X_train_s = X_train_s.reshape(60000, 28,28,1)
X_test_s = X_test_s.reshape(10000, 28,28,1)



# TODO:
# - pretvori y_train i y_test koji sadrze labele (0, 1, ... 9) u one hot encoding
# - koristi funkciju keras.utils.to_categorical
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO;
# PRIMJER KONVOLUCIJSKE NEURONSKE MREŽE
# - izgradi sekvencijalni model od dva skrivena sloja (128 neurona i 32 neurona), te jednim izlaznim slojem (softmax)
# - najprije razmisli koliko svaki sloj ima parametara, a tek onda pokreni metodu .summary()
model = keras.Sequential([
    layers.Input(shape=(28,28,1), name="ulaz"),
    layers.Conv2D(32, kernel_size=(3,3), padding="same", activation="relu"),
    layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    layers.Conv2D(64, kernel_size=(3,3), padding="same", activation="relu"),
    layers.MaxPool2D(pool_size=(2,2), strides=(2,2)),
    layers.Flatten(),
    layers.Dense(100, activation="relu"),
    layers.Dropout(rate=0.5),
    layers.Dense(50, activation="relu"),
    layers.Dense(10, activation="softmax", name="izlaz")
])

model.summary()


# TODO:
# - podesi proces treniranja pomocu metode .compile
model.compile(optimizer="adam",
              loss="categorical_crossentropy",
              metrics=["accuracy"]
              )



# TODO:
# - provedi ucenje mreze pomocu naredbe: history = model.fit(....
# - pomocu argumenta validation_split odvojite 10% podataka za validaciju

history = model.fit(
    X_train_s, y_train_s,
    batch_size=64,
    epochs = 60,
    validation_split = 0.1 #validation split kaze da uzimamo 10% podataka za validaciju
)


# TODO:
# - u objektu history nalaze se vrijednosti lossa i tocnosti tijekom ucenja
# - prikazite na istoj slici trening loss i validacijski loss tijekom ucenja
# - prikazite na istoj slici tocnost na trening skupu i tocnost na validacijskom skupu tijekom ucenja
# - na obje slike dodajte odgovarajucu legendu
# plt.figure(1, figsize=(16,10))
# plt.subplot(1,2,1)
# plt.plot(history.history["loss"], label = "train")
# plt.plot(history.history["val_loss"], label = "val")
# plt.xlabel("Epoha")
# plt.ylabel("Cross entropy loss")
#
#
# plt.subplot(1,2,2)
# plt.plot(history.history["accuracy"], label = "train")
# plt.plot(history.history["val_accuracy"], label = "val")
# plt.xlabel("Epoha")
# plt.ylabel("Accuracy")
#
#
# plt.legend()
# #plt.show()

# TODO:
# - evaluacija mreze na testnim podacima
# - ispisi tocnost na testnim podacima u terminal
score = model.evaluate(X_test_s, y_test_s)
print("test loss: ", score[0])
print("test accuracy: ", score[1])


# TODO:
# - predikcije na testnim podacima
# - izdvojite indekse slika koje su dobro klasificirani i koje su pogresno u dva numpy polja
predicted_vec = model.predict(X_test_s) #na datu sliku izbaci testnu sliku
predicted_classes = np.argmax(predicted_vec, axis=-1) #od uzetih vektora uzima maksimalnu vrijednost
correct_indices = np.nonzero(predicted_classes == y_test)[0]
incorrect_indices = np.nonzero(predicted_classes != y_test)[0]


# TODO:
# - nacrtajte sliku koja sadrzi nekoliko primjera dobro klasificiranih slika
# - nacrtajte sliku koja sadrzi nekoliko primjera pogresno klasificiranih slika (iznad svake slike u title naznacite stvarnu klasu i predikciju)
plt.figure(2)
for i, correct in enumerate(correct_indices[:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[correct], cmap="gray")
    plt.xticks([])
    plt.yticks([])
plt.show()

plt.figure(3)
for i, incorrect in enumerate(incorrect_indices[:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[incorrect], cmap="gray")
    plt.title("Predicted: " + str(predicted_classes[incorrect]) + " Stvarno: " + str(y_test[incorrect]))
    plt.xticks([])
    plt.yticks([])
plt.show()



# TODO:
# - koristite iz sklearn.metrics funkciju confusion_matrix za izracun matrice zabune
# - koristite iz sklearn.metrics funkciju classification_report za prikaz precision, recall, f1 mjere
# - prikazite dobivenu matricu zabune i metrike precision, recall, f1
# - rucno izracunajte precision i recall iz matrice zabune za jednu znamenku. Poklapa li se to s vrijednostima u classification reportu?
from sklearn.metrics import confusion_matrix, classification_report

conf_matrix = confusion_matrix(y_test, predicted_classes)
print(conf_matrix)

class_report = classification_report(y_test, predicted_classes)
print(class_report)


# TODO:
# - spremite model na disk u TensorFlow SavedModel obliku
model.save("CCN-fashion_mnist/")