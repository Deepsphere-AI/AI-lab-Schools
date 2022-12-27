import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
import math
from PIL import Image
import source.Cuboid as cuboid
import source.title_1 as head
import source.Cube as cube
import source.Cylinder as cylinder
import source.Cone as cone
import source.Sphere as sphere
import source.mid_point as md
import source.union as uni
import source.trisection2 as tri
with open('/app/ai-lab-schools/Streamlitapp/Grade-09/style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((2,5,3))
with imcol1:
    st.write("")
with imcol2:
    st.image('image/Logo_final.png')
with imcol3:
    st.write("")
#---------Side bar-------#
with st.sidebar:
    selected = st.selectbox("",
                     ['Home',"Cuboid","Cube","Cylinder","Cone","Sphere","Mid Point","Union & Intersection","Trisection"],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Streamlit-option-Menu","Image","Math","Pandas"],key='text1')
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    st.markdown("")
    def clear_text():
            st.session_state["text"] = "Home"
            st.session_state["text1"] = "Library Used"
            st.session_state["text2"] = "GCP Services Used"
    st.button("Clear/Reset", on_click=clear_text)

#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == "Home":
            head.title()
        if selected =="Cuboid":
            cuboid.cuboid_1()
        if selected =="Cube":
            cube.cube_1()
        if selected =="Cylinder":
            cylinder.cylinder_1()
        if selected =="Cone":
            cone.cone_1()
        if selected =="Sphere":
            sphere.sphere_1()
        if selected =="Mid Point":
            md.midpoint_1()
        if selected =="Union & Intersection":
            uni.uni_int()
        if selected =="Trisection":
            tri.trisection_1()
    except BaseException as error:
        st.error(error)
