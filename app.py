import streamlit as st

from src.text_cleaning import clean_text
from src.model_persistence import load_artifact

st.set_page_config(
    page_title="Intelligent Document Classifier",
    page_icon="📄",
    layout="centered"

)
st.title("Intellgent Document Classifier")
st.write(
    "Paste document text below to classify it as *Resume*, *Invoice*, or *Reportl*" 
)

@st.cache_resource
def load_models():
    vectorizer = load_artifact("vectorizer.joblib")
    model = load_artifact("model.joblib")
    return vectorizer, model

vectorizer, model = load_models()

user_text = st.text_area(
    "Enter document text:",
    height=250,
    placeholder="Paste resume, invoice, or report text here...."
)

if st.button("Classify Document"):
    if not user_text.strip():
        st.warning("Please enter some text to classify.")
        
    else:
        cleaned = clean_text(user_text)
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
        
        st.success(f"Predicted Document Type: **{prediction.upper()}**")