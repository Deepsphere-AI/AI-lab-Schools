import streamlit as vAR_st
import numpy as np
import head
import statistics as sts
from scipy import stats
import clear as cr

def mean(vAR_a):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1)) 
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))   
    vAR_c=[]
    vAR_sum=0
    vAR_b=vAR_a.split(",")   
    with bc1:
        vAR_st.write("") 
        if vAR_st.button("submit"):
            for i in vAR_b:
                if i.isnumeric():
                    vAR_c.append(int(i))
            for i in vAR_c:
                vAR_sum=vAR_sum+i
            vAR_mean=vAR_sum/len(vAR_c)
            with col1:
                vAR_st.markdown("### Answer is")
            with col2:
                vAR_st.success(vAR_mean)
            with bc2:
                vAR_st.write("")
                vAR_st.button("Clear", on_click=cr.button_rad)


def median(vAR_a):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    vAR_c=[]
    vAR_b=vAR_a.split(",")   
    with bc1:
        vAR_st.write("")  
        if vAR_st.button("submit"):
            for i in vAR_b:
                if i.isnumeric():
                    vAR_c.append(int(i))
            vAR_med=np.median(vAR_c)
            with col1:
                vAR_st.markdown("### Answer is")
            with col2:
                vAR_st.success(vAR_med)
            with bc2:
                vAR_st.write("")
                vAR_st.button("Clear", on_click=cr.button_rad)

def mode(vAR_a):
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    vAR_c=[]
    vAR_b=vAR_a.split(",")   
    with bc1:
        vAR_st.write("")  
        if vAR_st.button("submit"):
            for i in vAR_b:
                if i.isnumeric():
                    vAR_c.append(int(i))
            vAR_mod=max(set(vAR_c),key=vAR_c.count)
            with col1:
                vAR_st.markdown("### Answer is")
            with col2:
                vAR_st.success(vAR_mod)
            with bc2:
                vAR_st.write("")
                vAR_st.button("Clear", on_click=cr.button_rad)

def stat():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Mean,Median and Mode</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    w1,c1,c2,w2=vAR_st.columns((1,2,2,1))
    with c1:
        vAR_st.markdown("### ")
        vAR_st.markdown("### Enter the data")
        vAR_st.markdown("### ")
        vAR_st.markdown("### Select")
    with c2:
        vAR_a=vAR_st.text_input("",key="mean_in")
        vAR_r=vAR_st.selectbox("",["Mean","Median","Mode"],key="mmm")
    if vAR_r=="Mean":
        mean(vAR_a)
    if vAR_r=="Median":
        median(vAR_a)
    if vAR_r=="Mode":
        mode(vAR_a)

