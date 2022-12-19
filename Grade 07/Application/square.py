import streamlit as vAR_st
import head
import clear as cr
def squarecube():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span> Application to find the square and cube.</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("## ")
        vAR_st.markdown("### Select")
    with col2:
        r=vAR_st.selectbox("",("Square","Cube"))
    if r=="Square":
        with col1:
            vAR_st.markdown("## ")
            vAR_st.markdown("### Enter here")
        with col2:
            b = vAR_st.number_input('',key='clear')
        with bc1:
            vAR_st.write("")
            if vAR_st.button("submit"):
                s=b**2
                with col1:
                    vAR_st.markdown("### ")
                    vAR_st.markdown("### Answer is")
                with col2:
                    vAR_st.write("")
                    vAR_st.success(s)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=cr.button_c)
    if r=='Cube':
        with col1:
            vAR_st.markdown("## ")
            vAR_st.markdown("### Enter here")
        with col2:
            c = vAR_st.number_input('',key='clear2')    
        with bc1:
            vAR_st.write("")
            if vAR_st.button("submit"):
                s=c**3
                with col1:
                    vAR_st.markdown("### ")
                    vAR_st.markdown("### Answer is")
                with col2:
                    vAR_st.write("")
                    vAR_st.success(s)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=cr.button_c)