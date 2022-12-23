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
def profit_or_loss():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to Find the Profit & Loss </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,2.5,2.8,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Cost Price ")
        st.markdown("### ")
        st.write("# Enter the Selling Price ")
        
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Cost"] = ""
            st.session_state["Clear_Selling"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",key="Clear_Cost") 
        vAR_input_num_1=st.text_input("",key="Clear_Selling")  
       
    #----- Average -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num and vAR_input_num_1.isnumeric():
                    cost_price=int(vAR_input_num)
                    selling_price=int(vAR_input_num_1)
                    if (selling_price > cost_price):
                            profit = selling_price - cost_price
                            with col1:
                                st.write("# Profit ")
                            st.markdown("")
                            st.success(profit)
                    elif ( cost_price > selling_price):
                            loss = cost_price - selling_price
                            with col1:
                                st.write("# Loss ")
                            st.markdown("")
                            st.warning(loss)
                    else:
                        st.markdown("")
                        st.info("No Profit No Loss")
                else:
                    st.markdown("")
                    st.error("Error")
