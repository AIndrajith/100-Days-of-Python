# this code refers to how to work templates in flask

from flask import Flask, render_template

# Create Flasl App
app = Flask(__name__)

# Define a Route 
@app.route('/')
def hello():
    return render_template('index.html', name="Flask Developer")

# Run the App
if __name__=="__main__":
    app.run(debug=True)