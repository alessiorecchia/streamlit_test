import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.autograd import Variable

import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader

class CNN(nn.Module):
    
    def __init__(self):
        super(CNN, self).__init__()
        
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        self.fc1 = nn.Linear(in_features=64*14*14, out_features=1024)
        #self.drop = nn.Dropout2d(0.25)
        self.fc2 = nn.Linear(in_features=1024, out_features=512)
        self.fc3 = nn.Linear(in_features=512, out_features=10)

model = CNN()
model.load_state_dict(torch.load('Model_75%.pt'))
model.eval()



def write():

    st.title("Best Books of the 20th century :books:")
    st.header("""**Description**: """)
    st.markdown(
            """ 
One day you are browsing through the internet and stumbled upon [Goodreads](https://www.goodreads.com/). Being a
curious _Data Scientist_, you want to know what are the best books of 20th century. Well, worry not as we did that
just for you. \n
We scrapped the website for the first 1000 *_Best Books of the 20th century_* and made a nice dataframe so that
you could also analyse it. Later down the line, we will add some visualizations to better understand the relation
between different features.

If you would like to scrape the data of other book genres by yourself, you can easily do so by
modifying the source code which you can find [here](https://github.com/Deniz-shelby/goodreads_webscrap).\n
So without wasting any time, \n
            """
        )
        
    #Gif for "Let's begin"
    # st.write("![Your Awsome GIF](https://media.giphy.com/media/5zf2M4HgjjWszLd4a5/giphy.gif)")
    # st.write("\n")
    # st.write("\n")


    # st.header("**DataFrame**:")

    #This feature is not viable during deployment as its prompts user to upload a csv file
    #and we cannot except the user to have similar DataFrame.

    #Prompt the user to upload a csv file
    uploaded_file = st.file_uploader("Please choose an image file", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
       # do stuff
       uploaded_file = Image.open(uploaded_file).convert('LA')
       st.image(uploaded_file)