from document_classifier.data_loader import load_raw_documents
from document_classifier.text_cleaning import clean_text
from document_classifier.vectorizer import build_tfidf_vectorizer
from document_classifier.train_model import train_logistic_regression
from document_classifier.train_svm import train_linear_svm
from document_classifier.evaluate_model import evaluate_classifier

# Load and prepare data
texts, labels = load_raw_documents("data/raw")
cleaned_texts = [clean_text(t) for t in texts]
vectorizer, X = build_tfidf_vectorizer(cleaned_texts)

print("===== Logistic Regression =====")
lr_model, Xtr, Xte, ytr, yte = train_logistic_regression(X, labels, test_size=0.33)
evaluate_classifier(lr_model, Xte, yte)

print("\n===== Linear SVM =====")
svm_model, Xtr, Xte, ytr, yte = train_linear_svm(X, labels, test_size=0.33)
evaluate_classifier(svm_model, Xte, yte)
