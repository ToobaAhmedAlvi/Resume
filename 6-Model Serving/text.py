import streamlit as st
safe_html = '''
        <div style="background-color:red; padding:10px;">
        <h2 style="color:black;text-align:center;">The Job Category is JAVA developer</h2>
        </div>
        '''
warn_html ='''
        <div style="background-color:red; padding:10px;">
        <h2 style="color:black;text-align:center;">The Job Category is Application Consultant</h2>
        </div>
        '''
 
st.markdown(safe_html,unsafe_allow_html=True)
st.markdown(warn_html,unsafe_allow_html=True)

    