from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """
    # A test function
    """
    return("Hello world!")
