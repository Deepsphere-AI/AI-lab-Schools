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
def mark():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Mark Sheet </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Marks ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["sub1"] = ""
            st.session_state["sub2"] = ""
            st.session_state["sub3"] = ""
            st.session_state["sub4"] = ""
            st.session_state["sub5"] = ""
        st.button("Clear", on_click=clear_text)  
    with col2:
        vAR_input_num1=st.text_input("",placeholder="Language-1",key="sub1")  
        vAR_input_num2=st.text_input("",placeholder="Language-2",key="sub2")  
        vAR_input_num3=st.text_input("",placeholder="Mathematics",key="sub3")  
        vAR_input_num4=st.text_input("",placeholder="Social Science",key="sub4")  
        vAR_input_num5=st.text_input("",placeholder="Social",key="sub5")  
    
    #-----squreroot-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            
            with col2:
                if vAR_input_num1 and vAR_input_num2 and vAR_input_num3 and vAR_input_num4 and vAR_input_num5.isnumeric():
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