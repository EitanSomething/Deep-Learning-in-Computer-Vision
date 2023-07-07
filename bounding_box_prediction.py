import numpy as np
import os
import tensorflow as tf
import selective_search
from PIL import Image


def predict_image(image_path, model_path):
 
 # Recreate the exact same model, including its weights and the optimizer
    img = Image.open(image_path)
    new_model = tf.keras.models.load_model(model_path)

    # Show the model architecture
    new_model.summary()
    image_bbox = selective_search.selective_search_fast(image_path)
    array_numpy =np.append(image_bbox, np.empty(image_bbox.shape),axis = 1) 
    for i in array_numpy:
        cropped_image = _crop_image(img,i)
        i[1] = new_model.predict(cropped_image)

    return array_numpy

def _crop_image(example, bbox):
    bbox_rect = (bbox[1],bbox[0],bbox[1]+bbox[3],bbox[0]+bbox[2])
    return example.crop(bbox_rect)

predict_image("images.jpg", "model/saved_model/Efficient2mk2/")