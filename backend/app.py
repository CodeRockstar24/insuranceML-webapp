from flask import Flask, request, jsonify, send_from_directory
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join('backend', 'model', r'C:\Users\elroy\OneDrive\Desktop\insuranceML\backend\model\insurance_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Serve frontend HTML
@app.route("/")
def home():
    return send_from_directory('../frontend', 'index.html')  # Relative to backend folder

# Serve JS and CSS files from frontend folder
@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory('../frontend', filename)

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        df['age'] = df['age'].astype(float)
        df['bmi'] = df['bmi'].astype(float)
        df['children'] = df['children'].astype(float)
        df['sex'] = df['sex'].map({'male': 1, 'female': 0})
        df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
        df['region'] = df['region'].map({'northeast':0, 'northwest':1, 'southeast':2, 'southwest':3})

        prediction = model.predict(df)[0]
        return jsonify({"prediction": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
