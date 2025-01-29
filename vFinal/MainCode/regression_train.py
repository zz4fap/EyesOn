from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import csv
import joblib
from sklearn.linear_model import LinearRegression

# Initialize PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=True)

# Read CSV data
with open('calibration4s_file9-noflash-eachPredict-29-01.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Convert data to float
data = [item for item in data if item]  # Remove empty rows
data = [[float(value) for value in sublist] for sublist in data]  # Convert strings to floats

# Extract pitch, yaw, coord_x, coord_y
pitch_yaw = [(d[0], d[1]) for d in data]

coord_x = [d[2] for d in data]
coord_y = [d[3] for d in data]

# Transform features
poly_features = poly.fit_transform(pitch_yaw)
print(poly_features)
print(coord_x)

# Train Linear Regression model for X
model_x = LinearRegression()
model_x.fit(poly_features, coord_x)

# Train Linear Regression model for Y
model_y = LinearRegression()
model_y.fit(poly_features, coord_y)

# Test data  # Example pitch-yaw pairs
all = [[-0.635, -0.025], [0.204, -0.217], [0.658, -0.548]]
X_test_poly = poly.transform(all)  # Transform test data using polynomial features
y_test_x = [50, 1263, 1870]  # True target values for X
y_test_y = [50, 376, 1030]  # True target values for Y

# Predict X and Y
x_pred = model_x.predict(X_test_poly)
y_pred = model_y.predict(X_test_poly)

print()
print("Ground Truth for X: ", y_test_x)
print("Predictions for X:", x_pred)
print()
print("Ground Truth for Y: ", y_test_y)
print("Predictions for Y:", y_pred)
print()

# Calculate Mean Squared Error
mse_x = mean_squared_error(y_test_x, x_pred)
mse_y = mean_squared_error(y_test_y, y_pred)
print("Mean Squared Error for X:", mse_x)
print("Mean Squared Error for Y:", mse_y)

# Calculate R-squared scores
r2_x = r2_score(y_test_x, x_pred)
r2_y = r2_score(y_test_y, y_pred)
print("R-squared Score for X:", r2_x)
print("R-squared Score for Y:", r2_y)

# Save the models to files
joblib.dump(model_x, 'model_x_linear_morePitch_noflash-29.01.pkl')  # Save model_x
joblib.dump(model_y, 'model_y_linear_morePitch_noflash-29.01.pkl')  # Save model_y

print("Models saved successfully!")
