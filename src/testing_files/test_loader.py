from collections import Counter
from document_classifier.data_loader import load_raw_documents

texts, labels = load_raw_documents("data/raw")

print(f"Total documents loaded: {len(texts)}")
print("Label distribution:", Counter(labels))
