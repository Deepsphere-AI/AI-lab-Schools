import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
def title():
    st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Applied AI for schools - 8th Grade</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>Simple application built on Streamlit</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find Square, Square root, Cube, Day, Age, Perimeter of the Square, Average, MarkSheet, Profit or Loss Calculator, GST Calculator, Vaule of Power.</p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)