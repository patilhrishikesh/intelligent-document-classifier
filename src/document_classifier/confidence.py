import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def get_confidence_score(model, X):
    """
    Returns confidence score in percentage for Linear SVM
    """
    decision_scores = model.decision_function(X)

    if decision_scores.ndim > 1:
        score = np.max(decision_scores)
    else:
        score = decision_scores[0]

    confidence = sigmoid(score) * 100
    return round(confidence, 2)
