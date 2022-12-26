import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
import source.title_1 as head


def date_to_day():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Day </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Date ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Day"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",placeholder="dd/mm/yyyy",key="Clear_Day")  
    #----- Date to Day -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                try:
                    if  vAR_input_num !='':
                        vAR_date = vAR_input_num.split("/")
                        vAR_date = vAR_date[0]+vAR_date[1]+vAR_date[2]
                        vAR_int = str(vAR_date)
                        vAR_date = pd.to_datetime(vAR_int, format='%d%m%Y')
                        vAR_df = pd.Timestamp(vAR_date)
                        st.success(vAR_df.day_name())
                        with col1:
                            st.write("# Day ")
                    else:
                        st.error("Enter Valid Input")
                    
                except BaseException as error:
                    st.error("Follw this pattern dd/mm/yyyy")
