from flask import Flask, render_template, url_for, request, jasonify
import numpy as np
import pickle

app = Flask(__name__)
model=pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@flask_app.route("/fuelFlask",methods=["POST"])

def predict():
    fuel_consumption = [float(x) for x in request.form.values()]
    fuels = [np.array(fuel_consumption)]
    prediction = model.predict(fuels)
    return render_template("index.html", prediction_text = "The total co2 emission is  {}".format(prediction))


if __name__ == "__main__":
    app.run(debug=True)