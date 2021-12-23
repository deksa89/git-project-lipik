import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

dataset_path = "dataset"
mean_img_width = 101 # to je profesor odredio kao najoptimalniju velicinu
mean_img_height = 264


def load_ped_dataset(images_folder): # cilj funk je vracanje svake slike HOG znacajke #
    ped_image_dataset = os.path.join(dataset_path, images_folder) # spajamo putanje s koje cemo izlistati slike


    pedestrian_hog_list = []

    for file in os.listdir(ped_image_dataset):
        if file.endswith(".png"):
            image_name = os.path.join(ped_image_dataset, file)

            image_ped = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
            image_ped = cv2.resize(image_ped, (mean_img_width, mean_img_height))

            HOG_desc, hog_image = hog(image_ped, visualize=True) #visualize True prikazuje sliku

            # fig, axes = plt.subplots(1, 2)
            # axes[0].imshow(image_ped, cmap="gray") #u matplotlib kada predajemo crnobijelu sliku moramo navasti da je "grey"
            # axes[1].imshow(hog_image, cmap="gray")
            # plt.show()

            pedestrian_hog_list.append(HOG_desc) #apendamo nase znacajke

    pedestrian_hog_list = np.array(pedestrian_hog_list)

    return  pedestrian_hog_list


ped_dataset = load_ped_dataset("ped")
no_ped_dataset = load_ped_dataset("no_ped")

pedestrian_labels = np.ones((ped_dataset.shape[0]))
no_pedestrian_labels = np.zeros((no_ped_dataset.shape[0]))


X = np.concatenate((ped_dataset, no_ped_dataset))
y = np.concatenate((pedestrian_labels, no_pedestrian_labels))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True) #velika razlika izmedu True i False, pomijesat ce slike ped i no ped te na taj nacin uciti

classifier = MLPClassifier(random_state=1)

classifier.fit(X_train, y_train)

score = classifier.score(X_test, y_test)

#print(score)


test_image = cv2.imread("dataset/test_img.png", cv2.IMREAD_GRAYSCALE)
image_height = test_image.shape[0]
image_width = test_image.shape[1]



max_pedestrian_probability = 0
final_top_left_bb = (0, 0) #koordinate u kojima se nalazi pjesak
final_bottom_right = (0, 0)

for i in range(0, image_height - mean_img_height - 1, 10): #redak
    for j in range(0, image_width - mean_img_width - 1, 10): #stupac
        roi = test_image[i: i + mean_img_height, j: j + mean_img_width]
        HOG_desc, HOG_image = hog(roi, visualize=True)

        HOG_desc = HOG_desc.reshape((1, -1)) #radimo reshape jer je HOG_desc vektor a predict_proba ocekuje matricu koja je sada 1 puta dimenzija naseg vektora
        roi_probabilities = classifier.predict_proba(HOG_desc)

        pedestrian_probability = roi_probabilities[0, 1] # 0 jer smo poslali samo jednu sliku, 1 znaci da ce vratiti pjesaka

        if pedestrian_probability > max_pedestrian_probability:
            max_pedestrian_probability = pedestrian_probability
            final_top_left_bb = (j, i)
            final_bottom_right = (j + mean_img_width, i + mean_img_height)


detection_image = cv2.rectangle(test_image, final_top_left_bb, final_bottom_right, 255, thickness=2)
cv2.imshow("detection", detection_image)
cv2.waitKey()
cv2.destroyAllWindows()

