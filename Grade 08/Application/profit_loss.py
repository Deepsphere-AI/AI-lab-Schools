import streamlit as st
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
from title_1 import *
from img import *
with open('final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
def profit_or_loss():
    image()
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Application to Find the Profit or Loss</h1>", unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,1.5,1.8,6))
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
            st.session_state["text"] = ""
            st.session_state["text1"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",key="text") 
        vAR_input_num_1=st.text_input("",key="text1")  
       
    #----- Average -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num and vAR_input_num_1 != 0:
                    cost_price=int(vAR_input_num)
                    selling_price=int(vAR_input_num_1)
                    if (selling_price > cost_price):
                            profit = selling_price - cost_price
                            with col1:
                                st.write("# Profit ")
                            st.success(profit)
                    elif ( cost_price > selling_price):
                            loss = cost_price - selling_price
                            with col1:
                                st.write("# Loss ")
                            st.warning(loss)
                    else:
                        st.info("No Profit No Loss")
                else:
                    st.error("Error")
               
                
