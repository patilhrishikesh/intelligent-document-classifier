from document_classifier.data_loader import load_raw_documents
from document_classifier.text_cleaning import clean_text

text, labels = load_raw_documents('data/raw')

for i in range(3):
    print("Raw text:", text[i][:100])
    print("Cleaned text :", clean_text(text[i])[:100])
    print("-" * 50)