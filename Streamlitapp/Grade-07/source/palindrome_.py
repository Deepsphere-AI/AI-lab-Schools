import streamlit as vAR_st
import source.clear as cr
import source.head as head
import source.fun_palin as fpp
def palindrome():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the given input is palindrome or not.</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("## ")
        vAR_st.markdown("### Enter the string")
    with col2:
        b=vAR_st.text_input("",key='palin_in')
    vAR_pal=fpp.palin(b)
    with bc1:
        vAR_st.markdown("### ")
        vAR_button=vAR_st.button("Submit") 
        if vAR_button:
            if len(b)>1:
                if " " not in b:
                    if vAR_pal=="is palindrome":
                        with col1:
                            vAR_st.markdown("## ")
                            vAR_st.markdown("### Answer is")
                        with col2:
                            vAR_st.write("")
                            vAR_st.success(vAR_pal)      
                    else:
                        with col1:
                            vAR_st.markdown("## ")
                            vAR_st.markdown("### Answer is ")
                        with col2:
                            vAR_st.write("")
                            vAR_st.warning(vAR_pal)   
                else:
                    with col2:
                        vAR_st.write("")
                        vAR_st.error("Enter the string without space")
            else:
                with col2:
                    vAR_st.markdown("## ")
                    vAR_st.info(" Invalid input")
    with bc2:
        vAR_st.markdown("### ")
        vAR_st.button("Clear", on_click=cr.button_sq)