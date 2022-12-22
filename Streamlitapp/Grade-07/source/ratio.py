import streamlit as vAR_st
import math
import source.head as head


def cleartext():
        vAR_st.session_state["clr1"]=0
        vAR_st.session_state["clr2"]=0
def ratio():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find Ratio of two given numbers.</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("### ")
        vAR_st.markdown("### Enter Input 1")
        vAR_st.markdown("## ")
        vAR_st.markdown("### Enter Input 2")
    with col2:
        x=vAR_st.number_input("",key="clr1")
        y=vAR_st.number_input("",key="clr2")
    x=int(x)
    y=int(y)
    with bc1:
        if vAR_st.button("Submit"):
            try:
                z=str(int(int(round(x/(math.gcd(x,y)),0))))+':'+str(int(round(y/(math.gcd(x,y)),0)))
                with col1:
                    vAR_st.markdown("###")
                    vAR_st.markdown("### Ratio is")
                with col2:
                    vAR_st.write('')
                    vAR_st.success(z)
            except ZeroDivisionError:
                with col2:
                    vAR_st.subheader("Please enter the values")
    with bc2:
        vAR_st.button("Clear",on_click=cleartext)

