import streamlit as st
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
def age():
    image()
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Application to Find the Age</h1>", unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,1.5,1.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Date of Birth ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["text"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",placeholder="mm/dd/yyyy",key="text")  
    #-----squreroot-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num !='':
                    vAR_date=vAR_input_num.split("/")
                    for i in vAR_date:
                        if len(i)==2:
                            continue
                        else:
                            vAR_year=int(i)
                    current_year=date.today()
                    current_year=current_year.year
                    current_year=int(current_year)
                    vAR_age=current_year-vAR_year
                    st.success(vAR_age)
                else:
                    st.error("Error")
                with col1:
                    st.write("# Answer is ")
            
