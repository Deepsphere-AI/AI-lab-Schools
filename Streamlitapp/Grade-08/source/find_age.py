import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import math
import datetime
from datetime import date
import calendar
from PIL import Image
import source.title_1 as head

def age():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Find the Age </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Date of Birth ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Age"] = date.today()
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.date_input("",min_value=pd.to_datetime('1900-01-01', format='%Y-%m-%d'),max_value=date.today(),key="Clear_Age")  
    #-----squreroot-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num !='':
                    def calculateAge(birthDate):
                        today = date.today()
                        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
                        return age
                    vAR_age=calculateAge(vAR_input_num)
                    st.markdown("")
                    st.markdown("")
                    st.success(vAR_age)
                else:
                    st.error("Error")
                with col1:
                    st.write("# Answer is ")