import streamlit as vAR_st
from datetime import datetime
import datetime as dt
import time
def tyme():
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    w3,col3,col4,w4=vAR_st.columns((5,2,2,5))
    with col1:
        vAR_st.write("")
        vAR_st.write('')
        vAR_st.subheader("Select")
    with col2:
        sel=vAR_st.selectbox("",("Select","Standard time to railway time conversion","Railway time to standard time","Time interval"))
    def cleartext():
            vAR_st.session_state["clear"]=""
            vAR_st.session_state["clear2"]=""
            vAR_st.session_state["clear3"]=""
    if sel=="Standard time to railway time conversion":
        with col1:
            vAR_st.write("### ")
            vAR_st.subheader("Enter the time")
        with col2:
            vAR_m=vAR_st.text_input("",key="clear",placeholder="HH:MM AM/PM")

        with col3:
            vAR_st.subheader("")
            vAR_k=vAR_st.button("Submit")

        with col1:
            if vAR_k:
                try:
                    vAR_in_time = datetime.strptime(vAR_m, "%I:%M %p")
                    vAR_out_time = datetime.strftime(vAR_in_time, "%H:%M")
                
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### Converted time is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_out_time)
                except ValueError:
                    with col2:
                        vAR_st.info("Enter the time in 'HH:MM AM/PM' format")

        with col4:
            vAR_st.subheader("")
            vAR_st.button("Clear",on_click=cleartext)

    if sel=="Railway time to standard time":
        with col1:
            vAR_st.write("### ")
            vAR_st.subheader("Enter the time")
        with col2:
            vAR_m=vAR_st.text_input("",key="clear",placeholder="HH:MM")

        with col3:
            vAR_st.subheader("")
            vAR_k=vAR_st.button("Submit")

        with col1:
            if vAR_k:
                try:
                    vAR_in_time = datetime.strptime(vAR_m, "%H:%M" )
                    vAR_out_time = vAR_in_time.strftime("%I:%M %p")
                
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### Converted time is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_out_time)
                except ValueError:
                    with col2:
                        vAR_st.info("Enter the time in 'HH:MM' format")

        with col4:
            vAR_st.subheader("")
            vAR_st.button("Clear",on_click=cleartext)


    if sel=="Time interval":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        with col1:
            vAR_st.write('')
            vAR_st.write("")
            vAR_st.subheader("Select the operation")
        with col2:
            sel2=vAR_st.selectbox("",("Add time","Subract time"))
        if sel2=="Add time":
            w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
            w3,col3,col4,w4=vAR_st.columns((5,2,2,5))
            with col1:
                vAR_st.write('')
                vAR_st.write('')
                vAR_st.subheader("Time 1")
                vAR_st.write('### ')
                vAR_st.subheader("Time 2")
            with col2:
                vAR_t1=vAR_st.text_input("",key="clear2",placeholder="HH:MM")
                vAR_t2=vAR_st.text_input("",key="clear3",placeholder="HH:MM")

            with col3:   
                vAR_st.write("") 
                if vAR_st.button("submit"):
                    try:
                        t1 = dt.datetime.strptime(vAR_t1, '%H:%M')
                        t2 = dt.datetime.strptime(vAR_t2, '%H:%M')
                        vAR_time_zero = dt.datetime.strptime('00:00', '%H:%M')
                        vAR_ad=(t1 - vAR_time_zero + t2).time()
                        with col1:
                            vAR_st.write('')
                            vAR_st.subheader("Result")
                        with col2:
                            vAR_st.write('')
                            vAR_st.success(vAR_ad)
                    except ValueError:
                        with col2:
                            vAR_st.info("Enter the time in 'HH:MM' format")
            with col4:
                    vAR_st.write("")
                    vAR_st.button("Clear",on_click=cleartext)

        if sel2=="Subract time":
            w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
            w3,col3,col4,w4=vAR_st.columns((5,2,2,5))
            with col1:
                vAR_st.write('')
                vAR_st.write('')
                vAR_st.subheader("Time 1")
                vAR_st.write('### ')
                vAR_st.subheader("Time 2")
            with col2:
                vAR_t1=vAR_st.text_input("",key="clear2",placeholder="HH:MM")
                vAR_t2=vAR_st.text_input("",key="clear3",placeholder="HH:MM")
                
            with col3:
                vAR_st.write("")
                if vAR_st.button("submit"):
                    try:
                        time_1 = dt.datetime.strptime(vAR_t1,"%H:%M")
                        time_2 = dt.datetime.strptime(vAR_t2,"%H:%M")
                        time_interval = time_1 - time_2
                        with col1:
                            vAR_st.write("")
                            vAR_st.write('')
                            vAR_st.subheader("Result")
                        with col2:
                            vAR_st.write('')
                            vAR_st.write('')
                            vAR_st.success(time_interval)
                    except ValueError:
                        with col2:
                            vAR_st.info("Enter the time in 'HH:MM' format")
            with col4:
                    vAR_st.write("")
                    vAR_st.button("Clear",on_click=cleartext)


    


    

