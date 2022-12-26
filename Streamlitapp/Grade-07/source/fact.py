import streamlit as vAR_st
import source.head as head
import source.clear as cr

def factorial():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the factorial of given number</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("##" )
        vAR_st.markdown("### Enter the Number")
    with col2:
        b=vAR_st.text_input("",key="fact_in")
    with bc1:
        vAR_st.markdown("### ")
        if vAR_st.button("Submit"):
            if b.isnumeric():
                a=int(b)
                if a<=100:
                    fact=1
                    for i in range(1,a+1):
                        fact=fact*i
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(fact)
                else:
                    with col2:
                        vAR_st.info("Enter the input below 100")
            else:
                with col2:
                    vAR_st.info("Invalid input")
                    vAR_st.info("Enter only numeric values")
        with bc2:
            vAR_st.markdown("### ")
            vAR_st.button("Clear", on_click=cr.button_sq)
            