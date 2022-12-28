import streamlit as vAR_st

def ascdesc():
    def asc():
        vAR_c=[]
        flag=0
        new=[]
        vAR_b=vAR_a.split(",")
        
        with col2:
            if s:
                try:
                    for i in vAR_b:
                        vAR_c.append(float(i))
                        flag=0
                            
                
                    if flag==0:    
                        vAR_c.sort()
                        vAR_res=','.join(str(item) for item in vAR_c)
                        vAR_res=vAR_res.split(",")
                        for j in vAR_res:
                            k=str(j).split(".")
                            if k[1]=='0':
                                # k= 3,0
                                new.append(int(k[0])) 
                            else:
                                new.append(float(j))
                        new_res=','.join(str(item) for item in new)  
                        with col1:
                            vAR_st.write("")
                            vAR_st.subheader("Result")

                        vAR_st.write('')
                        vAR_st.success(new_res)

                except ValueError:
                    vAR_st.info("Enter a valid input")

    def desc():
        vAR_c=[]
        flag=0
        new=[]
        vAR_b=vAR_a.split(",")
        with col2:
            if s:
                try:
                    for i in vAR_b:
                        vAR_c.append(float(i))
                        flag=0
                            
                
                    if flag==0:    
                        vAR_c.sort(reverse=True)
                        vAR_res=','.join(str(item) for item in vAR_c)
                        vAR_res=vAR_res.split(",")
                        for j in vAR_res:
                            k=str(j).split(".")
                            if k[1]=='0':
                                # k= 3,0
                                new.append(int(k[0])) 
                            else:
                                new.append(float(j))
                        new_res=','.join(str(item) for item in new)  
                        with col1:
                            vAR_st.write("")
                            vAR_st.subheader("Result")

                        vAR_st.write('')
                        vAR_st.success(new_res)

                except ValueError:
                    vAR_st.info("Enter a valid input")


    cl1,col1,col2,cl2= vAR_st.columns((1,2,2,1))
    ul1,col3,col4,ul2=vAR_st.columns((5,2,2,5))

    def cleartext():
        vAR_st.session_state["Clear"]=""
        vAR_st.session_state["Clear2"]="Select"

    with col3:
        s=vAR_st.button("Submit")
    
    with col4:
        c=vAR_st.button("Clear",on_click=cleartext)


    with col1:
        vAR_st.write('##')
        vAR_st.subheader("Enter the numbers")
    with col2:
        vAR_a=vAR_st.text_input("",key="Clear",placeholder="Eg: 1,2,3,4,5")
    with col1:
        vAR_st.write('###')
        vAR_st.subheader(" Sorting Order")
    with col2:
        selected=vAR_st.selectbox("",("Select","Ascending order","Descending order"),key="Clear2")

    if vAR_a!="":
        if s and selected=="Select":
            with col2:
                vAR_st.subheader("Select the sorting order")

    if vAR_a=="":
        if s:
            with col2:
                vAR_st.info("Enter the input")


    


    if selected=="Ascending order":
        asc()
        
    if selected=="Descending order":
        desc()







        


    


    
