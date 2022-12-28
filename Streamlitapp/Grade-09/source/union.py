import streamlit as vAR_st
import source.title_1 as head
def clr_ins():
    vAR_st.session_state['set1']=""
    vAR_st.session_state['set2']=""
def union(a,b):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))
    e=a.split(",")
    f=b.split(",")
    c=set(e)
    d=set(f)
    with bc1:
        vAR_st.write("")
        vAR_button=vAR_st.button("Submit") 
        if vAR_button:
            try:
                if b=="" or a=='':
                    with col2:
                        vAR_st.info("Enter the values separated by comma")
                else:
                    z = c.union(d)
                    if z=='':
                        with col2:
                            vAR_st.info("Enter the input")                           
                    else:
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
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))  
    e=a.split(",")
    f=b.split(",")
    c=set(e)
    d=set(f)
    with bc1:
        vAR_st.write("")
        vAR_button=vAR_st.button("Submit") 
        if vAR_button:
            try:
                if b=="" or a=='':
                    with col2:
                        vAR_st.info("Enter the values separated by comma")
                else:
                    y = c.intersection(d)
                    if y:
                        with col2:
                            vAR_st.success(y)
                         
                    else:
                        with col2:
                            vAR_st.info("No Intersection")
            except BaseException as er:
                with col2:
                    vAR_st.info("Invalid input")
    with bc2:
        vAR_st.write("")
        vAR_st.button("Clear", on_click=clr_ins)

def uni_int():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Union and Intersection </p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))
        
    with col1:
        vAR_st.markdown("## ")
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

