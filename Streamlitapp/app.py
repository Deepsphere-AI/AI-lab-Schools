import streamlit as vAR_st
from PIL import Image
from streamlit_option_menu import option_menu
import source.datatype as dt
import source.roundingoff as ro
import source.calculator as calc
import source.unitconv as uc
import source.bmi as bi
import source.twonum as tn
import source.ascdesc as ad
import source.oddeven as oe
import source.tables as tb
import source.prinum as nr
import source.placevalue as pv
import source.tyme as tc


vAR_st.set_page_config(layout='wide')



#for creating the side menu



with vAR_st.sidebar:
    
    vAR_selected=vAR_st.selectbox("Menu",('Data type', 'Rounding Off','Arithmetic Operation','BMI','Unit Conversion','Compare two numbers','Sorting order',"Odd or Even","Tables","Numbers range","Place value","Time"),key="Clear8")
    vAR_lib=vAR_st.selectbox("",("Libraries","Streamlit","Pillow"),key="Clear9")
    vAR_st.button("Clear/Reset",on_click=dt.clear_text)
    
        
        
    

        

col1, col2, col3 = vAR_st.columns([3,5,3])
with col1:
    vAR_st.write('')
with col2:
    vAR_st.image('https://raw.githubusercontent.com/tarun243/Streamlit-commonToAllIndustry/master/Web_app/Logo_final.png')
with col3:
    vAR_st.write('')

vAR_st.markdown("<h1 font='IBM Flex Sans'; style='text-align: center; color: black; font-size:29px;'>Applied AI for Schools - 6th Grade</h1>", unsafe_allow_html=True)
vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: blue; font-size:29px;'>Simple applications built on Streamlit</p>", unsafe_allow_html=True)
if vAR_selected=="Data type":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the data type</p>", unsafe_allow_html=True)
if vAR_selected=="Rounding Off":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Rounding Off the numbers</p>", unsafe_allow_html=True)
if vAR_selected=="Arithmetic Operation":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for basic arithmetic operations</p>", unsafe_allow_html=True)
if vAR_selected=="BMI":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to calculate BMI</p>", unsafe_allow_html=True)
if vAR_selected=="Unit Conversion":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for Unit Conversion</p>", unsafe_allow_html=True)
if vAR_selected=="Compare two numbers":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for Comparing two numbers</p>", unsafe_allow_html=True)
if vAR_selected=="Sorting order":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for Sorting numbers</p>", unsafe_allow_html=True)
if vAR_selected=="Odd or Even":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find ODD or EVEN, Quotient and Remainder</p>", unsafe_allow_html=True)
if vAR_selected=="Tables":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Multiplication tables</p>", unsafe_allow_html=True)
if vAR_selected=="Numbers range":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to print numbers in range</p>", unsafe_allow_html=True)
if vAR_selected=="Place value":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the place value</p>", unsafe_allow_html=True)
if vAR_selected=="Time":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for time conversion</p>", unsafe_allow_html=True)

#for horizontal line
vAR_st.markdown("""
<hr style="width:100%;height:3px;background-color:gray;border-width:10">
""", unsafe_allow_html=True)

#for opening the css file
with open('style/style.css') as f:
    vAR_st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    try:
        if vAR_selected=='Data type':
            dt.datatype()

        if vAR_selected=='Rounding Off':
            ro.roundup()

        if vAR_selected=='Arithmetic Operation':
            calc.calculator()

        if vAR_selected=='BMI':
            bi.BMI()

        if vAR_selected=='Unit Conversion':
            uc.unitconversion()

        if vAR_selected=="Compare two numbers":
            tn.comparision()

        if vAR_selected=="Sorting order":
            ad.ascdesc()

        if vAR_selected=="Odd or Even":
            oe.oddeven()

        if vAR_selected=="Tables":
            tb.tables()
        
        if vAR_selected=="Numbers range":
            nr.numrange()

        if vAR_selected=="Place value":
            pv.placevalues()

        if vAR_selected=="Time":
            tc.tyme()




    except BaseException as error:
        print("Error Message",error)
        vAR_st.write(error)

#-----------------------------------------------------------------------------------------------------------------
