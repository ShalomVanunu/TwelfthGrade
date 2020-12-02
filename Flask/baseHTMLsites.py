"""
Targil 7
for BAsic sites HTML
generate more HTML pages from base.html
"""
from flask import Flask,redirect,url_for,render_template
#render_template - build your own HTML pages
# open templates Folder
# in templates folder you put all the HTML code

app = Flask(__name__)

@app.route("/") #root page
def home ():
    return render_template("home.html")

@app.route("/user") # go toe user.html
def user ():
    return render_template("user.html")

@app.route("/admin") # admin go to admin.html
def admin ():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True, port=80)