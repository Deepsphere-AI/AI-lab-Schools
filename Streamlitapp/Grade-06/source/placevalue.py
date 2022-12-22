import streamlit as st

def placevalues():
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((5,2,2,5))
    with col1:
        st.subheader("")
        st.subheader("Enter the Number ")
    with col2:
# ----input button-----#
        input_num=st.text_input("",key="text",placeholder="Eg: 12345")
    with bc2:
        def clear_text():
            st.session_state["text"] = ""
        st.button("Clear", on_click=clear_text) 
    with bc1: 
        if st.button("Submit"):
            if input_num.isnumeric():
                input_num1=int(input_num)
                if len(input_num)==5:
                    ten_thousand = (input_num1 // 10000) % 10
                    thousand= (input_num1 // 1000) % 10
                    hundred= (input_num1 // 100) % 10
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        a="Ten Thousand",ten_thousand 
                        b="Thousand",thousand
                        c="Hundred",hundred
                        d="Tens",tens
                        e="Units",units
                        f=','.join(str(item) for item in a)
                        g=','.join(str(item) for item in b)
                        h=','.join(str(item) for item in c)
                        i=','.join(str(item) for item in d)
                        j=','.join(str(item) for item in e)
                        a=f.replace(",","ㅤ") 
                        b=g.replace(",","ㅤ") 
                        c=h.replace(",","ㅤ") 
                        d=i.replace(",","ㅤ") 
                        e=j.replace(",","ㅤ") 
                        st.write("")  
                        st.subheader(a)
                        st.subheader(b)
                        st.subheader(c)
                        st.subheader(d)
                        st.subheader(e)
                        

                elif len(input_num)==4:
                    thousand= (input_num1 // 1000) % 10
                    hundred= (input_num1 // 100) % 10
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("") 
                        b="Thousand",thousand
                        c="Hundred",hundred
                        d="Tens",tens
                        e="Units",units
                        g=','.join(str(item) for item in b)
                        h=','.join(str(item) for item in c)
                        i=','.join(str(item) for item in d)
                        j=','.join(str(item) for item in e) 
                        b=g.replace(",","ㅤ") 
                        c=h.replace(",","ㅤ") 
                        d=i.replace(",","ㅤ") 
                        e=j.replace(",","ㅤ")   
                        st.write("")
                        st.subheader(b)
                        st.subheader(c)
                        st.subheader(d)
                        st.subheader(e)
                elif len(input_num)==3:
                    hundred= (input_num1 // 100) % 10
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        c="Hundred",hundred
                        d="Tens",tens
                        e="Units",units
                        h=','.join(str(item) for item in c)
                        i=','.join(str(item) for item in d)
                        j=','.join(str(item) for item in e) 
                        c=h.replace(",","ㅤ") 
                        d=i.replace(",","ㅤ") 
                        e=j.replace(",","ㅤ")  
                        st.write("") 
                        st.subheader(c)
                        st.subheader(d)
                        st.subheader(e)
                elif len(input_num)==2:
                    tens= (input_num1 // 10) % 10
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        d="Tens",tens
                        e="Units",units
                        i=','.join(str(item) for item in d)
                        j=','.join(str(item) for item in e) 
                        d=i.replace(",","ㅤ") 
                        e=j.replace(",","ㅤ")  
                        st.write("")   
                        st.subheader(d)
                        st.subheader(e)
                elif len(input_num)==1:
                    units= (input_num1 % 10)
                    with col2:
                        st.markdown("")
                        e="Units",units
                        j=','.join(str(item) for item in e) 
                        e=j.replace(",","ㅤ")
                        st.write("")
                        st.subheader(e)
                with col1:
                    st.subheader("Place values are")
            else:
                with col2:
                    st.subheader("Enter a number")
