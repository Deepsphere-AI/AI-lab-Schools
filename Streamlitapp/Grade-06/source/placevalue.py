import streamlit as vAR_st

def placevalues():
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((5,2,2,5))
    with col1:
        vAR_st.subheader("")
        vAR_st.subheader("Enter the Number ")
    with col2:
# ----input button-----#
        vAR_num=vAR_st.text_input("",key="text",placeholder="Accepts only 5 digit integer values")
    with bc2:
        def clear_text():
            vAR_st.session_state["text"] = ""
        vAR_st.button("Clear", on_click=clear_text) 
    with bc1:
        if vAR_st.button("Submit"):
                if vAR_num.isnumeric():
                    vAR_num1=int(vAR_num)
                    if len(vAR_num)==5:
                        ten_thousand = (vAR_num1 // 10000) % 10
                        thousand= (vAR_num1 // 1000) % 10
                        hundred= (vAR_num1 // 100) % 10
                        tens= (vAR_num1 // 10) % 10
                        units= (vAR_num1 % 10)
                        with col2:
                            vAR_st.markdown("")
                            vAR_a="Ten Thousand",ten_thousand 
                            vAR_b="Thousand",thousand
                            vAR_c="Hundred",hundred
                            vAR_d="Tens",tens
                            vAR_e="Units",units
                            vAR_f=','.join(str(item) for item in vAR_a)
                            vAR_g=','.join(str(item) for item in vAR_b)
                            vAR_h=','.join(str(item) for item in vAR_c)
                            vAR_i=','.join(str(item) for item in vAR_d)
                            vAR_j=','.join(str(item) for item in vAR_e)
                            vAR_a=vAR_f.replace(",","ㅤ") 
                            vAR_b=vAR_g.replace(",","ㅤ") 
                            vAR_c=vAR_h.replace(",","ㅤ") 
                            vAR_d=vAR_i.replace(",","ㅤ") 
                            vAR_e=vAR_j.replace(",","ㅤ") 
                            vAR_st.write("")  
                            vAR_st.success(vAR_a)
                            vAR_st.success(vAR_b)
                            vAR_st.success(vAR_c)
                            vAR_st.success(vAR_d)
                            vAR_st.success(vAR_e)
                            with col1:
                                vAR_st.subheader("Place values chart is")
                            

                    elif len(vAR_num)==4:
                        thousand= (vAR_num1 // 1000) % 10
                        hundred= (vAR_num1 // 100) % 10
                        tens= (vAR_num1 // 10) % 10
                        units= (vAR_num1 % 10)
                        with col2:
                            vAR_st.markdown("") 
                            vAR_b="Thousand",thousand
                            vAR_c="Hundred",hundred
                            vAR_d="Tens",tens
                            vAR_e="Units",units
                            vAR_g=','.join(str(item) for item in vAR_b)
                            vAR_h=','.join(str(item) for item in vAR_c)
                            vAR_i=','.join(str(item) for item in vAR_d)
                            vAR_j=','.join(str(item) for item in vAR_e) 
                            vAR_b=vAR_g.replace(",","ㅤ") 
                            vAR_c=vAR_h.replace(",","ㅤ") 
                            vAR_d=vAR_i.replace(",","ㅤ") 
                            vAR_e=vAR_j.replace(",","ㅤ")   
                            vAR_st.write("")
                            vAR_st.success(vAR_b)
                            vAR_st.success(vAR_c)
                            vAR_st.success(vAR_d)
                            vAR_st.success(vAR_e)
                            with col1:
                                vAR_st.subheader("Place values chart is")
                    elif len(vAR_num)==3:
                        hundred= (vAR_num1 // 100) % 10
                        tens= (vAR_num1 // 10) % 10
                        units= (vAR_num1 % 10)
                        with col2:
                            vAR_st.markdown("")
                            vAR_c="Hundred",hundred
                            vAR_d="Tens",tens
                            vAR_e="Units",units
                            vAR_h=','.join(str(item) for item in vAR_c)
                            vAR_i=','.join(str(item) for item in vAR_d)
                            vAR_j=','.join(str(item) for item in vAR_e) 
                            vAR_c=vAR_h.replace(",","ㅤ") 
                            vAR_d=vAR_i.replace(",","ㅤ") 
                            vAR_e=vAR_j.replace(",","ㅤ")  
                            vAR_st.write("") 
                            vAR_st.success(vAR_c)
                            vAR_st.success(vAR_d)
                            vAR_st.success(vAR_e)
                            with col1:
                                vAR_st.subheader("Place values chart is")
                    elif len(vAR_num)==2:
                        tens= (vAR_num1 // 10) % 10
                        units= (vAR_num1 % 10)
                        with col2:
                            vAR_st.markdown("")
                            vAR_d="Tens",tens
                            vAR_e="Units",units
                            vAR_i=','.join(str(item) for item in vAR_d)
                            vAR_j=','.join(str(item) for item in vAR_e) 
                            vAR_d=vAR_i.replace(",","ㅤ") 
                            vAR_e=vAR_j.replace(",","ㅤ")  
                            vAR_st.write("")   
                            vAR_st.success(vAR_d)
                            vAR_st.success(vAR_e)
                            with col1:
                                vAR_st.subheader("Place values chart is")
                    elif len(vAR_num)==1:
                        units= (vAR_num1 % 10)
                        with col2:
                            vAR_st.markdown("")
                            vAR_e="Units",units
                            vAR_j=','.join(str(item) for item in vAR_e) 
                            vAR_e=vAR_j.replace(",","ㅤ")
                            vAR_st.write("")
                            vAR_st.success(vAR_e)
                            with col1:
                                vAR_st.subheader("Place values chart is")
        
                    else:
                        with col2:
                            vAR_st.info("Enter number with only 5 digits")
                    

                else:
                    with col2:
                        vAR_st.info("Enter a number")

        


