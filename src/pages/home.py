"""Home page shown when the user enters the application"""
import streamlit as st

# import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        # ast.shared.components.title_awesome("")
        st.write(
            """
                Home page
                Home page
                Home page
                Home page         
            """)