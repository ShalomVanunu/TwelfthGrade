"""
Targil 6
build simple WEB with Redirect
# framework of WEB application with argument
"""
from flask import Flask,redirect,url_for,render_template
#render_template - build your own HTML pages
# open templates Folder
# in templates folder you put all the HTML code

app = Flask(__name__)

list_of_names = ["tal", "ofek", "afek", "eden"]

@app.route("/<argument>")
def home (argument):
    return render_template("indexarg.html", shalom=argument)


@app.route("/names")
def names ():
    return render_template("indexarg.html", names=list_of_names)

if __name__ == "__main__":
    app.run(debug=True)