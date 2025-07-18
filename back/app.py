from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

yield_model = joblib.load('models/yield_model.pkl')
disease_model = joblib.load('models/disease_model.pkl')

@app.route('/predict_yield', methods=['POST'])
def predict_yield():
    features = np.array(request.json['features']).reshape(1, -1)
    pred = yield_model.predict(features)[0]
    conf = max(yield_model.predict_proba(features)[0])
    return jsonify({'prediction': str(pred), 'confidence': conf})

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    features = np.array(request.json['features']).reshape(1, -1)
    pred = disease_model.predict(features)[0]
    conf = max(disease_model.predict_proba(features)[0])
    return jsonify({'prediction': str(pred), 'confidence': conf})

if __name__ == '__main__':
    app.run(debug=True)
