import streamlit as st
import pandas as pd
from sklearn import datasets
import PyPDF2
import textract
import title
import input_field 
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from PIL import Image
import preprocess
import output_field
from sklearn.ensemble import RandomForestClassifier

st.write("""This app predicts the Job Cateogry For the applicants' CV""")
st.sidebar.header("USER INPUT PARAMETERS")
#file = 'knn_model-Copy.sav'
#model1 = pickle.Unpickler(open(file,'rb'))
model = pickle.load(open('rf_model.pkl','rb'))

def predict_cv(data):
    #data = pd.DataFrame('cleaned_resume') 
    prediction = model.predict(preprocess.WordFeatures)
    print(prediction)
    return int(prediction)

if __name__=='__predict_cv__':
    predict_cv()
    
    

    

