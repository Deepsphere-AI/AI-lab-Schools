import streamlit as st
from streamlit_option_menu import option_menu
import math
import source.title_1 as head
def cube_1():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Surface Area and Volume of the Cube </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Area ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_area"] = 0
            st.session_state["cube_selectbox"] = "Select"
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_area=st.number_input("",min_value=0.00,step=1.0,key="Clear_area") 
        selected = st.selectbox("",
                            ["Select","Surface Area","Volume"],key="cube_selectbox")
        
    #-----cuboid-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_area !=0:
                    if selected == "Surface Area":
                        vAR_area= (6 * vAR_input_area * vAR_input_area)   
                        st.success(vAR_area)
                    if selected == "Volume":
                        vAR_area= (vAR_input_area**3)   
                        st.success(vAR_area)
                else:
                    st.error("Error")
                with col1:
                    st.markdown("# ")
                    st.markdown("# ")
                    st.markdown(" ")
                    st.write("# Result ")
