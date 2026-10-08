<div align="center">

# 📊 Advertising Sales Prediction

### Multiple Linear Regression | Python | Machine Learning

<p>
<strong>Predict product sales using advertising expenditure across TV, Radio, and Newspaper channels.</strong>
</p>

</div>

---

## ✨ Project Overview

This project builds a **Multiple Linear Regression** machine learning model to predict **Sales** based on advertising spending in three channels:

- 📺 **TV**
- 📻 **Radio**
- 📰 **Newspaper**

The project follows a simple machine learning workflow:

**Load Dataset → Explore Data → Prepare Data → Train Model → Predict Sales → Evaluate Model**

---

## 🎯 Objective

The main objective is to understand how advertising investment influences sales and use that relationship to predict future sales.

> **Input:** TV, Radio, and Newspaper advertising expenditure  
> **Output:** Predicted Sales

---

## 🧠 Machine Learning Model

### Multiple Linear Regression

Multiple Linear Regression is used to understand the relationship between multiple input variables and one target variable.

### Features (X)

- TV
- Radio
- Newspaper

### Target (y)

- Sales

### Train-Test Split

The dataset is divided into:

- 🟦 **80% Training Data**
- 🟨 **20% Testing Data**

A fixed `random_state=42` is used to make the results reproducible.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming language |
| 🐼 Pandas | Data loading and data analysis |
| 🔢 NumPy | Numerical operations |
| 🤖 Scikit-learn | Machine learning |
| 📈 Linear Regression | Sales prediction |
| 💻 VS Code | Development environment |
| 🌐 GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
Advertising-Sales-Prediction/
│
├── 📂 Advertising_Project/
│   ├── 📄 Advertising.csv
│   └── 🐍 advertising_sales_prediction.py
│
├── 📄 README.md
└── 📄 .gitignore

📥 Load Dataset
      ↓
🔍 Explore & Inspect Data
      ↓
🧹 Check Data Quality
      ↓
🎯 Select Features & Target
      ↓
✂️ Train-Test Split
      ↓
🤖 Train Linear Regression Model
      ↓
🔮 Generate Predictions
      ↓
📊 Evaluate Model
