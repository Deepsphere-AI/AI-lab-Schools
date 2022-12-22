import streamlit as st

def numrange():
    col1,col2,col3,col4=st.columns((1,2,2,1))
    col5,col6,col7,col8=st.columns((5,2,2,5))
    with col6:
        k=st.button("Submit")
    with col2:
        st.write("")
        st.subheader("Select your operation")
    with col3:
        sel=st.selectbox("",("Select","Print numbers 0 to given range","Print the even numbers from 0 to given range",
        "Print the odd numbers from 0 to given range","Print the numbers with a difference of three from 0 to given range"),key="clear")
    if sel=="Print numbers 0 to given range":
        with col2:
            st.write('')
            st.subheader("Enter the number")
        with col3:
            num=int(float(st.number_input("")))
        s=""
        for i in range(1,num+1):
            s=s+str(i)+","
        ans=""
        for j in range(len(s)-1):
            ans=ans+s[j]
        if k:
            with col3:
                st.subheader(ans)
        
    if sel=="Print the even numbers from 0 to given range":
        with col2:
            st.write('')
            st.subheader("Enter the number")
        with col3:
            num=int(float(st.number_input("")))
        s=""
        for i in range(1,num+1):
            if i%2==0:
                s=s+str(i)+","
        ans=""
        for j in range(len(s)-1):
            ans=ans+s[j]
        if k:
            with col3:
                st.subheader(ans)

    if sel=="Print the odd numbers from 0 to given range":
        with col2:
            st.write('')
            st.subheader("Enter the number")
        with col3:
            num=int(float(st.number_input("")))
        s=""
        for i in range(1,num+1,2):
            s=s+str(i)+","
        ans=""
        for j in range(len(s)-1):
            ans=ans+s[j]
        if k:
            with col3:
                st.subheader(ans)

    if sel=="Print the numbers with a difference of three from 0 to given range":
        with col2:
            st.write('')
            st.subheader("Enter the number")
        with col3:
            num=int(float(st.number_input("")))
        s=""
        for i in range(1,num+1,3):
            s=s+str(i)+","
        ans=""
        for j in range(len(s)-1):
            ans=ans+s[j]
        if k:
            with col3:
                st.subheader(ans)

    def cleartext():
        st.session_state["clear"]="Select"

    with col7:
        st.button("Clear",on_click=cleartext)
    




