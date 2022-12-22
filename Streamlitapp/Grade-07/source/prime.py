import streamlit as vAR_st
import source.fun_palin as fpp
import source.clear as cr
import source.head as head

def primeornot():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the given number is prime number or not a prime number</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.write("")
        vAR_st.markdown("### Enter the number")
    with col2:
        a=vAR_st.number_input("",key="prime_in")
    b=int(a)
    vAR_ans=fpp.prime(b)
    with bc1:
        vAR_st.markdown("### ")
        if vAR_st.button("submit"):
            if b!=0: 
                if vAR_ans=='prime number':
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is ")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_ans)
                    with bc2:
                        vAR_st.markdown("### ")
                        vAR_st.button("Clear", on_click=cr.button_sq)
                else:
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is ")
                    with col2:
                        vAR_st.write("")
                        vAR_st.warning(vAR_ans)
                    with bc2:
                        vAR_st.markdown("### ")
                        vAR_st.button("Clear", on_click=cr.button_sq)
            else:
                with col1:
                    vAR_st.markdown("### ")
                    vAR_st.markdown("### Answer is ")
                with col2:
                    vAR_st.write("")
                    vAR_st.success("composite")
                with bc2:
                        vAR_st.markdown("### ")
                        vAR_st.button("Clear", on_click=cr.button_sq)