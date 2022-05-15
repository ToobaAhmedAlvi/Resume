import streamlit as st
import PyPDF2
import textract
import re
import string
Resume = st.sidebar.file_uploader("Upload your input pdf file", type=["pdf"])
global to_text 
def user_input_features():
    #Resume = st.sidebar.file_uploader("Upload your input pdf file", type=["pdf"])
    #if Resume is not None:
    #input_df = PyPDF2.PdfFileReader(Resume)
    pdfReader = PyPDF2.PdfFileReader(Resume)

# Get total number of pages
    num_pages = pdfReader.numPages

# Initialize a count for the number of pages
    count = 0

# Iniialize a text empty etring variable
   
    to_text = ""
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
        return to_text
user_input_features()

st.subheader("USER INPUT PARAMETERS")


