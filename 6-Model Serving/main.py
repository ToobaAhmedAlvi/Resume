import streamlit as st
import pandas as pd
from sklearn import datasets
import PyPDF2
import textract
import title
import input_field 
import output_field

import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from PIL import Image
from sklearn.ensemble import RandomForestClassifier

st.write("""This app predicts the Job Cateogry For the applicants' CV""")
st.sidebar.header("USER INPUT PARAMETERS")
model = pickle.load(open('rf_model.pkl','rb'))
def predict(Resume):
    #data = {'Resumes',Resume} 
    data = pd.DataFrame(Resume)  
    prediction = model.predict([data])
    
    return int(prediction)

if __name__=='__predict__':
    predict()
    

