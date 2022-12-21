import streamlit as st
from streamlit_option_menu import option_menu


def tables():
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((5,2,2,5))
    with col1:
        st.write("")
        st.write("")
        st.subheader("Enter the Number ")
  
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
                st.session_state["text"] = ""
        st.button("Clear", on_click=clear_text) 
    # ---------input button----------#
    with col2:
        st.markdown("")
        vAR_input_number=st.text_input("",key="text")
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                st.markdown("")
                if vAR_input_number.isnumeric():
                    vAR_num=int(vAR_input_number)
                    for i in range(1,11):
                        x=vAR_num, 'x', i, "=" ,vAR_num*i
                        x=','.join(str(item) for item in x)
                        y=x.replace(",","")  
                        st.subheader(y)
                    with col1:
                        st.subheader("ㅤㅤㅤTables are ")
                elif vAR_input_number==str(vAR_input_number):
                    st.subheader("Enter a number")
                else:
                    st.subheader("Enter a number")
                
