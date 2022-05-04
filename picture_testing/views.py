#Import library

##Import django library requirements
from django.shortcuts import render

##Import default pyhton library
import pandas as pd
import numpy as np

##Import ready to used model
import pickle

##To process image data
from pillow import Image

## To process deep learning model
import tensorflow as tf
from tensorflow import keras

# Import function and models
def get_colors(image_file, numcolors=10, resize=150):
    # Resize image to speed up processing
    img = Image.open(image_file)
    img = img.copy()
    img.thumbnail((resize, resize))

    # Reduce to palette
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=numcolors)

    # Find dominant colors
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    colors = list()
    for i in range(numcolors):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        colors.append(tuple(dominant_color))

    return colors

def pred_cnn(image_file):
    class_names=['no_damage','low_damage','medium_damage','fully_damage']

    img = keras.preprocessing.image.load_img(
        image_file, target_size=(180,180)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    final_result = class_names[np.argmax(score)]

    return final_result

# Create your views here.
