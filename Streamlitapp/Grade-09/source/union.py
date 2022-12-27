import streamlit as vAR_st
import source.title_1 as head
def clr_ins():
    vAR_st.session_state['set1']=""
    vAR_st.session_state['set2']=""
def union(a,b):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    a=a.split(",")
    b=b.split(",")
    c=set(a)
    d=set(b)
    with bc1:
        vAR_st.write("")
        vAR_button=vAR_st.button("Submit") 
        if vAR_button:
            try:
                if a=="" or b=="":
                        with col2:
                            vAR_st.info("Enter the values separated by comma")
                else:
                    z = c.union(d)
                    with col2:
                        vAR_st.success(z)
            except BaseException as er:
                with col2:
                    vAR_st.info("Invalid input")
    with bc2:
        vAR_st.write("")
        vAR_st.button("Clear", on_click=clr_ins)
def intersec(a,b):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))  
    a=a.split(",")
    b=b.split(",")
    c=set(a)
    d=set(b)
    with bc1:
        vAR_st.write("")
        vAR_button=vAR_st.button("Submit") 
        if vAR_button:
            try:
                if a=="" or b=="":
                        with col2:
                            vAR_st.info("Enter the values separated by comma")
                else:
                    y = c.intersection(d)
                    with col2:
                        vAR_st.success(y)
            except BaseException as er:
                with col2:
                    vAR_st.info("Invalid input")
    with bc2:
        vAR_st.write("")
        vAR_st.button("Clear", on_click=clr_ins)

def uni_int():
    head.title()
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        
    with col1:
        vAR_st.markdown("### ")
        vAR_st.markdown("### Set A")
        
        vAR_st.markdown("## ")
        vAR_st.markdown("### Set B")
    with col2:
        a=vAR_st.text_input("",key='set1',placeholder="eg. 21,25,27,20,24,21,46")
        b=vAR_st.text_input("",key='set2',placeholder="eg. 21,25,27,20,24,21,46")
    w1,c1,c2,w2=vAR_st.columns((1,2,2,1))
    with c1:
        vAR_st.markdown("### ")
        vAR_st.markdown("### Select")
    with c2:
        selected=vAR_st.selectbox('',['Union','Intersection'])
    if selected=="Union":
        union(a,b)
    if selected=="Intersection":
        intersec(a,b)

