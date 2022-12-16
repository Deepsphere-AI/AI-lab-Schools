import streamlit as vAR_st
import clear as cr
import head


def areaperimeter():
    head.title()
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Area and Perimeter for circle, rectangle and square</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    c1,c2=vAR_st.columns((2,2))
    with c1:
        vAR_st.markdown("### ")
        vAR_st.markdown("### Select the shape")
    with c2:
        vAR_shapes=vAR_st.selectbox('',['select','Circle','Rectangle','Square'],key='placeholder')
    if vAR_shapes=="Circle":
        col1,col2=vAR_st.columns((2,2))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("### ")
            vAR_st.markdown("### Select")
        with col2:
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.markdown("## ")
                vAR_st.markdown("### Enter the radius of Circle")
            with col2:
                vAR_a=vAR_st.number_input("",key='rad')
            vAR_ar=3.14*vAR_a**2
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.markdown("### ")
                        vAR_st.success(vAR_ar)
                    with bc2:
                        vAR_st.write("")
                        vAR_st.button("Clear", on_click=cr.button_rad)
                    with us2:
                        vAR_st.write("")
                        vAR_st.button("Clear all", on_click=cr.button_clear)
        
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.markdown("## ")
                vAR_st.markdown("### Enter the radius of Circle")
            with col2:
                vAR_b=vAR_st.number_input("",key='rad2')
            vAR_rp=2*3.14*vAR_b
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.markdown("### ")
                        vAR_st.success(vAR_rp)
                    with bc2:
                        vAR_st.write("")
                        vAR_st.button("Clear", on_click=cr.button_rad)
                    with us2:
                        vAR_st.write("")
                        vAR_st.button("Clear all", on_click=cr.button_clear)
        else:
            pass
    elif vAR_shapes=="Rectangle":
        col1,col2=vAR_st.columns((2,2))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("## ")
            vAR_st.markdown("### Select")
        with col2:
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.markdown("### ")
                vAR_st.markdown("### Lenght of rectangle")
                vAR_st.markdown("## ")
                vAR_st.markdown("### Breadth of rectangle")
            with col2:
                vAR_l=vAR_st.number_input("",key="leng")
                vAR_b=vAR_st.number_input("",key="brth")
            vAR_arect=vAR_l*vAR_b
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_arect)
                    with bc2:
                        vAR_st.write("")
                        vAR_st.button("Clear", on_click=cr.button_rect)
                    with us2:
                        vAR_st.write("")
                        vAR_st.button("Clear all", on_click=cr.button_clear)
            
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.markdown("### ")
                vAR_st.markdown("### Lenght of rectangle")
                vAR_st.markdown("## ")
                vAR_st.markdown("### Breadth of rectangle")
            with col2:
                vAR_l=vAR_st.number_input("",key="leng2")
                vAR_b=vAR_st.number_input("",key="brth2")
            vAR_prect=2*(vAR_l+vAR_b)
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_prect)
                    with bc2:
                        vAR_st.write("")
                        vAR_st.button("Clear", on_click=cr.button_rect)
                    with us2:
                        vAR_st.write("")
                        vAR_st.button("Clear all", on_click=cr.button_clear)
        else:
            pass
    elif vAR_shapes=="Square":
        col1,col2=vAR_st.columns((2,2))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("###")
            vAR_st.markdown("### Select")
        with col2: 
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.markdown("##")
                vAR_st.markdown("### Enter the value of side")
            with col2:
                vAR_s=vAR_st.number_input("",key='sq')
            vAR_arect=vAR_s**2
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_arect)
                    with bc2:
                        vAR_st.write("")
                        vAR_st.button("Clear", on_click=cr.button_sq)
                    with us2:
                        vAR_st.write("")
                        vAR_st.button("Clear all", on_click=cr.button_clear)
                
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.markdown("###")
                vAR_st.markdown("### Enter the value of side")
            with col2:
                vAR_s=vAR_st.number_input("",key='sq2')
            vAR_prect=4*vAR_s
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Answer is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_prect)
                    with bc2:
                        vAR_st.write("")
                        vAR_st.button("Clear", on_click=cr.button_sq)
                    with us2:
                        vAR_st.write("")
                        vAR_st.button("Clear all", on_click=cr.button_clear)
            
        else:
            pass
    else:
        pass