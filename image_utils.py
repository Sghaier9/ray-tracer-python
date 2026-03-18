from PIL import Image
import numpy as np
print(">>> save_image_to_file signature OK") # pour voir l'enregistrement 

def save_image_to_file(image_array, path_to_save):
    rgb_image = (np.clip(image_array, 0.0, 1.0) * 255.0).astype(np.uint8)
    image = Image.fromarray(rgb_image)
    image.save(str(path_to_save))
