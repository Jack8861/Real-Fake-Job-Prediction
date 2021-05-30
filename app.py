from wsgiref import simple_server
from flask import Flask, request, render_template
# from flask import Response
import os
from flask_cors import CORS, cross_origin
from Data_prediction_process.DataPredictionProcessor import PredictionProcess



app = Flask(__name__)
CORS(app)  # what does it do?

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        data = {}
        data['title'] = request.form['title']
        data['location'] = request.form['location']
        data['department'] = request.form['department']
        data['salary_range'] = request.form['salary_range']
        data['company_profile'] = request.form['company_profile']

        predictor = PredictionProcess(data)
        predictor.find_probabilities()
        prediction = predictor.get_prediction()

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
