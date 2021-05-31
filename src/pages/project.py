import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px
import time

def write():

    st.title("The Project")
    st.header("""**Description**: """)
    st.markdown(
            """
Our goal is to build and train a Neural Network classifier in Pytorch for classifying the clothes in the Fashion-MNIST Dataset to achieve a test accuracy grater than 0.95
We will also visualize the loss behaviour over time for the training and the validation set and inspect the samples that have been misclassified, to figure out why the model failed and how to improve it.
""")
    st.write("![Your Awsome GIF](https://cdnb.artstation.com/p/assets/images/images/010/538/265/original/dane-vranes-datascience-optimized.gif?1524951477)")

    st.markdown(
        """

Below you can find detailed information abot the Fashion-MNIST Dataset.

Context\n
Fashion-MNIST is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. Zalando intends Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.\n

The original MNIST dataset contains a lot of handwritten digits. Members of the AI/ML/Data Science community love this 
dataset and use it as a benchmark to validate their algorithms. In fact, MNIST is often the first dataset researchers try. 
"If it doesn't work on MNIST, it won't work at all", they said. "Well, if it does work on MNIST, it may still fail on others."\n

Zalando seeks to replace the original MNIST dataset\n

Content
Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single 
pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. 
This pixel-value is an integer between 0 and 255. The training and test data sets have 785 columns. The first column consists 
of the class labels (see above), and represents the article of clothing. The rest of the columns contain the pixel-values of 
the associated image.\n

To locate a pixel on the image, suppose that we have decomposed x as x = i * 28 + j, where i and j are integers between 0 and 27. The pixel is located on row i and column j of a 28 x 28 matrix.
For example, pixel31 indicates the pixel that is in the fourth column from the left, and the second row from the top, as in the ascii-diagram below.


Labels\n

Each training and test example is assigned to one of the following labels:\n

0 T-shirt/top\n
1 Trouser\n
2 Pullover\n
3 Dress\n
4 Coat\n
5 Sandal\n
6 Shirt\n
7 Sneaker\n
8 Bag\n
9 Ankle boot\n

More on [kaggle.com](https://www.kaggle.com/zalando-research/fashionmnist)

            """
        )
        
  