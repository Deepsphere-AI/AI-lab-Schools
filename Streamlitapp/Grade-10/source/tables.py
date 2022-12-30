import streamlit as st
from streamlit_option_menu import option_menu
import math
import source.title_1 as head
def table_1():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Distance </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the θ")
        st.markdown("### ")
        st.write("# Enter the Degree° ")
    #-------------Assen the Value-----------------------#
    vAR_sin = ['0','1/2','1/2', '3/2', '1']
    vAR_cos = ['1 ','3/2 ','1/2', '1/2', '0']
    vAR_Tan = ['0', '1/3', '1', '3', '∞' ]
    vAR_cot = ['∞', '3', '1', '1/3', '0' ]
    vAR_sec = ['1', '2/3', '2', '2', '∞']
    vAR_cosec = ['∞', '2', '2', '2/3', '1' ]
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["table_selectbox"] = "θ"
            st.session_state["table_selectbox1"] = "°"
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_theta = st.selectbox("",
                            ["θ","Sin","Cos","Tan","Cot","Sec","Cosec"],key="table_selectbox") 
        vAR_degree = st.selectbox("",
                            ["°","0°","30°","45°","60°","90°"],key="table_selectbox1")
        vAR_degree_item = ["0°","30°","45°","60°","90°"]
        ind=[0,1,2,3,4,5]
        vAR_degree_len = len(vAR_degree_item)
    #-----cylinder-------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_theta != "θ" and vAR_degree  != "°":
                    if vAR_theta == "Sin":
                        for i in range(0,5):
                            if vAR_degree == vAR_degree_item[i]:
                                st.success(vAR_sin[i])
                    if vAR_theta == "Cos":
                        for i in range(0,5):
                            if vAR_degree == vAR_degree_item[i]:
                                st.success(vAR_cos[i])
                    if vAR_theta == "Tan":
                        for i in range(0,5):
                            if vAR_degree == vAR_degree_item[i]:
                                st.success(vAR_Tan[i])
                    if vAR_theta == "Cot":
                        for i in range(0,5):
                            if vAR_degree == vAR_degree_item[i]:
                                st.success(vAR_cot[i])
                    if vAR_theta == "Sec":
                        for i in range(0,5):
                            if vAR_degree == vAR_degree_item[i]:
                                st.success(vAR_sec[i])
                    if vAR_theta == "Cosec":
                        for i in range(0,5):
                            if vAR_degree == vAR_degree_item[i]:
                                st.success(vAR_cosec[i])
                else:
                    st.error("Error")
                with col1:
                    st.write("# Result ")
