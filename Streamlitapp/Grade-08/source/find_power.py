import streamlit as st
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
import source.title_1 as head

# with open('final.css') as f:
#         st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
def power_value():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Power Value </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Number ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Value"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",placeholder="Eg: 2^2",key="Clear_Value")  
    #-----squreroot-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                try:
                    if vAR_input_num !='':
                        vAR_split=vAR_input_num.split('^')
                        vAR_num=int(vAR_split[0])
                        vAR_power=int(vAR_split[1])
                        vAR_ans=pow(vAR_num, vAR_power)
                        st.markdown("")
                        st.markdown("")
                        st.success(vAR_ans)
                
                    else:
                        st.markdown("")
                        st.error("Error")
                    with col1:
                        st.markdown("")
                        st.markdown("")
                        st.write("# Result ")
                except BaseException as error:
                    st.error("follw this pattern 2^2")
