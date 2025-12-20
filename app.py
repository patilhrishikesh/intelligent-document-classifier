import streamlit as st

from document_classifier.confidence import get_confidence_score

from document_classifier.text_cleaning import clean_text
from document_classifier.file_router import save_file_by_class

from document_classifier.text_extractor import extract_text
from document_classifier.text_cleaning import clean_text
from document_classifier.model_persistence import load_artifact

st.set_page_config(
    page_title="Intelligent Document Classifier",
    page_icon="📄",
    layout="centered"

)
st.title("Intellgent Document Classifier")
st.write(
    "Paste document text below to classify it as *Resume*, *Invoice*, or *Reportl*" 
)

uploaded_file = st.file_uploader(
    "Upload a document (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"]
)

extracted_text = ""

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()
    try:
        extracted_text = extract_text(uploaded_file, file_type)
        st.success("Text extracted successfully!")
        st.text_area("Extracted Text (Preview)", extracted_text, height=200)
    except Exception as e:
        st.error(f"Error extracting text : {e}")
@st.cache_resource
def load_models():
    vectorizer = load_artifact("vectorizer.joblib")
    model = load_artifact("model.joblib")
    return vectorizer, model

vectorizer, model = load_models()

user_text = st.text_area(
    "Or paste document text manually:",
    height=200,
    placeholder="Paste resume, invoice, or report text here....",
    value=extracted_text
)

if st.button("Classify Document"):
    if not user_text.strip():
        st.warning("Please upload a document or enter text.")
        
    else:
        cleaned = clean_text(user_text)
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
        confidence = get_confidence_score(model, X)

        st.success(
    f"📌 Predicted Document Type: **{prediction.upper()}**\n\n"
    f"📊 Confidence: **{confidence}%**"
)

        
        if uploaded_file:
            saved_path = save_file_by_class(uploaded_file, prediction)
            st.info(f"📁 File stored in: `{saved_path}`")