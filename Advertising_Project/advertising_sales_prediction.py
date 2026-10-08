import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load data
data = pd.read_csv("Advertising.csv")

print("\n--- Dataset ---")
print(data.head())
print("\nColumns:", list(data.columns))
print("Shape:", data.shape)
print("\nMissing values:\n", data.isnull().sum())

# Features and target
X = data[["TV", "Radio", "Newspaper"]]
y = data["Sales"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test predictions
y_pred = model.predict(X_test)

print("\n--- Predictions ---")
results = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})
print(results.head(10).round(2))

# Required prediction
new_budget = pd.DataFrame({
    "TV": [150],
    "Radio": [20],
    "Newspaper": [30]
})
new_sales = model.predict(new_budget)[0]

print("\n--- New Budget Prediction ---")
print("TV = 150, Radio = 20, Newspaper = 30")
print(f"Predicted Sales = {new_sales:.2f}")

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"MAE  = {mae:.4f}")
print(f"MSE  = {mse:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"R2   = {r2:.4f}")

# Coefficients
coef = pd.Series(model.coef_, index=X.columns)

print("\n--- Coefficients ---")
for name, value in coef.items():
    print(f"{name}: {value:.4f}")

print(f"Intercept: {model.intercept_:.4f}")

strongest = coef.abs().idxmax()
weakest = coef.abs().idxmin()

print(f"\nStrongest impact: {strongest}")
print(f"Weakest impact: {weakest}")

# Regression equation
print("\n--- Regression Equation ---")
print(
    f"Sales = {model.intercept_:.4f}"
    f" + {model.coef_[0]:.4f}*TV"
    f" + {model.coef_[1]:.4f}*Radio"
    f" + {model.coef_[2]:.4f}*Newspaper"
)

# Actual vs predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.75, edgecolors="black")

low = min(y_test.min(), y_pred.min())
high = max(y_test.max(), y_pred.max())
plt.plot([low, high], [low, high], "--", linewidth=2)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Conclusions
print("\n--- Conclusion ---")
print(f"Business recommendation: give more attention to {strongest}, "
      "which has the strongest model coefficient.")
print("Technical improvement: use cross-validation and compare "
      "other regression models to improve prediction reliability.")
