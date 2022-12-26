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
        vAR_name = vAR_st.text_input("",key="clear")
    
    with col1:
        vAR_st.write("")
        vAR_st.write("")
        vAR_st.write('')
        vAR_st.subheader("Enter Input here")
    
    col9, col3, col4, col10 = vAR_st.columns((1,2,2,1))
    col11,col5,col6,col12= vAR_st.columns((5,2,2,5))

    with col5:
        k = vAR_st.button("Submit")
    
    
    
    with col6:
        vAR_st.button("clear",on_click=clear_text)
        
    def findtype():
        if vAR_name.isnumeric():
                with col3:
                    vAR_st.subheader("Data type")
                with col4:
                    vAR_st.success("Integer")

        elif vAR_name.isalpha()==True:
                with col3:
                    vAR_st.subheader("Data type")
                    with col4:
                        vAR_st.success("String")
        
        
        
        

        
        elif "." in vAR_name:
                vAR_a=vAR_name.split(".")
                if len(vAR_a)==2:
                    try:
                        vAR_b = int(vAR_a[0])
                        vAR_c = int(vAR_a[1])
                        with col3:
                            vAR_st.subheader("Data type")
                        with col4:
                            vAR_st.success("Float")
                    except:
                        with col4:
                            vAR_st.info("Enter a valid input")

                else:
                    with col4:
                        vAR_st.info("Enter a valid input")
                 
        
        elif vAR_name.isalnum()==True:
            with col4:
                vAR_st.info("Enter a Valid Input")

        else:
            with col4:
                vAR_st.info("Enter a Valid Input")

            

    if k:
        if vAR_name=="":
            with col2:
                vAR_st.info("Enter a value")
        if vAR_name!="":
            findtype()

