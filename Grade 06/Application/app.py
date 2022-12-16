import streamlit as vAR_st
from streamlit_option_menu import option_menu
from PIL import Image
import pyautogui
import area_perimeter as ap
import clear
import fact
import palindrome_ as pld
import prime
import square as sc

#vAR_st.set_page_config(layout='wide')
with open('style2.css') as vAR_f:
    vAR_st.markdown (f"<style>{vAR_f.read()}</style>",unsafe_allow_html=True)

if 'placeholder' not in vAR_st.session_state:
    vAR_st.session_state.placeholder = "select"

col1, col2, col3 = vAR_st.columns([1,8,2])
with col1:
    vAR_st.write("")
with col2:
    vAR_img = Image.open("Logo_final.png")
    vAR_st.image(vAR_img,width=400)
with col3:
    vAR_st.write("")



with vAR_st.sidebar:
    selected=vAR_st.selectbox("Menu",('Area & Perimeter','Factorial','Square and Cube','Palindrome','Prime or not'))
    vAR_lib=vAR_st.selectbox("",("Libraries","Streamlit","Pillow"))
    if vAR_st.button("Clear/Reset"):
        pyautogui.hotkey("ctrl","F5")



if __name__=="__main__":
    try:
        if selected=="Area & Perimeter":
            ap.areaperimeter()
        if selected=="Factorial":
            fact.factorial()
        if selected=="Palindrome":
            pld.palindrome()
        if selected=="Prime or not":
            prime.primeornot()
        if selected=="Square and Cube":
            sc.squarecube()
    except BaseException as error:
        vAR_st.error(error)
