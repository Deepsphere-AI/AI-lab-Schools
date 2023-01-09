import streamlit as vAR_st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

def tables():
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((5,2,2,5))
    with col1:
        vAR_st.write("###")
        vAR_st.write("###")
        vAR_st.subheader("Enter the Number ")
  
    with bc2:
        vAR_st.markdown("")
        vAR_st.markdown("")
        def clear_text():
                vAR_st.session_state["text"] = ""
        vAR_st.button("Clear", on_click=clear_text) 
    # ---------input button----------#
    with col2:
        vAR_st.markdown("")
        vAR_input_number=vAR_st.text_input("",key="text",placeholder= "Eg: 3")
    with bc1:
        vAR_st.markdown("")
        vAR_st.markdown("")
        if vAR_st.button("Submit"):
            with col2:
                vAR_st.markdown("")
                if vAR_input_number.isnumeric():
                    vAR_num=int(vAR_input_number)
                    df=[]
                    for i in range(1,11):
                        vAR_x=vAR_num, 'x', i, "=" ,vAR_num*i   #"4,x,1,=,4"
                        vAR_x=','.join(str(item) for item in vAR_x)
                        tab=vAR_x.split(",")
                        df.append(tab)
                        hide_table_row_index = """
                            <style>
                            thead tr:first-child, thead th:first-child {display:none}
                            tr th{display:none}
                            </style>
                            """
                    vAR_st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    
                    
                    vAR_st.table(df)

                    with col1:
                        vAR_st.subheader("ㅤㅤㅤTables")
                elif "." in vAR_input_number:
                    vAR_st.info("Enter a whole number")
                elif vAR_input_number==str(vAR_input_number):
                    vAR_st.info("Enter a number")
                else:
                    vAR_st.info("Enter a number")


                
