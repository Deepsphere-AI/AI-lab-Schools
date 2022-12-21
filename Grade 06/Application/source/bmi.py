#Program to calculate BMI
import streamlit as vAR_st
def BMI():
    #vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'>Application to calculate BMI</h1>", unsafe_allow_html=True)
    col1,col2,col5,col6= vAR_st.columns((0.5,2,2,0.7))
    
    with col2:
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader('Select your category')
    
    with col5:
        category = vAR_st.selectbox('',('Adult','Child'))
    
    with col2:
        vAR_st.write('')
        vAR_st.subheader('Select the height format')
    
    with col5:
        status = vAR_st.selectbox('',('Select','cms','meters','feet'),key='clear6')
    
    col1,col2,col3=vAR_st.columns((0.5,3.6,0.6))
    with col2:
        weight = vAR_st.slider("Select your weight(in kgs)",1,200,key='clear2')
    
    if status=='cms':
        with col2:
            height = vAR_st.slider("Select your height",1,240,key='clear3')
            bmi = weight/((height/100)**2)
    
    elif status=="meters":
        with col2:
            height = vAR_st.slider("Select your height",1.0,10.0,key='clear4')
            bmi = weight/(height**2)
    
    else:
        with col2:
            height= vAR_st.slider("Select your height",1.0,10.0,key='clear5')
            bmi = weight/((height/3.28)**2)
    
    def clear_text():
        vAR_st.session_state["clear"]=""
        vAR_st.session_state['clear2']=1
        vAR_st.session_state['clear3']=1
        vAR_st.session_state['clear4']=1.0
        vAR_st.session_state['clear5']=1.0
        vAR_st.session_state['clear6']='Select'

    col6,col7,col8=vAR_st.columns((0.1,2,0.1))
    
    def ChildBMI():
        if(bmi < 13):
            with col7:
                vAR_st.error("You are Extremely Underweight")
        elif(bmi >= 13 and bmi < 16):
            with col7:
                vAR_st.warning("You are Underweight")
        elif(bmi >= 16 and bmi < 18):
            with col7:
                vAR_st.success("Healthy")
        elif(bmi > 18 and bmi <= 21):
            with col7:
                vAR_st.warning("Overweight")
        elif(bmi >= 22):
            with col7:
                vAR_st.error("Extremely Overweight")
    
    def adultBMI():
        if(bmi < 16):
            with col7:
                vAR_st.error("You are Extremely Underweight")
        elif(bmi >= 16 and bmi < 18.5):
            with col7:
                vAR_st.warning("You are Underweight")
        elif(bmi >= 18.5 and bmi < 25):
            with col7:
                vAR_st.success("Healthy")
        elif(bmi >= 25 and bmi < 30):
            with col7:
                vAR_st.warning("Overweight")
        elif(bmi >= 30):
            with col7:
                vAR_st.error("Extremely Overweight")

    col3,col4,col5,col6= vAR_st.columns((5,2,2,5))
    
    with col4:
        vAR_st.write("")
        if(vAR_st.button('Submit')):
            # print the BMI INDEX
            vAR_st.text("Your BMI Index is {}.".format(bmi))
            if category=='Adult':
                adultBMI()
            if category=='Child':
                ChildBMI()
        
        with col5:
            vAR_st.write("")
            vAR_st.button("clear",on_click=clear_text)