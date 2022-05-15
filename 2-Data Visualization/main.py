import streamlit as st
import pandas as pd
from sklearn import datasets
import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image
from sklearn.ensemble import RandomForestClassifier

import streamlit as st
import PyPDF2
import textract
import re
import string
Resume = st.sidebar.file_uploader("Upload your input pdf file", type=["pdf"])
global to_text
global scores 

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

    terms = {     
         'ApplicationConsultant':['leadership','collaboration','ATM','conflict resolution','Digital Channels',
                                       'integration protocols','ATM/CCDM Controller','analytical','verbal',
                                       'ISO 8583 messages','IBFT','UBPS','Inter Bank Fund Transfers','Banking',
                                       'Utility Bill Payment Services ','banking','finance','7','7 years experience'
                                       'patient','reporting system','stake holder','Payments','client','satisfaction',
                                       'implementation','delivery','administration','agile','budget','cost','direction','feasibility analysis',
                              'finance','kanban','leader','leadership','management','milestones','planning',
                              'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders','operations','custom support','hardware','problem solving','database architecture',
       'programming skills','VMWare','Virtual Box','networking','Information System','Computer Engineering','TCP/IP','Customer Care Service','decision making',
       'cloud','solutions','designing','upgrading system','reporting system','associate application consultant'],
         
        
        'JAVADeveloper':['2 years experience ','JAVA','developer','development','rest','soap','api','REST','SOAP','API','Web Services','database structures',
                      'statistical analysis','analytical mindset','problem solving skills','api','application programming interface',
                      'verbal communication','excellent written skills','Java Programming Language','Ability to work','Software Engineeing','Computer Science',
                      'Masters in CS','fast pace environment','Bachelors','programming','coding','HTML','object oriented programming','OOP','java',
                      'java developer']             
}
       
    developer = 0
    consultant = 0
    scores = []
# Create an empty list where the scores will be stored
    

# Obtain the scores for each area
    for area in terms.keys():
        if area == 'ApplicationConsultant':
            for word in terms[area]:
                if word in to_text:
                    consultant+=1
                    scores.append(consultant)
        else:
            for word in terms[area]:
                if word in to_text:
                    developer +=1
                    scores.append(developer)
       

        
user_input_features()
st.subheader("USER INPUT PARAMETERS")
summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
st.write(summary)
    

