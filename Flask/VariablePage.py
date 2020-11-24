
"""
Targil 2
build simple WEB with Variables
# framework of WEB application
"""
from flask import Flask

app = Flask(__name__) # declare the Object of Flask here

@app.route("/") # declare that the root of http is the main WEB page
def home():
    return "<h1> Hello Class </h1> <p>Enter Variable Path</p>"


@app.route("/<count>") # < >  is Variable for path
def test(count):
    price_of_apple = 5
    total_price = int(count)*price_of_apple
    return f"<h1> Total income of seeling Apples </h1> <h2> Income  is {total_price} </h2>"


if __name__ == '__main__':
    app.run(debug=True, port=4000) # run the flask web