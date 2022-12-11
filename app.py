import numpy as np
from flask import Flask, request, render_template, url_for
import pickle
import joblib
from datetime import datetime

app = Flask(__name__)

model = joblib.load("regmodel.pkl")


@app.route('/')
def hello():
    return render_template('house.html')


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if(request.method == 'POST'):
        input_features = [x for x in request.form.values()]
        CRIM = input_features[0]
        ZN = input_features[1]
        INDUS = input_features[2]
        CHAS = input_features[3]
        NOX = input_features[4]
        RM = input_features[5]
        AGE = input_features[6]
        DIS = input_features[7]
        RAD = input_features[8]
        TAX = input_features[9]
        PTRATIO = input_features[10]
        B = input_features[11]
        LSTAT = input_features[12]
        print(input_features)
        result = model.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
        print(result)
        return render_template('house.html', Prediction_text=f"According to the prediction, Price is:- {result}")
    else:
        miss = "Field is missing"
        return render_template('house.html', Prediction_text=f"{miss}")


if __name__ == "__main__":
    app.run()
