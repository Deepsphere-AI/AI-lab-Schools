import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
import source.title_1 as head
def area_perameter():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Perimeter from Area </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Side of a Square")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_parameter"] = 0
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.number_input("",min_value=0.00,step=1.0,key="Clear_parameter")  
    #----- Date to Day -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if  vAR_input_num == int or float:
                    vAR_input_num=int(vAR_input_num)
                    vAR_parameter=4 * math.squrt(vAR_input_num)
                    st.markdown("### ")
                    st.success(vAR_parameter)
                else:
                    st.markdown("### ")
                    st.error("Error")
                with col1:
                    st.markdown("")
                    st.write("# Perimeter is  ")
