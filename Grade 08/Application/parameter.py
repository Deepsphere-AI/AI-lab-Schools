import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
from title_1 import *
from img import *
with open('final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
def area_perameter():
    image()
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Application to Find the Perameter</h1>", unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,1.5,1.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Area of a Square ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["text"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",placeholder="In CM",key="text")  
    #----- Date to Day -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if  vAR_input_num !='':
                    vAR_input_num=int(vAR_input_num)
                    vAR_parameter=4 * vAR_input_num
                    st.markdown("### ")
                    st.success(vAR_parameter)
                else:
                    st.markdown("### ")
                    st.error("Error")
                with col1:
                    st.write("# Perameter is  ")

