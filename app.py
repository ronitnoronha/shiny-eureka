# JMETER PRACTICAL FLASK FILE
# PREDICTION API

from flask import Flask,jsonify,request
import pandas as pd
import joblib

app = Flask(__name__)
model  = joblib.load("telecom_tower_model.pkl")

@app.route('/')
def home():
    return "prediction running successfully"
@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify(
        {
            "prediction":int(prediction[0])
        }
    )
app.run(debug=True)
