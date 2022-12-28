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
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Profit & Loss </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Cost Price ")
        st.markdown("### ")
        st.write("# Enter the Sell Price ")
        
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Cost"] = 0.00
            st.session_state["Clear_Selling"] = 0.00
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.number_input("",min_value=+0.00,step=1.0,key="Clear_Cost") 
        vAR_input_num_1=st.number_input("",min_value=+0.00,step=1.0,key="Clear_Selling")  
       
    #----- Average -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num and vAR_input_num_1 == int or float:
                    vAR_cost_price=vAR_input_num
                    vAR_selling_price=vAR_input_num_1
                    if (vAR_selling_price > vAR_cost_price):
                            vAR_profit = vAR_selling_price - vAR_cost_price
                            with col1:
                                st.write("# Profit ")
                            st.success(vAR_profit)
                    elif ( vAR_cost_price > vAR_selling_price):
                            vAR_loss = vAR_cost_price - vAR_selling_price
                            with col1:
                                st.write("# Loss ")
                            st.warning(vAR_loss)
                    else:
                        st.info("No Profit No Loss")
                else:
                    st.error("Error")
