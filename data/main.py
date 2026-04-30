import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

np.random.seed(42)

data = pd.DataFrame({
    'area': np.random.randint(500, 3000, 100),
    'bedrooms': np.random.randint(1, 5, 100),
    'bathrooms': np.random.randint(1, 4, 100),
    'location': np.random.choice(['A', 'B', 'C'], 100),
    'age': np.random.randint(0, 20, 100),
    'price': np.random.randint(2000000, 10000000, 100)
})

print("\nDataset Preview:\n", data.head())

new_house = pd.DataFrame([{
    'area': 1200,
    'bedrooms': 3,
    'bathrooms': 2,
    'age': 5,
    'location_A': 1,
    'location_B': 0,
    'location_C': 0
}])

predicted_price = rf.predict(new_house)

X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Models

lr = LinearRegression()
rf = RandomForestRegressor()

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)
#  Predictions
lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

#  Evaluation

def evaluate(y_test, pred, model_name):
    print(f"\n{model_name}")
    print("MAE:", mean_absolute_error(y_test, pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
    print("R2:", r2_score(y_test, pred))

evaluate(y_test, lr_pred, "Linear Regression")
evaluate(y_test, rf_pred, "Random Forest")


#  Visualization

import os
os.makedirs("outputs", exist_ok=True)   # ✅ ADD HERE

plt.scatter(y_test, rf_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.savefig("outputs/prediction_plot.png")
plt.show()

#  Prediction
new_house = [[1200, 3, 2, 1, 5]]
predicted_price = rf.predict(new_house)

print("\nPredicted Price:", predicted_price[0])
