from flask import Flask, jsonify

app = Flask(__name__)

# Root Endpoint
@app.route('/')
def home():
    return jsonify({
        "new york":{"temperature":22, "condition":"sunny"},
        "London": {"temperature":15, "condition":"Cloudy"},
        "tokyo": {"temperature":28, "condition":"Clear"}
    })

if __name__=='__main__':
    app.run(debug=True)