
"""
Targil 1
build simple WEB
# framework of WEB application
"""
from flask import Flask

app = Flask(__name__) # declare the Object of Flask here

@app.route("/") # declare that the root of http is the main WEB page
def home():
    return "<h1> Hello Class. </h1> <p>enter the /test for start the test</p>"


@app.route("/Test") # another path of test . Case sensitive.
def test():
    return "<h1> Test Page </h1> <p> answer the question</p>"


if __name__ == '__main__':
    app.run(debug=True, port=4000) # run the flask web