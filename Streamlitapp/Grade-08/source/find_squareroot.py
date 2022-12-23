import streamlit as st
from streamlit_option_menu import option_menu
import math
from PIL import Image
import source.title_1 as head
def square_root():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Square Root </p>", unsafe_allow_html=True)
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
            st.session_state["Clear_Squareroot"] = 0
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.number_input("",min_value=0,key="Clear_Squareroot")  
    #-----squreroot-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num == int or float:
                    square=math.sqrt(vAR_input_num)
                    square=round(square,4)
                    st.success(square)
                else:
                    st.error("Error")
                with col1:
                    st.write("# Square root ")
