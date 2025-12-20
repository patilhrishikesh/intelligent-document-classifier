from document_classifier.data_loader import load_raw_documents
from document_classifier.text_cleaning import clean_text
from document_classifier.vectorizer import build_tfidf_vectorizer
from document_classifier.train_svm import train_linear_svm
from document_classifier.model_persistence import save_artifact

# Load data
texts, labels = load_raw_documents("data/raw")

# clean text
cleaned_text = [clean_text(t) for t in texts]

# Vectorize
vectorizer, X = build_tfidf_vectorizer(cleaned_text)

# Train best model
model, _, _, _, _ = train_linear_svm(X, labels, test_size=0.3)

# Save artifacts
save_artifact(vectorizer, "vectorizer.joblib")
save_artifact(model, "model.joblib")

print("Model and Vectorizer saved successfully.")