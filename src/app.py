from flask import Flask, request, jsonify
import pandas as pd
from model import RetailModel

app = Flask(__name__)
model = RetailModel()
model.load()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X = pd.DataFrame([data])
    prediction = model.predict(X)[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
