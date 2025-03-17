from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

#initialize Flask app
app = Flask(__name__)

#load the trained logistic model
model = joblib.load("models/logistic_regression.pkl")
feature_names = joblib.load("models/feature_names.pkl")

#Define API route for  making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert input data into a DataFrame
        input_data = pd.DataFrame([data])

        # Remove customerID if present (not used in model)
        if 'customerID' in input_data.columns:
            input_data.drop(columns=['customerID'], inplace=True)

        # Ensure all expected features are present
        for col in feature_names:
            if col not in input_data.columns:
                input_data[col] = 0  # Add missing numerical columns with default 0
        
        # Reorder columns to match training order
        input_data = input_data[feature_names]

        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0][1]

        return jsonify({
            "churn_prediction": int(prediction),
            "churn_probability": float(prediction_proba)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

        