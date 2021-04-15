# import streamlit as st
# from PIL import Image # Required to show images
# import pandas as pd
# logo = Image.open("logo.png")
# st.sidebar.image(logo, width=100)

# PAGES = {
#     "Home": src.pages.home,
#     "The Magic": src.pages.insights,
#     # "Gallery": src.pages.gallery.index,
    # "Vision": src.pages.vision,
    # "About": src.pages.about,
# }

import streamlit as st

# import awesome_streamlit as ast

import src.pages.home
import src.pages.insights
import src.pages.plot
import src.pages.data

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "The Magic": src.pages.insights,
    "The Plot": src.pages.plot,
    "The Dangeon": src.pages.data,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        st.sidebar.title("Contribute")
        st.sidebar.info(
            "This an open source project and you are very welcome to **contribute** your awesome "
            "comments, questions, resources and apps as "
            "[issues](https://github.com/alessiorecchia/hufflepuff_team/issues) of or "
            "[pull requests](https://github.com/alessiorecchia/hufflepuff_team/pulls) "
            "to the [source code](https://github.com/alessiorecchia/hufflepuff_team). "
        )
        st.sidebar.title("About")
        st.sidebar.info(
#         """
#         This app is maintained by Marc Skov Madsen. You can learn more about me at
#         [datamodelsanalytics.com](https://datamodelsanalytics.com).
# """
    )


if __name__ == "__main__":
    main()




# Text/Title
# st.title("Welcome to demo app")

# st.sidebar.header("Sidebar")
# st.sidebar.text("Writing on the sidebar!")
# st.sidebar.markdown("""This is a template for [Streamlit](https://www.streamlit.io/) to publish some results from your first AI Build Week!
# I wrote some examples of things you could do using Streamlit. Go at the end of the document to look for more resources to learn from!""")

# # Header/Subheader
# st.header("This is a header")
# st.subheader("This is a subheader")

# st.text("This is text")
# st.markdown("""### I know, this webapp looks like the Antonio's one. And it is it!
# I hope you guys are better than me in making things look cool (I know you are!). Scroll down to see other stuff I changed!""")

# st.markdown("### Display stuff with `st.write(python_code)`")
# hello_world_variable = "Hello World"
# st.write(hello_world_variable)

# st.markdown("### Create a button with `st.button('Text')`")
# st.button("Click me")

# st.markdown("### If statement with buttons")
# if st.button("Click to show spoiler"):
#     st.write("Bazinga!")

# st.markdown("### Success/Info/Warning/Error")

# st.success("Successful!")
# st.info("Information")
# st.warning("Warning!")
# st.error("Error!")

# st.markdown("### Raise exceptions")

# st.exception("AnError {This app is too cool. Cool it down.}")

# st.markdown("### Load images")

# img = Image.open("fitting_comparison.png")
# st.image(img, caption="Comparison of all fitting function")

# st.subheader("Widgets!")
# # Widget 
# if st.checkbox("Show/Hide"):
#     st.text("Showing or Hiding Widget")

# status = st.radio("What is you status", ("Active", "Inactive"))
# if status == "Active":
#     st.success("You are Active")
# else:
#     st.warning("You're Inactive")

# SelectBox
# occupation = st.selectbox("Your occupation", ["Programmer", "Data Scientist", "Striver", "Trying to survive", "Already died :D"])
# st.write("You selected", occupation)

# music = st.multiselect("Which music do you like?", ["Rock", "Pop", "EDM", "Electronic", "Classical", "Traditional"])
# st.write("You selected", len(music), "music genres")

# age = st.slider("How old are you?", 18,100)
# st.write(age)

# where = st.text_area("Where are you from? Write your city to display it on the map", "Type here...")
# from geopy.geocoders import Nominatim
# if st.button("Submit"):
#     geolocator = Nominatim(user_agent="a")
#     location = geolocator.geocode(where)
#     lat = location.latitude
#     lon = location.longitude
#     map_df = pd.DataFrame.from_dict({"lat":[lat], "lon":[lon]})
#     st.map(map_df)

# import datetime
# today = st.date_input("Today is", datetime.datetime.now())

# st.text("Display JSON")
# st.json({"Strive":{"Professor": {"name": "Jan", "subject":"being-great!"}, "TA":{"name":"Antonio", "subject":"being-awesome!"} }})

# Display Row Code

# st.text("Display Raw Code")
# st.code("import numpy as np")

# with st.echo():
#     import pandas as pd
#     df = pd.DataFrame()

# import time
# st.text("Loading bar and spinner")
# my_bar = st.progress(0)
# if st.button("Progress bar"):
#     with st.spinner("Waiting .."):
        
#         for p in range(0,120,20):
#             time.sleep(0.5)
#             my_bar = my_bar.progress(p)
#     st.success("Finished")


# st.balloons()

# st.header("Pandas and Visualization")

# st.markdown("""The great thing about Streamlit is that you can work in Python as you normally do, and then you can add an "interactive layer" to it!
# If you look at the code down here, the dataset is loaded using pandas as you're used to.
# In this example, we will use a csv file created scraping from IMDb last time.""")

# import pandas as pd
# import numpy as np

# df = pd.read_csv("500_rows.csv")
# df['minmax_norm_ratings'] = 1 + (df['avg_rating'] - df['avg_rating'].min()) / (df['avg_rating'].max() - df['avg_rating'].min()) * 9
# df['mean_norm_ratings'] = (1 + (df['avg_rating'] - df['avg_rating'].mean()) / (df['avg_rating'].max() - df['avg_rating'].min())) * 4.5 +1


# if st.button("Show me the data."):
#     st.dataframe(df)

# st.markdown("If you want to display only few columns, you can do like the following:")

# columns_to_show = st.multiselect("Select the columns you want to display", df.columns)
# st.markdown("Filter out the movies under a threshold of ratings:")
# threshold = st.slider("Filter movies for less than", 2, 10)
# filtered = df[df["avg_rating"] >= threshold]
# st.dataframe(filtered[columns_to_show])



# st.subheader("Visualization with Matplotlib")

# import matplotlib.pyplot as plt

# def plot_norm(not_norm_series, norm_series, norm_type: str, bins_ = 20, not_norm_color='#e67e4d', norm_color='#e67eff', edgecolor_='black'):
    
#     # defining some useful variables
#     norm_min = round(norm_series.min(), 2)
#     norm_max = round(norm_series.max(), 2)

    
#     # Set the number of subplots and the fig dimensions
#     fig, ax = plt.subplots(1, 2, figsize = (15,7))

#     # defining the not-normilized graph
#     ax[0].hist(not_norm_series, bins=bins_, color=not_norm_color, histtype='bar', edgecolor=edgecolor_)
#     ax[0].set_title("Not normalized")
#     ax[0].set_xlabel('Ratings')
#     ax[0].set_ylabel('Frequency')

#     # defining the normilized graph
#     ax[1].hist(norm_series, bins=bins_, color=norm_color, histtype='bar', edgecolor=edgecolor_)
#     ax[1].set_title(norm_type)
#     ax[1].set_xlabel(f'Ratings (normalized {norm_min} to {norm_max})')
#     ax[1].set_ylabel('Frequency')

#     # Set the ticks for x axis in normalized graph, according to the data range
#     plt.sca(ax[1])
#     plt.xticks(np.arange(norm_min, norm_max + 1, 1))

#     return fig

# # Examples
# fig1 = plot_norm(df.avg_rating, df.minmax_norm_ratings, norm_type='Min-Max normalization')
# fig2 = plot_norm(df.avg_rating, df.mean_norm_ratings, norm_type='Mean normalization')

# st.pyplot(fig1)
# st.pyplot(fig2)



# import plotly.express as px
# fig1 = px.bar(df, x = 'author', y = 'reviews',title = 'very silly test plot')

# st.plotly_chart(fig1)

# st.header("Conclusions")
# st.markdown("""Here you have seen a couple of things you can do using Streamlit.
# I found the process pretty smooth myself, very intuitive once you know a bit of Python.
# I want to stress a bit the importance of visualizing things: you're going to deal with people, and if you can show 
# stuff, people can trust you faster... and give you a job.
# So I recommend you to take care of building a nice portfolio, to share it on the internet, so that you can be exposed to people that
# are seeking smart guys and gals like you to be hired!
# """)
# st.header("More resources")

# st.markdown("""Following a bunch of links to reduce your *Google fatigue*:
# - Streamlit crash course (*not* covering pandas and plotting) https://www.youtube.com/watch?v=_9WiB2PDO7k
# - Streamlit Tutorials Playlist from [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q) https://www.youtube.com/watch?v=ZZ4B0QUHuNc
# - Streamlit official documentation https://docs.streamlit.io/
# - Streamlit cheat sheet https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
# - How to deploy your Streamlit web-app with Heroku https://towardsdatascience.com/from-streamlit-to-heroku-62a655b7319
#  """)