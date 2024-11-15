import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from flask import Flask, render_template

# Load the dataset
file_path = 'crop rice.csv'
data = pd.read_csv(file_path)

# Step 1: Data Preprocessing
# Encode categorical variables
label_encoders = {}
for col in ['Region', 'Soil_Type', 'Crop', 'Weather_Condition']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Features and target
X = data.drop('Yield_tons_per_hectare', axis=1)
y = data['Yield_tons_per_hectare']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Model Training
# Initialize the Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
# Train the model
rf_model.fit(X_train, y_train)

# Step 3: Model Evaluation
# Predict on test data
y_pred = rf_model.predict(X_test)
# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Initialize Flask app
app = Flask(__name__)

# Route for displaying the metrics
@app.route('/')
def index():
    # Pass the metrics to the HTML template
    return render_template('index.html', mae=mae, mse=mse, r2=r2)

if __name__ == '__main__':
    app.run(debug=True)
