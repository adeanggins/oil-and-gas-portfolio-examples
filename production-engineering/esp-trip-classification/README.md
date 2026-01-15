# ESP Trip Cause Classification using NLP

## 1. Problem Statement
Electrical Submersible Pumps (ESPs) are critical artificial lift systems. When an ESP trips (shuts down), operators record the reason in daily drilling or production reports. However, these records are often **unstructured free text** (e.g., "pump stopped due to underload," "high amps detected," "vib high"). 

Analyzing these causes historically is difficult because standard analytics tools cannot process raw text. Manual categorization is time-consuming and prone to human error, leading to poor visibility into the root causes of failure (RCF).

## 2. Solution Overview
This repository contains a Machine Learning solution that automates the categorization of trip reasons using **Natural Language Processing (NLP)**.

**The Workflow:**
1.  **Ingestion:** Load raw operator comments.
2.  **Preprocessing:** Clean text (remove stopwords, punctuation, lemmatization) using **SpaCy** and **NLTK**.
3.  **Vectorization:** Convert text into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
    * *Concept:* TF-IDF highlights words that are unique to specific comments while filtering out generic words that appear everywhere.
4.  **Classification:** Train a Supervised Learning model (Linear SVC or Random Forest) to predict the standardized category (e.g., "Underload", "Overload", "Electrical Failure").

## 3. Results
The model achieves high accuracy in mapping free-text comments to standardized engineering categories, enabling engineers to perform statistical analysis on failure modes automatically.

## 4. Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Download the English language model for SpaCy: `python -m spacy download en_core_web_sm`
3. Run the Jupyter Notebook: `jupyter notebook esp_trip_classifier.ipynb`
