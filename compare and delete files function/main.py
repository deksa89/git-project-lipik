import os
import glob
from pathlib import Path


processed_images = glob.glob("Images/*.jpg")

def removing_photos(processed_images):
    for processed_image in processed_images:
        stem_image = Path(processed_image).stem
        txt_file = f"Labels/{stem_image}.txt" 

        if not os.path.exists(txt_file):
            os.remove(processed_image)
            #print(processed_image)

removing_photos(processed_images)










