import streamlit as st
import pandas as pd
import numpy as np


st.header("Pandas and Visualization")

st.markdown("""The great thing about Streamlit is that you can work in Python as you normally do, and then you can add an "interactive layer" to it!
If you look at the code down here, the dataset is loaded using pandas as you're used to.
In this example, we will use a csv file created scraping from IMDb last time.""")

import pandas as pd
import numpy as np

df = pd.read_csv("500_rows.csv")
df['minmax_norm_ratings'] = 1 + (df['avg_rating'] - df['avg_rating'].min()) / (df['avg_rating'].max() - df['avg_rating'].min()) * 9
df['mean_norm_ratings'] = (1 + (df['avg_rating'] - df['avg_rating'].mean()) / (df['avg_rating'].max() - df['avg_rating'].min())) * 4.5 +1


if st.button("Show me the data."):
    st.dataframe(df)

st.markdown("If you want to display only few columns, you can do like the following:")

columns_to_show = st.multiselect("Select the columns you want to display", df.columns)
st.markdown("Filter out the movies under a threshold of ratings:")
threshold = st.slider("Filter movies for less than", 2, 10)
filtered = df[df["avg_rating"] >= threshold]
st.dataframe(filtered[columns_to_show])