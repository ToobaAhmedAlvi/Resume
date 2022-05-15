import streamlit as st
import pandas as pd
from sklearn import datasets
import PyPDF2
import textract
import title
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


st.write("""This app predicts the Job Cateogry For the applicants' CV""")
st.sidebar.header("USER INPUT PARAMETERS")
#file = 'knn_model-Copy.sav'
#model1 = pickle.Unpickler(open(file,'rb'))

single_review = st.sidebar.text_input('Enter single review below:')


to_text = ""
count = 0
to_text = single_review.lower()
    # Remove numbers
to_text = re.sub(r'\d+','',to_text)
    # Remove punctuation
to_text = to_text.translate(str.maketrans('','',string.punctuation))
st.write(to_text)
text=pd.DataFrame([to_text])
transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("svm-model.pkl", "rb")))
#tfidf = transformer.fit_transform(loaded_vec.fit_transform(requiredText))
tfidf = transformer.fit_transform(loaded_vec.fit_transform([to_text]))
st.write(tfidf)
val=tfidf.astype(int)
model = pickle.load(open('rf_model.pkl','rb'))
prediction = model.predict(val)
st.write(prediction)
if prediction == 0:
    st.write("YOU ARE APPLICATION CONSULTANT")
else if prediction ==1:
    st.write("YOU ARE DATA ANALYST")
else if prediction ==2:
    st.write("YOU ARE JAVA DEVELOPER")
else
   st.write("YOU ARE PROJECT MANAGER")
    


