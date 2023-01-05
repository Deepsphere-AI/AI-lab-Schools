import streamlit as st
from streamlit_option_menu import option_menu
import math
import source.title_1 as head
def Section_1():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Section Formuls </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,col3,w2=st.columns((1,3,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    
    with col1:
        st.markdown("")
        st.write("# Enter the x1 and y1")
        st.markdown("")
        st.write("# Enter the x2 and y2")
        st.markdown("### ")
        st.write("# Enter the m ")
        st.markdown("### ")
        st.write("# Enter the n ")
        st.markdown("### ")
        st.write("# Select")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_sec_x1"] = 0
            st.session_state["Clear_sec_x2"] = 0
            st.session_state["Clear_sec_y1"] = 0
            st.session_state["Clear_sec_y2"] = 0
            st.session_state["Clear_sec_m"] = 0
            st.session_state["Clear_sec_n"] = 0
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_x1=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_x1")
    with col3:
        vAR_input_y1=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_x2")
    with col2:   
        vAR_input_x2=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_y1")
    with col3:
        vAR_input_y2=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_y2")
    with col2:    
        vAR_input_m=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_m")
        vAR_input_n=st.number_input("",min_value=0.00,step=1.0,key="Clear_sec_n")
        selected=st.selectbox("",["Internal Section","External Section"])
    #-----cylinder-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                
                if vAR_input_x1 and vAR_input_x2 and vAR_input_m and vAR_input_n and vAR_input_y1 != 0:
                    if selected == "Internal Section":
                        vAR_dis = (((vAR_input_m*vAR_input_x2)+(vAR_input_n*vAR_input_x1))/vAR_input_n + vAR_input_m),(((vAR_input_m*vAR_input_y2)+(vAR_input_n*vAR_input_y1))/vAR_input_n + vAR_input_m)
                        st.success(vAR_dis)
                    if selected == "External Section":
                        vAR_dis = (((vAR_input_m*vAR_input_x2)-(vAR_input_n*vAR_input_x1))/vAR_input_n - vAR_input_m),(((vAR_input_m*vAR_input_y2)-(vAR_input_n*vAR_input_y1))/vAR_input_n - vAR_input_m)
                        st.success(vAR_dis)
                else:
                    st.error("Error")
                with col1:
                    st.write("# Result ")
