import streamlit as st
from streamlit_option_menu import option_menu
import math
import source.title_1 as head
def cuboid_1():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Cuboid </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the length ")
        st.markdown("### ")
        st.write("# Enter the Breadth ")
        st.markdown("### ")
        st.write("# Enter the Height ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Square"] = 0
            st.session_state["Clear_breadth"] = 0
            st.session_state["Clear_Height"] = 0
            st.session_state["cubiod_selectbox"] = "Select"
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_length=st.number_input("",min_value=0.00,step=1.0,key="Clear_length") 
        vAR_input_breadth=st.number_input("",min_value=0.00,step=1.0,key="Clear_breadth")
        vAR_input_Height=st.number_input("",min_value=0.00,step=1.0,key="Clear_Height") 
        selected = st.selectbox("",
                            ["Select","Surface area","Volume","Space diagonal"],key="cubiod_selectbox")

        
    #-----cuboid-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_breadth and vAR_input_Height and vAR_input_length !=0:
                    if  selected == 'Surface area':
                        vAR_Surface_area = 2 * ( vAR_input_length * vAR_input_breadth +  vAR_input_breadth * vAR_input_Height + vAR_input_Height * vAR_input_length)
                        vAR_Surface_area = round(vAR_Surface_area,2)
                        st.success(vAR_Surface_area)
                    elif  selected == "Volume":    
                        vAR_Volume = (vAR_input_length *  vAR_input_breadth * vAR_input_Height)
                        vAR_Volume = round(vAR_Volume,2)
                        st.success(vAR_Volume)
                    elif  selected == "Space diagonal":    
                        vAR_Space_diagonal = math.sqrt(vAR_input_length**2 + vAR_input_breadth**2 + vAR_input_Height**2)
                        vAR_Space_diagonal = round(vAR_Space_diagonal,2)
                        st.success(vAR_Space_diagonal)               
                else:
                    st.error("Error")
                with col1:
                    st.markdown("# ")
                    st.markdown("# ")
                    st.markdown(" ")
                    st.write("# Result ")