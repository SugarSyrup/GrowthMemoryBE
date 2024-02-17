from flask import Flask, request, jsonify
from flask_restx import Api, Resource

from reviewAnalyze import *

app = Flask(__name__)
api = Api(app)

review_analyze()

if __name__ == "__main":
    app.run(debug=True, host="0.0.0.0", port=80)
