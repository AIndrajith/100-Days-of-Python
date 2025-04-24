from flask import Flask

# create Flask app
app = Flask(__name__) # creates an instance of the flask app

# Defime a Route 
@app.route('/')
def hello():
    return "Hello, Indrajith!"

# Run the App
if __name__ == '__main__':
    app.run(debug=True)