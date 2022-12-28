import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
import source.title_1 as head
def cal_GST():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to GST Calculator </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Price ")
        st.markdown("")
        st.markdown("")
        st.write("# GST in % ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_price"] = 0
            st.session_state["clear_gst"] = 0
        st.button("Clear", on_click=clear_text)   
    with col2:  
        vAR_input_sellingprice=st.number_input("",min_value=0.00,step=1.0,key="Clear_price")
        vAR_gst_rate=st.number_input("",min_value=0.00,step=1.0,key="clear_gst")
    #----- Date to Day -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if  vAR_input_sellingprice !='':
                    vAR_input_sellingprice=int(vAR_input_sellingprice)
                    vAR_Cgst=vAR_input_sellingprice*(vAR_gst_rate/2)/100
                    vAR_Sgst=vAR_Cgst
                    vAR_18= vAR_Cgst+vAR_Sgst
                    vAR_total=vAR_input_sellingprice + vAR_Cgst + vAR_Sgst
                    vAR_total=round(vAR_total,4)
                    #st.success(vAR_18)
                    st.markdown("")
                    st.success(vAR_total)
                else:
                    st.markdown("### ")
                    st.error("Error")
                with col1:  
                    st.write("# Amount Payable   ")
