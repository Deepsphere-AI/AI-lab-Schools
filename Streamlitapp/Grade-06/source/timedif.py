import streamlit as vAR_st
import datetime as dt
import pendulum
import time

w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
with col1:
    vAR_st.markdown("### ")
    vAR_st.markdown("### Enter the time")
    vAR_st.markdown("## ")
    vAR_st.markdown("### Enter the time to add")
with col2:
    vAR_t1=vAR_st.text_input("",key="time_in",placeholder="HH:MM")
    vAR_t2=vAR_st.text_input("",key="time_in2",placeholder="HH:MM")
    
    if vAR_st.button("submit"):
        time_1 = dt.datetime.strptime(vAR_t1,"%H:%M")
        time_2 = dt.datetime.strptime(vAR_t2,"%H:%M")
        time_interval = time_1 - time_2
        with col1:
            vAR_st.markdown("### Answer is")
        with col2:
            vAR_st.success(time_interval)
