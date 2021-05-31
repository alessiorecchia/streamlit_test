import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px
import time

def write():

    st.title("Developing and training the model")
    #st.header("""**Description**: """)
    st.markdown(
            """ 
We created a [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network) with the following structure:

- first convolutional layer: 1 channel (the images are in grayscale), 3 x 3 filter 
            """
        )
        
    #Gif for "Let's begin"
    st.write("![Your Awsome GIF](https://la.mathworks.com/matlabcentral/mlc-downloads/downloads/3682850e-dc4d-4c07-a2c8-4e58a721b65b/f50369fd-32ea-477d-b74c-1b3f6e014122/images/screenshot.gif)")
    st.write("\n")
    st.write("\n")


    st.header("**DataFrame**:")

    #This feature is not viable during deployment as its prompts user to upload a csv file
    #and we cannot except the user to have similar DataFrame.

    #Prompt the user to upload a csv file
    #uploaded_file = st.file_uploader("Please choose a .CSV file", type=['csv'])
    #if uploaded_file is not None:
     #   # do stuff
      #  df = pd.read_csv(uploaded_file)
       # df1 = df.head()

    