import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
import math
from PIL import Image
import source.find_square as sfs
import source.find_squareroot as root
import source.find_cube as cb
import source.date_input as d_in
import source.find_age as f_age
import source.find_avg as f_avg
import source.profit_loss as pl
import source.find_power as power
import source.parameter as peri
import source.Mark_sheet as marks
import source.gst as gst
import source.title_1 as head

with open('/app/ai-lab-schools/Streamlitapp/Grade-08/style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((2,5,3))
with imcol1:
    st.write("")
with imcol2:
    st.image('/app/ai-lab-schools/Streamlitapp/Grade-08/image/Logo_final.png')
with imcol3:
    st.write("")
#---------Side bar-------#
with st.sidebar:
    selected = st.selectbox("",
                     ['Home','Square','Square Root','Cube','Find the Day','Find the Age',
                     'Find Perimeter from Area','Find the Average','Find the Mark Sheet','Find the Profit or Loss',
                     'Gst Calculator','Find the Power Value'],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Image","Math","Pandas"],key='text1')
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
        if selected =="Square":
            sfs.square()
        if selected == "Square Root":
            root.square_root()
        if selected == "Cube":
            cb.cube()
        if selected == "Find the Day":
            d_in.date_to_day()
        if selected == "Find the Age":
            f_age.age()
        if selected == "Find the Average":
            f_avg.average()
        if selected == "Find the Profit or Loss":
            pl.profit_or_loss()
        if selected == 'Find the Power Value':
            power.power_value()
        if selected == 'Find Perimeter from Area':
            peri.area_perameter()
        if selected == 'Find the Mark Sheet':
            marks.mark()
        if selected == 'Gst Calculator':
           gst.cal_GST()
    except BaseException as error:
        st.error(error)
