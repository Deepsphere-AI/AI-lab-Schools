import streamlit as st
from streamlit_option_menu import option_menu
import math
import source.title_1 as head
def Section_1():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Section Formuls </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the x1")
        st.markdown("### ")
        st.write("# Enter the x2 ")
        st.markdown("### ")
        st.write("# Enter the m1 ")
        st.markdown("### ")
        st.write("# Enter the m2 ")
        st.markdown("### ")
        st.write("# Select")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_sec_x1"] = 0
            st.session_state["Clear_sec_x2"] = 0
            st.session_state["Clear_sec_m1"] = 0
            st.session_state["Clear_sec_m2"] = 0
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_x1=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_x1") 
        vAR_input_x2=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_x2")
        vAR_input_m1=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_m1")
        vAR_input_m2=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_m2") 
        selected=st.selectbox("",["Internal Section","External Section"])
    #-----cylinder-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                
                if vAR_input_x1 and vAR_input_x2 and vAR_input_m1 and vAR_input_m2 != 0:
                    if selected == "Internal Section":
                        vAR_dis = (((vAR_input_m1*vAR_input_x2) + (vAR_input_m2*vAR_input_x1))/(vAR_input_m1 + vAR_input_m2))
                        st.success(vAR_dis)
                    if selected == "External Section":
                        vAR_dis = (((vAR_input_m1*vAR_input_x2) - (vAR_input_m2*vAR_input_x1))/(vAR_input_m1 - vAR_input_m2))
                        st.success(vAR_dis)
                else:
                    st.error("Error")
                with col1:
                    st.write("# Result ")
