import streamlit as vAR_st

def numrange():
    col1,col2,col3,col4=vAR_st.columns((1,2,2,1))
    col5,col6,col7,col8=vAR_st.columns((5,2,2,5))
    with col6:
        vAR_k=vAR_st.button("Submit")
    with col2:
        vAR_st.write("")
        vAR_st.write('')
        vAR_st.subheader("Select your operation")
    with col3:
        vAR_sel=vAR_st.selectbox("",("Select","Within a range","Even within a range",
        "Odd within a range","Interval 3 within a range"),key="clear")
    if vAR_sel=="Within a range":
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter numbers from")
        with col3:
            vAR_num=int(float(vAR_st.number_input("")))
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter numbers upto")
        with col3:
            vAR_num2=int(float(vAR_st.number_input("",key="gs")))
        vAR_s=""
        for i in range(vAR_num,vAR_num2+1):
            vAR_s=vAR_s+str(i)+","
        vAR_ans=""
        for j in range(len(vAR_s)-1):
            vAR_ans=vAR_ans+vAR_s[j]
        if vAR_k:
            with col3:
                vAR_st.subheader(vAR_ans)
        
    if vAR_sel=="Even within a range":
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter the number")
        with col3:
            vAR_num=int(float(vAR_st.number_input("")))
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter numbers upto")
        with col3:
            vAR_num2=int(float(vAR_st.number_input("",key="g")))
        vAR_s=""
        for i in range(vAR_num,vAR_num2+1):
            if i%2==0:
                vAR_s=vAR_s+str(i)+","
        vAR_ans=""
        for j in range(len(vAR_s)-1):
            vAR_ans=vAR_ans+vAR_s[j]
        if vAR_k:
            with col3:
                vAR_st.subheader(vAR_ans)

    if vAR_sel=="Odd within a range":
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter the number")
        with col3:
            vAR_num=int(float(vAR_st.number_input("")))
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter numbers upto")
        with col3:
            vAR_num2=int(float(vAR_st.number_input("",key="ws")))
        vAR_s=""
        for i in range(vAR_num,vAR_num2+1):
            if i%2!=0:
                vAR_s=vAR_s+str(i)+","
        vAR_ans=""
        for j in range(len(vAR_s)-1):
            vAR_ans=vAR_ans+vAR_s[j]
        if vAR_k:
            with col3:
                vAR_st.subheader(vAR_ans)

    if vAR_sel=="Interval 3 within a range":
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter the number")
        with col3:
            vAR_num=int(float(vAR_st.number_input("")))
        with col2:
            vAR_st.write('')
            vAR_st.subheader("Enter numbers upto")
        with col3:
            vAR_num2=int(float(vAR_st.number_input("",key="ls")))
        vAR_s=""
        for i in range(vAR_num,vAR_num2+1,3):
            vAR_s=vAR_s+str(i)+","
        vAR_ans=""
        for j in range(len(vAR_s)-1):
            vAR_ans=vAR_ans+vAR_s[j]
        if vAR_k:
            with col3:
                vAR_st.subheader(vAR_ans)

    def cleartext():
        vAR_st.session_state["clear"]="Select"

    with col7:
        vAR_st.button("Clear",on_click=cleartext)




