from flask_restful import Resource, Api, reqparse, abort
from flask import Flask, render_template, request, make_response, session
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
import authomatic
import logging
import sys
from config import CONFIG
import requests
import pymongo
import pprint
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__,template_folder='templates')
api = Api(app)

authomatic = Authomatic(CONFIG, '123qwe,./', report_errors=False)


client = pymongo.MongoClient("mongodb+srv://sherisenia:pa$$w0rd@cluster0.y4ewv.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
collection = db.webusers_db

@app.route('/')
def index():
    return render_template('webpageoauth3.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()

        # The rest happens inside the template.
        POST  = [{
            "_id": result.user.id,
            "name": result.user.name,
            "mail": result.user.email}]

        try:
          result = collection.insert_many(POST, ordered=False)

        except pymongo.errors.BulkWriteError as e:
          print(e.details['writeErrors'])

        return render_template('webpageoauth3.html', result=result) 

        panic = filter(lambda x: x['code'] != 11000, e.details['writeErrors'])

        if len(panic) > 0:
          print("Iets gaat mis!")

    # Don't forget to return the response.
    return response


#@app.route('/data', methods=["GET", "POST"])
#def data():
#    data = {}
#    if request.method == "POST":
#        return render_template("webpageoauth3.html")

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
