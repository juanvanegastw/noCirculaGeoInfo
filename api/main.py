from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'key2': 'value'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
