
"""
Targil 4
build simple HTML
# framework of WEB application
"""
from flask import Flask,render_template

app = Flask(__name__) # declare the Object of Flask here

@app.route("/") # declare that the root of http is the main WEB page
def index():
    return render_template("bank.html")


if __name__ == '__main__':
    app.run(debug=True, port=4000) # run the flask web