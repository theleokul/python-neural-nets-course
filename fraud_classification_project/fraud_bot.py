# Flask - neat microframework for web service creation
from flask import Flask, request

# System utilities
import os

# Good module for transferring python objects between programs
import pickle as pkl

# You know what it is
import numpy as np

# Module for regular expressions stuff
import re

# Create a web service
app = Flask(__name__)

# Directory where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Load our ready model (unpickling)
with open(os.path.join(basedir, 'fraud_clf.pkl'), 'rb') as f:
    fraud_clf = pkl.load(f)

# Regular compiler to detect out feautres in json from requst object
r = re.compile(r'^v\d+$')


@app.route("/", methods=["GET"])
def predict():
    # Filter features from request's json
    request_items = list(filter(lambda item: r.match(item[0]), request.json.items()))

    # Sort features by their number
    request_items.sort(key=lambda item: int(item[0][1:]))

    # Collect feature values in an array
    feature_values = np.array([[value for _, value in request_items]])

    # Use our unpickled model to get prediction
    prediction = fraud_clf.predict(feature_values)

    return str(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)
