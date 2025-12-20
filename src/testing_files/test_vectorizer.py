from document_classifier.data_loader import load_raw_documents
from document_classifier.text_cleaning import clean_text
from document_classifier.vectorizer import build_tfidf_vectorizer

texts, labels = load_raw_documents("data/raw")

cleaned_texts = [clean_text(t) for t in texts]

vectorizer, X = build_tfidf_vectorizer(cleaned_texts)


print("TF-IDF matrix shape:", X.shape)
print("Sample feature names:", vectorizer.get_feature_names_out()[:20])
