
"""
Targil 3
build simple WEB with Redirect
# framework of WEB application
"""
from flask import Flask,redirect,url_for,render_template

app = Flask(__name__) # declare the Object of Flask here

@app.route("/") # declare that the root of http is the main WEB page
def index():
    return "<h1> Hello Class </h1> <p>Enter Variable Path</p>"


@app.route("/name/<name>")
def show_name(name):
   return f"<h1> The name is : {name}"


@app.route("/<count>") # < >  is Variable for path
def test(count):
    price_of_apple = 5
    total_price = int(count)*price_of_apple
    return f"<h1> Total income of seeling Apples </h1> <h2> Income  is {total_price} </h2>"

@app.route("/ynet/") # external WEB
def ynet():
    return redirect("https://www.ynet.co.il")

@app.route("/shalom/") # Internal WEB
def shalom():
    return redirect(url_for("show_name", name = "shalom"))

@app.route("/sellsofapple/<apples>") # internal redirect
def sellsapples(apples):
    return redirect(url_for("test" ,count =apples ))

if __name__ == '__main__':
    app.run(debug=True, port=80) # run the flask web