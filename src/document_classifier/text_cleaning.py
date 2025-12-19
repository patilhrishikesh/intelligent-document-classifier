import re

def clean_text(text:str) -> str:
    # Normalize and clean raw text data for downstream NLP tasks.
    text = text.lower()
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove phone numbers
    text = re.sub(r'\+?\d[d\s\-]{8,}\d', ' ', text)
    
    # Remove currency symbols and numbers
    text = re.sub(r'₹|\$|€|\d+', ' ', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text).strip()
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
    
    