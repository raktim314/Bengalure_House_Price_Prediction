from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hi"
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    app.run()