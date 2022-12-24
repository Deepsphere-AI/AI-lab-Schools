import streamlit as vAR_st


def oddeven():
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    s1,col3,col4,s2=vAR_st.columns((5,2,2,5))

    

  

   
    def cleartext():
        vAR_st.session_state["Clear"]=""
    with col1:
        vAR_st.write("")
        vAR_st.write('')
        vAR_st.subheader("Enter the Number ")
    with col4:
        vAR_st.write("")
        vAR_st.write("")
        vAR_st.button("Clear", on_click=cleartext)

    with col2:
        vAR_num1=vAR_st.text_input("",key="Clear",placeholder="Eg: 3") 

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
                            vAR_st.success("The number is Even")
                            with col1:
                                vAR_st.write("")
                                vAR_st.subheader("Result")
                        else:
                            vAR_st.write('')
                            vAR_st.success("The number is Odd")
                            with col1:
                                vAR_st.write("")
                                vAR_st.subheader("Result")
                    else:
                        vAR_st.write('')
                        vAR_st.info("Enter a number")
                        

    


