from sklearn.feature_extraction.text import TfidfVectorizer
import input_field
def pre_processing(requiredText):    
    requiredText = input_field.to_text
    word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    stop_words='english',
    max_features=1500)
    word_vectorizer.fit(requiredText)
    WordFeatures = word_vectorizer.transform(requiredText)
    return WordFeatures

