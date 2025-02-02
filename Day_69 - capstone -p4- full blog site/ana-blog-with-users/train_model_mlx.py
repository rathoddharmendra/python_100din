import numpy as np
import mlx.core as mx
import mlx.nn as nn
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generate a simple dataset
np.random.seed(42)
house_size = np.random.randint(500, 4000, 100).reshape(-1, 1)
house_price = house_size * 150 + np.random.randint(-50000, 50000, 100).reshape(-1, 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(house_size, house_price, test_size=0.2, random_state=42)

# Train a simple scikit-learn model
model = LinearRegression()
model.fit(X_train, y_train)

# Convert weights to MLX format
mlx_model = nn.Linear(1, 1)
mlx_model.weight.value = mx.array(model.coef_)  # Set weight
mlx_model.bias.value = mx.array(model.intercept_)  # Set bias

# Save MLX model
mx.savez("house_price_model.mlx", weight=mlx_model.weight.value, bias=mlx_model.bias.value)
print("Model saved in MLX format as house_price_model.mlx")

# Load and use the model
loaded_params = mx.load("house_price_model.mlx")
loaded_model = nn.Linear(1, 1)
loaded_model.weight.value = loaded_params["weight"]
loaded_model.bias.value = loaded_params["bias"]

# Test with new input
input_value = mx.array([[2000]])
predicted_price = loaded_model(input_value)
print(f"Predicted price for 2000 sqft house: {predicted_price.item():.2f}")
