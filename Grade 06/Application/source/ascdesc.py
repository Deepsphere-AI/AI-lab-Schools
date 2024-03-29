import streamlit as vAR_st

def ascdesc():
    def asc():
        vAR_c=[]
        flag=0
        vAR_b=vAR_a.split(",")
        
        with col2:
            if s:
                for i in vAR_b:
                    if i.isnumeric():
                        vAR_c.append(int(i))
                    else:
                        vAR_st.subheader("Enter only numeric values")
                        flag=1
                        break
                if flag==0:    
                    vAR_c.sort()
                    vAR_res=','.join(str(item) for item in vAR_c)
                    with col1:
                        vAR_st.write("")
                        vAR_st.subheader("Answer is")

                    vAR_st.write('')
                    vAR_st.subheader(vAR_res)

    def desc():
        vAR_c=[]
        vAR_b=vAR_a.split(",")
        with col2:
            if s:
                for i in vAR_b:
                    if i.isnumeric():
                        vAR_c.append(int(i))
                    else:
                        vAR_st.subheader("Enter only numeric values")
                        flag=1
                        break
            
                if flag==0:
                    vAR_c.sort(reverse=True)
                    vAR_res=','.join(str(item) for item in vAR_c)
                    with col1:
                        vAR_st.write("")
                        vAR_st.subheader("Answer is")
                    vAR_st.write('')
                    vAR_st.subheader(vAR_res)


    cl1,col1,col2,cl2= vAR_st.columns((1,2,2,1))
    ul1,col3,col4,ul2=vAR_st.columns((5,2,2,5))

    def cleartext():
        vAR_st.session_state["Clear"]=""
        vAR_st.session_state["Clear2"]="Select"

    with col3:
        s=vAR_st.button("Submit")
    
    with col4:
        c=vAR_st.button("Clear",on_click=cleartext)


    with col1:
        vAR_st.write('')
        vAR_st.subheader("Enter the numbers")
    with col2:
        vAR_a=vAR_st.text_input("",key="Clear")
    with col1:
        vAR_st.write('')
        vAR_st.subheader(" Sorting Order")
    with col2:
        selected=vAR_st.selectbox("",("Select","Ascending order","Descending order"),key="Clear2")

    if selected=="Ascending order":
        asc()
        
    if selected=="Descending order":
        desc()


        


    


    
