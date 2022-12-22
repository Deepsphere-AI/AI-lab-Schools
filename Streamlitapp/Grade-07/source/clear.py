import streamlit as vAR_st

def button_clear():
    vAR_st.session_state["clear"]= ""
    vAR_st.session_state.placeholder = "select"

def button_rad():
    vAR_st.session_state["rad"]= 0
    vAR_st.session_state["rad2"]= 0
    vAR_st.session_state["main"]="Area & Perimeter"
    vAR_st.session_state.placeholder = "select"
    
def button_rect():
    vAR_st.session_state["leng"]= 0
    vAR_st.session_state["brth"]= 0
    vAR_st.session_state["leng2"]= 0
    vAR_st.session_state["brth2"]= 0

def button_sq():
    vAR_st.session_state["sq"]= 0
    vAR_st.session_state["sq2"]= 0
    vAR_st.session_state["fact_in"]=""
    vAR_st.session_state["palin_in"]=""
    vAR_st.session_state['prime_in']=0
    vAR_st.session_state["rth_in"]=0
    vAR_st.session_state["rtb_in"]=0
    vAR_st.session_state["rth_inp"]=0
    vAR_st.session_state["rtb_inp"]=0
    vAR_st.session_state["rhm_in1"]=0
    vAR_st.session_state["rhm_in2"]=0
    vAR_st.session_state["rhm_p"]=0
    vAR_st.session_state["tb1"]=0
    vAR_st.session_state["tb2"]=0
    vAR_st.session_state["th"]=0
    vAR_st.session_state["tb1_p"]=0
    vAR_st.session_state["tb1_p"]=0
    vAR_st.session_state["ts1"]=0
    vAR_st.session_state["ts1"]=0
    vAR_st.session_state["ts2"]=0

def button_c():
    #vAR_st.session_state.placeholder="Square"
    vAR_st.session_state["clear"]= 0
    vAR_st.session_state["clear2"]= 0
