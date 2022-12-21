import streamlit as vAR_st


def oddeven():
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    s1,col3,col4,s2=vAR_st.columns((6,2,2,6))

    with col2:
        k=vAR_st.selectbox("",("Select","Odd or Even","Quotient and remainder"))

    with col1:
        vAR_st.write('')
        vAR_st.subheader("Select the operation")

    if k=="Odd or Even":
        def cleartext():
            vAR_st.session_state["Clear"]=""
        with col1:
            vAR_st.write("")
            vAR_st.subheader("Enter the Number ")
        with col4:
            vAR_st.write("")
            vAR_st.write("")
            vAR_st.button("Clear", on_click=cleartext)

        with col2:
            vAR_num1=vAR_st.text_input("",key="Clear") 
    
        with col3:
            vAR_st.write("")
            vAR_st.write("")
            with col3:
                if vAR_st.button("Submit"):
                    with col2:
                        if vAR_num1.isnumeric():
                            vAR_num1=int(vAR_num1)
                            if vAR_num1 % 2 == 0:
                                vAR_st.write('')
                                vAR_st.subheader("The number is Even")
                                with col1:
                                    vAR_st.write("")
                                    vAR_st.subheader("Answer is ")
                            else:
                                vAR_st.write('')
                                vAR_st.subheader("The number is Odd")
                                with col1:
                                    vAR_st.write("")
                                    vAR_st.subheader("Answer is ")
                        else:
                            vAR_st.write('')
                            vAR_st.subheader("Enter a number")
                        

    if k =="Quotient and remainder":
        def cleartext2():
            vAR_st.session_state["Clear2"]=0
            vAR_st.session_state["Clear3"]=0
        with col1:
            vAR_st.write("")
            vAR_st.write("")
            vAR_st.subheader("Enter Input 1")
        with col1:
            vAR_st.write("")
            vAR_st.write("")
            vAR_st.subheader("Enter Input 2")
        with col4:
            vAR_st.write("")
            vAR_st.write("")
            vAR_st.button("Clear", on_click=cleartext2)
        with col2:
            vAR_st.write('')
            s=vAR_st.number_input("",key="Clear2")
            vAR_st.write('')
            t=vAR_st.number_input("",key="Clear3")
        
        with col2:
            vAR_st.write("")
            vAR_st.write("")
            with col3:
                vAR_st.write('')
                vAR_st.write('')
                if vAR_st.button("Submit"):
                    with col2:
                        try:
                            u,v=divmod(s,t)
                            vAR_st.subheader(u)
                            vAR_st.subheader(v)
                            with col1:
                                vAR_st.write('')
                                vAR_st.subheader("Quotient is")
                                vAR_st.write('')
                                vAR_st.subheader("Remainder is")
                            
                        except ZeroDivisionError:
                            with col2:
                                vAR_st.subheader("Cannot divide by zero")



