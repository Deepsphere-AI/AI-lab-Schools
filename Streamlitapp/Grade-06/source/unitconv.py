import streamlit as vAR_st


def unitconversion():
    def kilometer(num):
        if vAR_select=="Kilometer" and select2=="Hectometer":
            if vAR_k:
                with col2:
                    vAR_st.write('')
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                    vAR_st.write("")
                    vAR_st.success(num)
        if vAR_select=="Kilometer" and select2=="Decameter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Kilometer" and select2=="Meter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Kilometer" and select2=="Decimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Kilometer" and select2=="Centimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Kilometer" and select2=="Millimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*1000000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)

    def hectometer(num):
        if vAR_select=="Hectometer" and select2=="Kilometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Hectometer" and select2=="Decameter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Hectometer" and select2=="Meter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Hectometer" and select2=="Decimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Hectometer" and select2=="Centimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Hectometer" and select2=="Millimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)

    def decameter(num):
        if vAR_select=="Decameter" and select2=="Kilometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decameter" and select2=="Hectometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decameter" and select2=="Meter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decameter" and select2=="Decimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decameter" and select2=="Centimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decameter" and select2=="Millimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)

    def meter(num):
        if vAR_select=="Meter" and select2=="Kilometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Meter" and select2=="Hectometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Meter" and select2=="Decameter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Meter" and select2=="Decimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Meter" and select2=="Centimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Meter" and select2=="Millimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)

    def decimeter(num):
        if vAR_select=="Decimeter" and select2=="Kilometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decimeter" and select2=="Hectometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decimeter" and select2=="Decameter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decimeter" and select2=="Meter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decimeter" and select2=="Centimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Decimeter" and select2=="Millimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)

    def centimeter(num):
        if vAR_select=="Centimeter" and select2=="Kilometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Centimeter" and select2=="Hectometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Centimeter" and select2=="Decameter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Centimeter" and select2=="Meter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Centimeter" and select2=="Decimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Centimeter" and select2=="Millimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num*10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)

    def millimeter(num):
        if vAR_select=="Millimeter" and select2=="Kilometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/1000000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Millimeter" and select2=="Hectometer":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Millimeter" and select2=="Decameter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Millimeter" and select2=="Meter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/1000
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Millimeter" and select2=="Decimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/100
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)
        if vAR_select=="Millimeter" and select2=="Centimeter":
            if vAR_k:
                with col2:
                    vAR_st.write("")
                    vAR_st.subheader("Result")
                num=num/10
                with col3:
                        vAR_st.write("")
                        vAR_st.success(num)


    col1,col2,col3,col4=vAR_st.columns((1,2,2,1))
    with col2:
        vAR_st.write("####")
        vAR_st.subheader("Enter input")
    with col3:
        num=vAR_st.number_input("",key="Clear3")
    with col2:
        vAR_st.write("####")
        vAR_st.subheader("From unit")
    with col3:
        vAR_select=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Decimeter","Centimeter","Millimeter"),key="Clear")
    with col2:
        vAR_st.write("###")
        vAR_st.subheader("To unit")
    with col3:
        if vAR_select=="Kilometer":
            select2=vAR_st.selectbox("",("Select the unit","Hectometer","Decameter","Meter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif vAR_select=="Hectometer":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Decameter","Meter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif vAR_select=="Decameter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Meter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif vAR_select=="Meter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Decimeter","Centimeter","Millimeter"),key="Clear2")
        elif vAR_select=="Decimeter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Centimeter","Millimeter"),key="Clear2")
        elif vAR_select=="Centimeter":
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Decimeter","Millimeter"),key="Clear2")
        else:
            select2=vAR_st.selectbox("",("Select the unit","Kilometer","Hectometer","Decameter","Meter","Decimeter","Centimeter"),key="Clear2")

    




    def cleartext():
        vAR_st.session_state["Clear"]="Select the unit"
        vAR_st.session_state["Clear2"]="Select the unit"
        vAR_st.session_state["Clear3"]=0


    

    col5, col6, col7,col8=vAR_st.columns((5,2,2,5))

    with col6:
        vAR_st.write("")
        vAR_k=vAR_st.button("Submit")

    if vAR_k:
        if vAR_select and select2=="Select the unit":
            with col3:
                vAR_st.info("Select a unit to convert")

    if vAR_k:
        if vAR_select =="Select the unit" and select2 !="Select the unit":
            with col3:
                vAR_st.info("Select the unit of the input")


    with col7:
        vAR_st.write("")
        vAR_st.button("Clear",on_click=cleartext)

    kilometer(num)
    hectometer(num)
    decameter(num)
    meter(num)
    decimeter(num)
    centimeter(num)
    millimeter(num)













    


