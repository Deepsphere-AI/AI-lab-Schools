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
def mark():
    image()
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Application to MarkSheet</h1>", unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,1.5,1.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Marks ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["text1"] = ""
            st.session_state["text2"] = ""
            st.session_state["text3"] = ""
            st.session_state["text4"] = ""
            st.session_state["text5"] = ""
        st.button("Clear", on_click=clear_text)  
    with col2:
        vAR_input_num1=st.text_input("",placeholder="Language-1",key="text1")  
        vAR_input_num2=st.text_input("",placeholder="Language-2",key="text2")  
        vAR_input_num3=st.text_input("",placeholder="Mathematics",key="text3")  
        vAR_input_num4=st.text_input("",placeholder="Social Science",key="text4")  
        vAR_input_num5=st.text_input("",placeholder="Social",key="text5")  
    
    #-----squreroot-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            
            with col2:
                if vAR_input_num1 !='':
                    #------change data type-------#
                    vAR_input_num1=int(vAR_input_num1)
                    vAR_input_num2=int(vAR_input_num2)
                    vAR_input_num3=int(vAR_input_num3)
                    vAR_input_num4=int(vAR_input_num4)
                    vAR_input_num5=int(vAR_input_num5)
                    vAR_total = vAR_input_num1 + vAR_input_num2 + vAR_input_num3 + vAR_input_num4 + vAR_input_num5
                    vAR_average = vAR_total/5.0
                    vAR_percentage = (vAR_total / 500.0) * 100
                    st.success(vAR_total)
                    st.success(vAR_average)
                    st.success(vAR_percentage)
                
                    with col1:
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.markdown("# ")
                        st.write("# Total ")
                        st.write("# Average ")
                        st.write("# Percentage % ")
                else:
                    st.error("Error")
            
