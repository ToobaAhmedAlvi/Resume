import streamlit as st
import main
import input_field
import main
if st.button("Predict the CV"):   
    output = main.prediction
    st.success('The category is {}'.format(output))
    safe_html ='''   
        <div style="background-color:red; padding:10px;">
        <h2 style="color:black;text-align:center;">The Job Category is JAVA developer </h2>
        </div>
        '''
    warn_html = '''
        <div style="background-color:red; padding:10px;">
        <h2 style="color:black;text-align:center;">The Job Category is Application Consultant</h2>
        </div>
        '''

    if output == 0:
        st.markdown(safe_html,unsafe_allow_html=True)
    elif output == 1:
        st.markdown(warn_html,unsafe_allow_html=True)

    
