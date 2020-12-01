"""
Targil 5
build simple WEB with Redirect
# framework of WEB application
"""
from flask import Flask,redirect,url_for,render_template
#render_template - build your own HTML pages
# open templates Folder
# in templates folder you put all the HTML code

app = Flask(__name__)

@app.route("/")
def home ():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=80)