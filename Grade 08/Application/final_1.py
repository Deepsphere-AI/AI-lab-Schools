import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
import math
from PIL import Image
import pyautogui as pt
from title_1 import *
from Data_types import *
from find_square import * 
from find_squareroot import * 
from find_cube import *
from date_input import *
from find_age import *
from find_avg import *
from profit_loss import *
from find_power import *
from parameter import *
from Mark_sheet import *
from gst import *

with open('final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

#---------Side bar-------#
with st.sidebar:
    selected = st.selectbox("",
                     ['Home','Square','Square Root','Cube','Find the Day','Find the Age',
                     'Find the Area of Perameter','Find the Average','Find the Mark Sheet','Find the Profit or Loss',
                     'Find the Selling Price','Find the Power Value'])
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Image"])
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"])
    st.markdown("")
    if st.button("Clear/Reset"):
        pt.hotkey("ctrl","F5")

#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == "Home":
            img =Image.open("Logo Color.jpg")
            st.image(img)
            title()
        if selected =="Square":
            square()
        if selected == "Square Root":
            square_root()
        if selected == "Cube":
            cube()
        if selected == "Find the Day":
            date_to_day()
        if selected == "Find the Age":
            age()
        if selected == "Find the Average":
            average()
        if selected == "Find the Profit or Loss":
            profit_or_loss()
        if selected == 'Find the Power Value':
            power_value()
        if selected == 'Find the Area of Perameter':
            area_perameter()
        if selected == 'Find the Mark Sheet':
            mark()
        if selected == 'Find the Selling Price':
           cal_GST()
    except BaseException as error:
        st.error(error)





