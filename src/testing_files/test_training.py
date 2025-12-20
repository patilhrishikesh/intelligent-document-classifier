from document_classifier.data_loader import load_raw_documents
from document_classifier.text_cleaning import clean_text
from document_classifier.vectorizer import build_tfidf_vectorizer
from document_classifier.train_model import train_logistic_regression
from document_classifier.evaluate_model import evaluate_classifier

# Load data
texts, labels = load_raw_documents("data/raw")

# clean text
cleaned_text = [clean_text(t) for t in texts]

# Vectorize (converting text to numerical values)
vectorizer, X = build_tfidf_vectorizer(cleaned_text)

# Train the model
model, X_train, X_test, y_train, y_test = train_logistic_regression(X, labels)

# Evaluate the model
evaluate_classifier(model, X_test, y_test)
