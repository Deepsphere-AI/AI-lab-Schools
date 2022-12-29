import streamlit as vAR_st
import source.title_1 as head
#import source.frustum as fstm    copy this to app
def clr_num():
    vAR_st.session_state['radi1']=0
    vAR_st.session_state['radi2']=0
    vAR_st.session_state['height']=0
def csa(x,y,z):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))
    pi=3.14
    with bc1:
        vAR_st.write("")
        if vAR_st.button("Submit"):
            try:
                s=pi*(x+y)*z
                with col1:
                    vAR_st.markdown("### CSA is")
                with col2:
                    s=round(s,2)
                    vAR_st.success(str(s)+" sq units")
            except BaseException as er:
                vAR_st.info(er)
    with bc2:
        vAR_st.write("")
        vAR_st.button("Clear", on_click=clr_num)
    
def vol(x,y,z):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))
    pi=3.14
    with bc1:
        vAR_st.write("")
        if vAR_st.button("Submit"):
            try:
                s=(pi*z)/3 *(x**2 + x*y + y**2)
                with col1:
                    vAR_st.markdown("### Volume is")
                with col2:
                    s=round(s,2)
                    vAR_st.success(str(s)+" cu.units")
            except BaseException as er:
                vAR_st.info(er)
    with bc2:
        vAR_st.write("")
        vAR_st.button("Clear", on_click=clr_num)
def frustum():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the volume and corved surface area of frustum</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    #us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))
    with col1:
        vAR_st.markdown("## ")
        vAR_st.markdown("### Radius 1")        
        vAR_st.markdown("## ")
        vAR_st.markdown("### Radius 2")
        vAR_st.markdown("### ")
        vAR_st.markdown("### Height")
        
    with col2:
        a=vAR_st.number_input("",key='radi1',min_value=0.00)
        b=vAR_st.number_input("",key='radi2',min_value=0.00)
        h=vAR_st.number_input("",key='height',min_value=0.00)
        leng=h**2 + (a-b)**2
        c=leng**0.5
    with col1:
        vAR_st.markdown("## ")
        vAR_st.markdown("### Select")
    with col2:
        selected=vAR_st.selectbox('',['curved Surface Area','Volume'])
    if selected=="curved Surface Area":
        csa(a,b,c)
    if selected=="Volume":
        vol(a,b,c)
# frustum()
