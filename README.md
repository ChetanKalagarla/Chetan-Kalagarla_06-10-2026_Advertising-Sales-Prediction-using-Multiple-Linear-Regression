<div align="center">

📊 Advertising Sales Prediction
Multiple Linear Regression | Python | Machine Learning
<p>
  <strong>Predict product sales using advertising expenditure across TV, Radio, and Newspaper channels.</strong>
</p>

</div>

✨ Project Overview
This project builds a Multiple Linear Regression machine learning model to predict Sales based on advertising spending in three channels:
- 📺 TV
- 📻 Radio
- 📰 Newspaper
The project follows a simple machine learning workflow: load the dataset, inspect and prepare the data, split it into training and testing sets, train the regression model, generate predictions, and evaluate the model.
🎯 Objective
The main objective is to understand how advertising investment influences sales and use that relationship to predict future sales.
Input: TV, Radio, Newspaper advertising expenditure
Output: Predicted Sales

🧠 Machine Learning Model
Multiple Linear Regression
The model learns the relationship between multiple independent variables and one dependent variable.
Features (X):
- TV
- Radio
- Newspaper
Target (y):
- Sales
The dataset is divided into:
- 🟦 80% Training Data
- 🟨 20% Testing Data
A fixed random_state=42 is used so that the split is reproducible.
🛠️ Technologies Used
Technology	Purpose
🐍 Python	Programming language
🐼 Pandas	Data loading and analysis
🔢 NumPy	Numerical operations
🤖 Scikit-learn	Machine learning
📈 Linear Regression	Sales prediction
💻 VS Code	Development environment
🌐 GitHub	Version control and project hosting


📁 Project Structure
Advertising-Sales-Prediction/
│
├── 📂 Advertising_Project/
│   ├── 📄 Advertising.csv
│   └── 🐍 advertising_sales_prediction.py
│
├── 📄 README.md
└── 📄 .gitignore
🔄 Project Workflow
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
⚙️ Installation
1. Clone the repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
2. Open the project folder
cd Advertising_Project
3. Install required libraries
pip install pandas numpy scikit-learn
▶️ How to Run
Run the Python program using:
python advertising_sales_prediction.py
The program displays:
- Dataset information
- Column names
- Dataset shape
- Missing-value information
- Sample predictions
- Model evaluation results
📊 Dataset
The project uses Advertising.csv.
The main columns are:
Column	Description
TV	Advertising expenditure on TV
Radio	Advertising expenditure on Radio
Newspaper	Advertising expenditure on Newspaper
Sales	Product sales


📈 Model Evaluation
The model evaluates predictions using commonly used regression metrics:
- Mean Absolute Error (MAE) — average absolute prediction error
- Mean Squared Error (MSE) — average squared prediction error
- R² Score — indicates how well the model explains the variation in sales
The exact values are generated when the Python script is executed.
🔮 Sample Prediction Output
The program compares actual and predicted sales in a table similar to:
   Actual Sales   Predicted Sales
0      XX.XX          XX.XX
1      XX.XX          XX.XX
2      XX.XX          XX.XX
...
💡 Key Learning Outcomes
- Understanding supervised machine learning
- Understanding regression problems
- Working with CSV datasets using Pandas
- Selecting features and target variables
- Splitting data into training and testing sets
- Training a Multiple Linear Regression model
- Making predictions using a trained model
- Evaluating regression performance
- Using Git and GitHub for project management
🚀 Future Improvements
Possible improvements include:
- 📊 Add data visualizations
- 🔍 Compare multiple regression algorithms
- ⚙️ Add feature scaling and preprocessing
- 📈 Create an interactive prediction interface
- 💾 Save and load the trained model
- ☁️ Deploy the model as a web application
👨‍💻 Author
Chetan Kalagarla
🎓 Computer Science Engineering
💻 Machine Learning | Python | Data Analytics
<div align="center">

⭐ If you find this project useful, consider giving it a star!
Built with Python & Machine Learning 🚀
</div>
