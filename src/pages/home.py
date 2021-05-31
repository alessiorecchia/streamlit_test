#Home page for the web app
import streamlit as st
import base64
from PIL import Image
import webbrowser

def write():
    st.title("The Team")
    st.markdown(
           """## About us

We are a team of developers who are divided by nation but united by passion to learn. We are currently
developing our AI skills at [_Strive School_](https://strive.school/) with not only theortical knowledge but also
applying it practically. One such example is this web application that you are in. 



            """
    )

    st.markdown(
        """## Team Pull&Bear

We are the Pull&Bear Team, feel free to reach us on our LinkeIn pages
        """
    )
    st.write("![Your Awsome GIF](https://media.tenor.com/images/2b5ab573093a82c466b461129f77c8a8/tenor.gif)")


#Give the details of the team
    def dummy_fun():
        st.markdown("## Members:")
        if st.button('Olatunde Salami'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/salamituns/')
        elif st.button('Lakshmipathi rao Devalla'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/devalla-lakshmipathirao/')
        elif st.button('Madina Zhenisbek'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/madina-zhenisbek/')
        elif st.button('Alessio Recchia'):
            webbrowser.open_new_tab('https://www.linkedin.com/in/alessio-recchia-3abb3522/')
    dummy_fun()