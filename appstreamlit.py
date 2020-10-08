#Importing necessary libraries
import os
import shutil
import random

import numpy as np
import cv2
import efficientnet.tfkeras as efn
from PIL import Image, ImageOps

import tensorflow as tf
from keras.models import load_model
  
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import streamlit as st

st.set_option('deprecation.showfileUploaderEncoding',False)
#Setting the title of the web app
st.title("Upload + Classification Example")

#Putting the loaded model into cache so that we does not have to load model everytime we predict
@st.cache(allow_output_mutation=True)
def load_our_model():
  model = tf.keras.models.load_model('/content/DR B3.h5')
  return model

#Loading the model into memory
model = load_our_model()

#Uploading the image through web app and storing the image as numpy array
uploaded_file = st.file_uploader("Choose an image...", type="png")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    new_array = cv2.resize(img, (128, 128))
    new_array = new_array/255
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    
    from keras.preprocessing.image import load_img
    from keras.preprocessing.image import img_to_array
     
    #Predicting the class of the image and displaying it on the web app 
    x = np.expand_dims(new_array, axis=0)
    y = model.predict(x)
    y_classes = y.argmax(axis=-1)
    if y_classes == 1:
      label = "Mild"
    elif y_classes == 2:
      label = "Moderate"
    elif y_classes == 3:
      label = "No_DR"
    elif y_classes == 4:
      label = "Proliferate_DR"
    else:
      label = "Severe"
    st.write(label)

