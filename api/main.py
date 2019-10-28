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
    return jsonify({doc['user']: doc['message'] for doc in list(mydb.entry.find())})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
