import streamlit as st
from streamlit_option_menu import option_menu
import math
import source.title_1 as head
def Semi_perimeter():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Semi-perimeter </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the a ")
        st.markdown("### ")
        st.write("# Enter the b ")
        st.markdown("### ")
        st.write("# Enter the c ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_a"] = 0
            st.session_state["Clear_b"] = 0
            st.session_state["Clear_c"] = 0
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_a=st.number_input("",min_value=0.00,step=1.0,key="Clear_a") 
        vAR_input_b=st.number_input("",min_value=0.00,step=1.0,key="Clear_b")
        vAR_input_c=st.number_input("",min_value=0.00,step=1.0,key="Clear_c") 
        
    #-----semi perimeter-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_a and vAR_input_b and vAR_input_c !=0:
                    vAR_area=((vAR_input_a + vAR_input_b + vAR_input_c) /2)
                    st.success(vAR_area) 
                else:
                    st.error("Error")
                with col1:
                    st.markdown("# ")
                    st.markdown("# ")
                    st.markdown(" ")
                    st.write("# Result ")
