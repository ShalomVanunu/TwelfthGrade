"""
Targil 8
for BAsic sites HTML with Bootstrap
generate more HTML pages from basebt.html
"""
from flask import Flask,redirect,url_for,render_template
#render_template - build your own HTML pages
# open templates Folder
# in templates folder you put all the HTML code

app = Flask(__name__)

@app.route("/") # root page
def home ():
    return render_template("homebs.html")


if __name__ == "__main__":
    app.run(debug=True, port=80)