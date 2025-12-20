# Intelligent Document Classifier 📄🤖

## Overview
The Intelligent Document Classifier is an end-to-end machine learning project that automatically classifies unstructured text documents into predefined categories such as **Resume**, **Invoice**, and **Report**.

The project is built following **industry-style ML development practices**, with a clear separation of data ingestion, preprocessing, feature engineering, modeling, evaluation, and deployment readiness.

---

## Problem Statement
Organizations receive large volumes of unstructured documents (resumes, invoices, reports, etc.).  
Manual document classification is time-consuming, inconsistent, and error-prone.

This project aims to **automate document classification** using machine learning while maintaining a clean, reproducible, and production-oriented pipeline.

---

## Objectives
- Automatically classify documents into predefined categories
- Build a modular and reusable ML pipeline
- Follow real-world engineering practices (clean code, version control, phased development)
- Prepare the system for deployment as an interactive web application

---

## Document Categories
- **Resume** – CVs, skill profiles, professional summaries  
- **Invoice** – Billing, payment, and transaction-related documents  
- **Report** – Formal reports, summaries, and analytical documents  

---

## Project Architecture (High-Level)
Raw Text Documents
↓
Data Ingestion & Validation
↓
Text Cleaning & Normalization
↓
TF-IDF Feature Engineering
↓
ML Classifier (Logistic Regression / Linear SVM)
↓
Predicted Document Category


This architecture ensures **consistency between training and inference**, which is critical in production ML systems.

---

## Tech Stack
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP Techniques:** TF-IDF Vectorization
- **Models:** Logistic Regression, Linear Support Vector Machine (SVM)
- **Environment Management:** `uv`
- **Version Control:** Git & GitHub

---

## Machine Learning Pipeline
This project follows a **modular ML pipeline** design:

1. **Data Ingestion**
   - Safe loading of raw text files
   - Encoding handling and validation
   - Labels inferred from directory structure

2. **Text Cleaning**
   - Lowercasing
   - Noise and symbol removal
   - Standardization for NLP tasks

3. **Feature Engineering**
   - TF-IDF vectorization
   - Vocabulary learned from training data

4. **Model Training**
   - Logistic Regression as baseline
   - Linear SVM for improved text classification

5. **Evaluation**
   - Precision, Recall, F1-score
   - Confusion Matrix

---

## Model Comparison
Two baseline models were implemented and compared using the same pipeline:

| Model | Description |
|-----|------------|
| Logistic Regression | Interpretable, fast baseline classifier |
| Linear SVM | Margin-based classifier, robust for high-dimensional sparse text |

This comparison demonstrates **model selection based on data and problem characteristics**, not assumptions.

---

## Development Approach
The project was developed in **phases**, similar to real-world ML projects:

- Phase 0: Problem definition & repository setup
- Phase 1: Data ingestion & dataset documentation
- Phase 2: Robust data loading & validation
- Phase 3: Text cleaning & normalization
- Phase 4: TF-IDF feature engineering
- Phase 5: Baseline model training
- Phase 6: Model comparison (Logistic vs SVM)
- Phase 7: Deployment preparation (Streamlit UI)

Each phase includes clean Git commits and verifiable outputs.

---

## Future Enhancements
- Streamlit-based web application for document upload and prediction
- Model and vectorizer persistence using `joblib`
- Formal `sklearn` pipeline integration
- Support for PDF documents with OCR
- Transformer-based models (BERT / DistilBERT) for advanced accuracy

---

## Key Learning Outcomes
- End-to-end ML pipeline design
- Text preprocessing and feature engineering
- Model comparison and evaluation
- Industry-style project structuring
- Deployment-oriented ML thinking

---

🚀 **Live Demo:** https://intelligent-document-classifier.streamlit.app


---

## Author
**Hrishikesh Patil**  
Aspiring AI / Machine Learning Engineer  
