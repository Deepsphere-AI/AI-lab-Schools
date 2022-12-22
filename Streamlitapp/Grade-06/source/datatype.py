#Program to find the data type
import streamlit as vAR_st
def clear_text():
        vAR_st.session_state["clear"]=""
        vAR_st.session_state["Clear8"]="Data type"
        vAR_st.session_state["Clear9"]="Libraries"
def datatype():
    #vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'>Application to find the data type</h1>", unsafe_allow_html=True)
    col7, col1, col2, col8 = vAR_st.columns((1,2,2,1))
    with col2:
        vAR_st.write('')
        vAR_name = vAR_st.text_input("",key="clear",placeholder="Eg: HELLO, 20 or 20.2")
    
    with col1:
        vAR_st.write("")
        vAR_st.write("")
        vAR_st.write('')
        vAR_st.subheader("ㅤㅤEnter Input here  ","")
    
    col9, col3, col4, col10 = vAR_st.columns((1,2,2,1))
    col11,col5,col6,col12= vAR_st.columns((5,2,2,5))

    with col5:
        k = vAR_st.button("Submit")
    
    
    
    with col6:
        vAR_st.button("clear",on_click=clear_text)
        
    def findtype():
        if vAR_name.isnumeric():
                with col3:
                    vAR_st.subheader("Entered Input is an")
                with col4:
                    vAR_st.subheader("Integer","")

        elif vAR_name.isalnum()==True:
            with col4:
                vAR_st.subheader("Enter a Valid Input","")

        
        elif "." in vAR_name:
                vAR_a=vAR_name.split(".")
                try:
                    vAR_b = int(vAR_a[0])
                    vAR_c = int(vAR_a[1])
                    with col3:
                        vAR_st.subheader("Entered Input is a")
                    with col4:
                        vAR_st.subheader("Float","")
                except:
                    with col4:
                        vAR_st.subheader("Enter a valid input","")
        
        else:
            if vAR_name.isalpha()==True:
                with col3:
                    vAR_st.subheader("Entered Input is a")
                    with col4:
                        vAR_st.subheader("String","")

    if k:
        if vAR_name=="":
            with col2:
                vAR_st.subheader("Enter a value")
        if vAR_name!="":
            findtype()
