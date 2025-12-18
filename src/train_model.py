from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from typing import Tuple

def train_logistic_regression(
    X,
    y,
    test_size: float = 0.3,
    random_state: int = 42
) -> Tuple[LogisticRegression, any, any, any, any]:
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size = test_size,
        random_state = random_state,
        # keeps class balance in train and test sets
        stratify=y
        
    )
    
    model = LogisticRegression(max_iter = 1000, n_jobs = -1)
    
    model.fit(X_train, y_train)
    
    return model, X_train, X_test, y_train, y_test