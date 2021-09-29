from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
import pandas as pd
import ast
import json

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self):        
        with open('data.json', 'r') as f:
            data = json.load(f)
            if not data:
                abort(400, message="Could not find any data.")
        return data

    def post(self):
        data = request.get_json()
        app.logger.info("Applying post.")
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
            post = "Posted data: {0}".format(data)
        return jsonify(post)

api.add_resource(Data, '/data')

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)