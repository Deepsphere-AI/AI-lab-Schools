import streamlit as st
from streamlit_option_menu import option_menu
import math
from PIL import Image
from title_1 import *
def image():
    #---------Logo import-----------#
    img =Image.open("Logo Color.jpg")
    st.image(img)
    title()
    