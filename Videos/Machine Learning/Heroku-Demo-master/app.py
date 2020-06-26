import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))




model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index_page():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [int_features]
    prediction = model.predict(final_features)

    output = prediction[0]
    Answer = ''
    if output == 1:
        Answer = "Yes"

    else:
        Answer = "No"
    #conf_score = prediction.predict_proba([final_features])* 100


    return render_template('index.html', prediction_text='Is the customer Going to subscribe to a term deposit? {}, final features {}'.format(Answer, final_features))

if __name__ == "__main__":
    app.run(debug=True)
