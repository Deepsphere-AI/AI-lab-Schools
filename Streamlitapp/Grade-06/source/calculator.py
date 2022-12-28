#Arithmetic calculator
import streamlit as vAR_st
def calculator():
    #vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'>Calculator</h1>", unsafe_allow_html=True)
    
    def add(a,b):
        c=a+b
        vAR_st.write('')
        vAR_st.write('')
        if vAR_k:
            vAR_st.success(c)
    
    def subract(a,b):
        c=a-b
        vAR_st.write('')
        vAR_st.write('')
        if vAR_k:
            vAR_st.success(c)
    
    def multiply(a,b):
        c=a*b
        vAR_st.write('')
        vAR_st.write('')
        if vAR_k:
            vAR_st.success(c)
    
    def divide(a,b):
        try:
            c=a/b
            vAR_st.write('')
            vAR_st.write('')
            if vAR_k:
                vAR_st.success(c)
        except ZeroDivisionError:
            vAR_st.write('')
            vAR_st.write('')
            if vAR_k:
                vAR_st.info("Cannot divide by zero")
        
    def cleartext():
        vAR_st.session_state["Clear1"]=0
        vAR_st.session_state["Clear2"]=0
        vAR_st.session_state["Clear3"]= "Select"
        
    def answer():
        with col4:
            vAR_st.write('')
            vAR_st.write('')
            if vAR_k:
                vAR_st.subheader("Result")
            

    col7,col1,col2,col8= vAR_st.columns((1,2,2,1))
    col3,col4,col5,col6 = vAR_st.columns((1,2,2,1))
    col9,col10,col11,col12= vAR_st.columns((5,2,2,5))

    with col10:
        vAR_st.write('')
        vAR_k=vAR_st.button('Submit')
    
    
    with col4:
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader('Arithmetic operation ')
    
    
    with col5:
        vAR_sel=vAR_st.selectbox('',("Select","Add","Subract","Multiply","Divide"),key="Clear3")

    
            
    
    with col1:
        vAR_st.write('##')
        vAR_st.subheader("Enter number 1 ") 
        vAR_st.write('###')  
        vAR_st.subheader("Enter number 2 ")
        
    with col2:
        num1=vAR_st.number_input("",key="Clear1")
        num2=vAR_st.number_input("",key="Clear2")

    if vAR_k:
        if vAR_sel=="Select":
            if num1 and num2!=0:
                with col5:
                    vAR_st.info("Select the operation")
            else:
                with col5:
                    vAR_st.info("Enter two Numbers")

    with col5:
        if vAR_sel=="Add":
            answer()
            with col5:
                add(num1,num2)
    
    with col5:
        if vAR_sel=="Subract":
            answer()
            with col5:
                subract(num1,num2)
    
    with col5:
        if vAR_sel=="Multiply":
            with col4:
                answer()
            with col5:
                multiply(num1,num2)

    with col5:
        if vAR_sel=="Divide":
            answer()
            with col5:
                divide(num1,num2)

    with col11:
        vAR_st.write('')
        vAR_st.button("Clear",on_click=cleartext)

