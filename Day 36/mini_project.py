# The goal is here is to build a Hello Flask app with the home page, which is slash the basic page stating page 
# showing a welcome message, and then a personalized greeting page with a particular 
# route of slash greet shash the name of the person

# URL/<name> is anything like indrajith or anything 
# whatever it is, i want to use that as a personalized greeting page.
# and then we'll do proper use of HTML templates in ths particular project,
# 

from flask import Flask, render_template

# create flask app
app = Flask(__name__)

# Define a route 
@app.route('/')
def home():
    return render_template('index2.html')

# Greeting Route 
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

# Run the app
if __name__=='__main__':
    app.run(debug=True)