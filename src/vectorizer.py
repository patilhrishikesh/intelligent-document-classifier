# This file will only handle text ---> vectors

from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Tuple

def build_tfidf_vectorizer(
    texts: List[str],
    max_features: int = 5000
) -> Tuple[TfidfVectorizer, any]:
    """
    Fit a TF-IDF vectorizer on cleaned text data.
    
    Args:
         texts (List[str]) : Cleaned input documents
         max_features (int): Maximum vocabulary size
         
    Returns:
        vectorizer : Fitted TF-IDF vectorizer
        X : TF-IDF feature matrix
    
    """

    vectorizer = TfidfVectorizer(
        max_features = max_features,
        stop_words = 'english'
    )
    
    X = vectorizer.fit_transform(texts)
    return vectorizer, X