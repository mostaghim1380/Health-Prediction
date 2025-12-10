# Advanced Machine Learning System for Multi-Disease Clinical Prediction

**Predicting Diabetes, Heart Disease, and Liver Disease**

A machine learning project that builds and compares multiple classification models to predict the presence of three common medical conditions: **diabetes**, **heart disease**, and **liver disease**. The repository contains data preprocessing, model training, evaluation, and a Streamlit-based demo for interactive prediction.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Dataset(s)](#datasets)
- [Preprocessing](#preprocessing)
- [Models & Techniques](#models--techniques)
- [Evaluation & Results](#evaluation--results)
- [Saved Models](#saved-models)
- [Deployment (Streamlit)](#deployment-streamlit)
- [Repository Structure](#repository-structure)
- [How to run](#how-to-run)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This project presents a **comprehensive end-to-end Machine Learning system** for predicting three high-impact medical conditions — **Diabetes**, **Heart Disease**, and **Liver Disease** — using state-of-the-art model evaluation, modularized architecture, and a reproducible pipeline.

Designed as a portfolio-quality project for academic submission, it demonstrates advanced skills in:
- Clinical data preprocessing
- Model engineering & cross‑validation
- Experimental documentation
- Deployment of a medical prediction system using **Streamlit**
- Reproducible and modular code design

The project mirrors the structure and methodology of professional Data Science workflows used in research labs and healthcare analytics teams.

## Motivation

Chronic diseases continue to be a major healthcare burden worldwide. This project explores how **data‑driven decision support systems** can improve early detection. It aims to showcase technical depth, academic rigor, and the ability to build real-world ML systems aligned with modern healthcare analytics practices.


Early detection of chronic diseases enables timely intervention and better patient outcomes. This project demonstrates an end-to-end ML workflow suitable for academic portfolios and demonstrates technical skills relevant to Data Science graduate applications.

## Datasets

The repository uses public datasets sourced from **Kaggle** for each condition. Each dataset is stored under `data/` and includes a README describing original source, column descriptions, and citation where applicable.

> **Note:** Always check dataset licenses and patient privacy constraints before sharing or publishing.

## Preprocessing

Key preprocessing steps implemented in the notebooks and scripts:

- **Missing value handling:** imputation strategies (mean/median for numeric, most frequent for categorical) with clear justification.
- **Outlier detection:** winsorization / clipping or removal based on domain-relevant thresholds.
- **Encoding categorical variables:** One-Hot Encoding is used for nominal categorical features; ordinal encoding is used when categories have a natural order. (Example: `pd.get_dummies()` or `OneHotEncoder` from scikit-learn).
- **Feature scaling:** `StandardScaler` or `MinMaxScaler` for algorithms sensitive to feature scale (SVM, KNN).
- **Train / validation / test split:** stratified splitting to preserve class balance.
- **Cross-validation:** Stratified K-Fold used during model selection.
- **Feature selection & engineering:** correlation analysis, domain-driven feature creation, and model-based importance checks.

## Models & Techniques

Multiple algorithms were trained and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- XGBoost
- Gradient Boosting (scikit-learn / XGBoost as applicable)

Hyperparameter tuning was performed with `GridSearchCV` / `RandomizedSearchCV` and cross-validation.

**Notable results from experiments:**
- Gradient Boosting delivered the best performance for **diabetes** (model saved with `pickle`).
- Random Forest performed best for **heart disease** in our experiments.
- Decision Tree was the most effective algorithm for **liver disease** on the used dataset.

(These results are based on the datasets and preprocessing pipelines included in this repository; results may vary with other datasets or features.)

## Evaluation & Results

Evaluation metrics included:

- Accuracy
- Precision, Recall, F1-score
- ROC-AUC
- Confusion matrix

Each experiment notebook records the model training logs, hyperparameters, cross-validation scores, and final test set performance. Visualizations (ROC curves, feature importances) are stored in `reports/figures/`.

## Saved Models

Trained models that produced the best results are exported to `models/` as serialized files (Pickle format):

- `models/diabetes_gradient_boosting.pkl` (Gradient Boosting)
- `models/heart_random_forest.pkl` (Random Forest)
- `models/liver_decision_tree.pkl` (Decision Tree)

Each model file includes a corresponding `preprocessor` object (scaler, encoders, feature list) to ensure predictions are reproducible.

## Deployment (Streamlit)

A Streamlit demo (`app.py`) provides an interactive UI for entering patient features and getting a prediction with probability and explanation (feature contributions or important features shown). The `requirements.txt` contains Streamlit and other necessary packages.

## Repository Structure
The repository follows **research‑grade structuring standards**, ensuring clarity, reproducibility, and scalability:

```
├── README.md                 # Comprehensive project documentation
├── requirements.txt          # Exact package dependencies (reproducible environments)
├── app.py                    # Streamlit clinical prediction interface
├── data/                     # Raw + processed datasets from Kaggle
├── notebooks/                # Exploratory analysis & experiment notebooks
├── models/                   # Best-performing serialized models (pickle)
├── src/                      # Modular ML pipeline (preprocessing, training, evaluation)
├── reports/
│   ├── figures/              # ROC curves, confusion matrices, feature importance charts
│   └── results/              # Experiment logs and CV metrics
├── LICENSE                   # Open-source license (MIT)
└── CONTRIBUTING.md           # Guidelines for collaborative development
```

This structure is intentionally designed to reflect **professional ML engineering practices**, making the project easy to review by academic committees and research evaluators.

## How to run

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Create a virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

3. Run the Streamlit demo:

```bash
streamlit run app.py
```

4. To reproduce training experiments, open the corresponding notebook in `notebooks/` or run training scripts in `src/`.

## Requirements

Primary libraries used:

- Python 3.9+
- pandas, numpy
- scikit-learn
- xgboost
- streamlit
- matplotlib, seaborn

A full `requirements.txt` is included.

## Contributing

Contributions are welcome. Open an issue or submit a pull request. Please follow the coding style used in the repo and include tests for new functionality where applicable.

## License

This repository is available under the MIT License. See `LICENSE` for details.

## Contact

**Arshiya Mostaghim**  
Email: mostaghimarshia@gmail.com  
GitHub: https://github.com/mostaghim1380

---

*This README was generated to be included in your GitHub repository for graduate school applications. Feel free to edit any project-specific details (dataset sources, model filenames, or contact info) before publishing.*

