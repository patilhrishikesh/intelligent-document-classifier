from sklearn.metrics import classification_report, confusion_matrix

def evaluate_classifier(model, X_test, y_test) -> None:
    
    predictions = model.predict(X_test)
    
    print("Classification Report:")
    print(classification_report(y_test, predictions))
    
    print("confusion matrix:")
    print(confusion_matrix(y_test, predictions))
    
    
    
    
    
