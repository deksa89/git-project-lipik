import os
import splitfolders

splitfolders.ratio("gtsrb_dataset/Train", output="gtsrb_dataset/Divided", seed=1337, ratio=(.85, 0.15))
print("gotovo")