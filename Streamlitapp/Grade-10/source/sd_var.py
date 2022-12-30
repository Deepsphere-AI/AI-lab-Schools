import streamlit as vAR_st
import statistics as sts
import source.title_1 as head

def to_clr():
    vAR_st.session_state['sdvr']="Standard Deviation"
    vAR_st.session_state['sd_in']=""

def sd(x):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1)) 
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))   
    vAR_c=[]
    vAR_b=x.split(",")
    with bc1:
        vAR_st.write("")  
        if vAR_st.button("submit"):
            try:
                if x=="":
                    with col2:
                        vAR_st.info("Enter the values separated by comma")
                else:
                    for i in vAR_b:
                        vAR_c.append(float(i))
                    standard_deviation = sts.stdev(vAR_c)
                    with col1:
                        standard_deviation=round(standard_deviation,4)
                        vAR_st.write("")
                        vAR_st.markdown("### Result")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(standard_deviation)
            except BaseException as er:
                with col2:
                    vAR_st.info("Invalid input")
        with bc2:
            vAR_st.write("")
            vAR_st.button("Clear", on_click=to_clr)
                    
def var(x):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1)) 
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))   
    vAR_c=[]
    
    
    vAR_b=x.split(",")
    with bc1:
        vAR_st.write("")  
        if vAR_st.button("submit"):
            try:
                if x=="":
                    with col2:
                        vAR_st.info("Enter the values separated by comma")
                else:
                    for i in vAR_b:
                        vAR_c.append(float(i))
                    vari=sts.variance(vAR_c)
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### Varience")
                    with col2:
                        vari=round(vari,4)
                        vAR_st.write("")
                        vAR_st.success(vari)
            except BaseException as er:
                with col2:
                    vAR_st.info("Invalid input")
        with bc2:
            vAR_st.write("")
            vAR_st.button("Clear", on_click=to_clr)

def stats():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Standard deviation and Varience</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    w1,c1,c2,w2=vAR_st.columns((1,2,2,1))
    with c1:
        
        vAR_st.markdown("### ")
        vAR_st.markdown("### Enter the data")
        
        vAR_st.markdown("## ")
        vAR_st.markdown("### Select")
    with c2:
        vAR_a=vAR_st.text_input("",key="sd_in",placeholder="eg. 21,25,27,20,24,21,46")
        vAR_r=vAR_st.selectbox("",["Standard Deviation","Varience"],key="sdvr")
    if vAR_r=="Standard Deviation":
        sd(vAR_a)
    if vAR_r=="Varience":
        var(vAR_a)
#stats()