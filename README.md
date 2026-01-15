# Bank Marketing Machine Learning Project

## 👤 Author

- **Phan Van Son Tung**
- GitHub: [phantung205](https://github.com/phantung205)

## 📌 Introduction
This project applies machine learning techniques to solve a classification problem
related to bank marketing campaigns.

## 🎯 Problem Statement
The goal of this project is to predict whether a client will subscribe to a product
based on given features.

## 📊 Dataset

The dataset used in this project is the **Bank Marketing Dataset**
from the UCI Machine Learning Repository.

- Source: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
- File used: `bank-full.csv`
- Total samples: 41,188
- Features: Client information, campaign details, and economic indicators
- Target variable: `y` (yes / no)

> Note: The dataset is not included in this repository due to size limitations.
Please download it manually from the source link above and place it in:
`data/raw/`


## ⚙️ Methods
- Data preprocessing
- Feature selection
- Model training
- Model evaluation

## 🧠 Models Used
- Support Vector Machine (SVM)
- Random Forest

## 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score

## 🚀 How to Run
```bash
pip install -r requirements.txt
python app.py
