from flask import Flask
from flask import jsonify
import pymongo
import os


SERVER = os.environ['MY_IP']
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://"+SERVER+":27017/")
mydb = myclient["hoynocircula"]


@app.route('/')
def hello_world():
    data = mydb.entry.find().sort([('date', pymongo.DESCENDING), ]).limit(1)
    response = []
    for entry in list(data):
        del entry['_id']
        response.append(entry)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
