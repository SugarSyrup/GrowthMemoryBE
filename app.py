from flask import Flask
from flask_restx import Api, Resource
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate("authentication/firebase_auth.json")
firebase_admin.initialize_app(cred), {
    'databaseURL' : ''
}


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world!"}


if __name__ == "__main":
    app.run(debug=True, host="0.0.0.0", port=80)
