import streamlit as vAR_st
from streamlit_option_menu import option_menu
from PIL import Image as img
import source.area_perimeter as ap
import source.clear as cr
import source.fact as fact
import source.palindrome_ as pld
import source.prime as prime
import source.ratio as rio
import source.lcm_1 as lc
from source.statistics import stat

vAR_st.set_page_config(layout='wide')
with open('style/style.css') as vAR_f:
    vAR_st.markdown (f"<style>{vAR_f.read()}</style>",unsafe_allow_html=True)

if 'placeholder' not in vAR_st.session_state:
    vAR_st.session_state.placeholder = "select"

col1, col2, col3 = vAR_st.columns((2,5,3))
with col1:
    vAR_st.write("")
with col2:
    vAR_st.image('https://github.com/danishdeepsphere/AI_Schools/blob/main/image/Logo_final.png')
with col3:
    vAR_st.write("")

with vAR_st.sidebar:
    selected=vAR_st.selectbox("Menu",('Area & Perimeter','Factorial','Statistics','Palindrome','Prime or not','Ratio','LCM'),key="main")
    vAR_lib=vAR_st.selectbox("",("Libraries","Streamlit","Pillow","numpy","scipy"))
    vAR_st.button("Clear/Reset", on_click=cr.button_rad)
        

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
        if selected=="Statistics":
            stat()
        if selected=="Ratio":
            rio.ratio()
        if selected=="LCM":
            lc.lcm()
    except BaseException as error:
        vAR_st.error(error)
