import numpy as np
import pandas as pd
import joblib  # For saving and loading the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate a simple dataset (House Size vs. Price)
np.random.seed(42)
house_size = np.random.randint(500, 4000, 1000).reshape(-1, 1)  # House size in sqft
house_price = house_size * 150 + np.random.randint(-50000, 50000, 1000).reshape(-1, 1)  # Price with noise

with open("house_price_data.csv", "w") as f:
    df = pd.DataFrame({"House Size (sqft)": house_size.flatten(), "Price ($)": house_price.flatten()})
    df.to_csv(f, index=False)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_size, house_price, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "house_price_model.pkl")
print("Model saved as house_price_model.pkl")

# Load the model and make predictions
loaded_model = joblib.load("house_price_model.pkl")
predictions = loaded_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
print(f"Predicted price for a 2000 sqft house: {loaded_model.predict([[2000]])[0][0]:.2f}")
