from flask import Flask, request, jsonify
from flask_restful import abort
import json


def get(app):        
    with open('data.json', 'r') as f:
        data = json.load(f)
        if not data:
            abort(400, message="Could not find any data.")
    return data

def post(app):
    data = request.get_json()
    app.logger.info("Applying post.")
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
        post = "Posted data: {0}".format(data)
    return jsonify(post)
