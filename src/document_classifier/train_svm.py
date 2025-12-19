from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from typing import Tuple

def train_linear_svm(
    X,
    y,
    test_size: float = 0.3,
    random_state: int = 42
) -> Tuple[LinearSVC, any, any, any, any]:
    
    # Train Linear SVM classifier
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    
    # creating model of SVM algorithm called
    model = LinearSVC(
        max_iter=3000
    )
    model.fit(X_train, y_train)
    
    return model, X_train, X_test, y_train, y_test