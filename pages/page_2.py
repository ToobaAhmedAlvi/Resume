import streamlit as st
import main_page
st.markdown("# CV CLASSIFICATION VIA NLP MODEL❄️")
st.sidebar.markdown("# Page 2 ❄️")
import streamlit as st
import pandas as pd
from sklearn import datasets
import PyPDF2
import textract
#import title
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
#model = pickle.load(open('rf_model.pkl','rb'))
Resume = st.sidebar.file_uploader("Upload your input pdf file", type=["pdf"])

to_text = ""
count = 0
  
if Resume is not None:
    pdfReader = PyPDF2.PdfFileReader(Resume)
    num_pages = pdfReader.numPages
    # Extract text from every page on the file
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        to_text += pageObj.extractText()
        #st.write(to_text)
        to_text = to_text.lower()
        # Remove numbers
        to_text = re.sub(r'\d+','',to_text)
        # Remove punctuation
        to_text = to_text.translate(str.maketrans('','',string.punctuation))
        #st.write(to_text)
else:
    single_review = st.sidebar.text_input('Enter single review below:')
     #st.write(to_text)
    to_text = single_review.lower()
    # Remove numbers
    to_text = re.sub(r'\d+','',to_text)
    # Remove punctuation
    to_text = to_text.translate(str.maketrans('','',string.punctuation))
    #st.write(to_text)
text=pd.DataFrame([to_text])
transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("svm-model.pkl", "rb")))
#tfidf = transformer.fit_transform(loaded_vec.fit_transform(requiredText))

test_feature = loaded_vec.transform([to_text])
model = pickle.load(open("mnb_model.pkl","rb"))
prediction = model.predict(test_feature)
st.write(prediction)
if prediction == 0:
    st.write("YOUR CV MATCHES APPLICATION CONSULTANT")
elif prediction ==1:
    st.write("YOUR CV MATCHES DATA ANALYST")
elif prediction ==2:
    st.write("YOUR CV MATCHES JAVA DEVELOPER")
elif prediction ==3:
    st.write("YOUR CV MATCHES PROJECT MANAGER")
else:
    st.write("Sorry,Your CV didnot match any of the available job openings") 


