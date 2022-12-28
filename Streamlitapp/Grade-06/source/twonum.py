import streamlit as vAR_st

def comparision():
    def comp():
        if vAR_st.button("Submit"):
            with col2:
                vAR_st.write("")
                vAR_st.write('')
                vAR_st.subheader("Result")
            if vAR_num1>vAR_num2:
                with col3:
                    vAR_st.write("")
                    vAR_st.success("A is greater than B")
            elif vAR_num1<vAR_num2:
                with col3:
                    vAR_st.write("")
                    vAR_st.success("B is greater than A")
            else:
                with col3:
                    vAR_st.write('')
                    vAR_st.success("Both the numbers are equal")


    col1,col2,col3,col4=vAR_st.columns((1,2,2,1))
    with col2:
        vAR_st.write("##")
        vAR_st.markdown("### Enter number 1")
    with col3:
        vAR_num1=vAR_st.number_input("",key="Clear")
    with col2:
        vAR_st.write("#")
        vAR_st.markdown("### Enter number 2")
    with col3:
        vAR_num2=vAR_st.number_input("",key="Clear2")
    

    col5,col6,col7,col8=vAR_st.columns((5,2,2,5))
    with col6:
        vAR_st.write('')
        comp()

    def cleartext():
        vAR_st.session_state["Clear"]=0
        vAR_st.session_state['Clear2']=0

    with col7:
        vAR_st.write("")
        vAR_st.button("Clear",on_click=cleartext)


        


    
