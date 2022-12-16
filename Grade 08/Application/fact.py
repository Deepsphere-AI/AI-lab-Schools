import streamlit as vAR_st
import head
import clear as cr

def factorial():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the factorial of given number</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    
    col1,col2=vAR_st.columns((2,2))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("###" )
        vAR_st.markdown("### Enter the Number")
    with col2:
        b=vAR_st.number_input("",key="fact_in")
        a=int(b)
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    with bc1:
        vAR_st.markdown("### ")
        if vAR_st.button("Submit"):
            with col1:
                vAR_st.markdown("### ")
                vAR_st.markdown("### Answer is")
            with col2:
                vAR_st.write("")
                vAR_st.success(fact)
            with bc2:
                vAR_st.markdown("### ")
                vAR_st.button("Clear", on_click=cr.button_sq)