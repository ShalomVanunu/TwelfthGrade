"""
program deals with sqlalchemy
# install module flask_sqlalchemy
"""
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.db' #location of DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True # not Event log
db = SQLAlchemy(app) # init DB

class Users(db.Model): # build the DB with Columns
    id = db.Column(db.Integer,  primary_key = True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route("/")
def home():
    return "<h1> Home Page </h1><br><h2> Please visit /Login Page</h2>"

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST": # update the data to DB
        user = request.form["UserNameClick"]
        email = request.form["EmailClick"]
        #print(f" user {user} || Email  {email}")
        ### insert the data to db
        insert_data = Users(username=user, email=email) # init the Class with the argumets
        db.session.add(insert_data) # what to do/ add data
        db.session.commit() # insert data
        return redirect(url_for("home"))
    else:
        return render_template("login1.html")


@app.route("/show") # query from db
def show():
    data_import = Users.query.all()
    all_data = "<h1>"
    for item in data_import:
        all_data = all_data + f"Username: {item.username} || Email: {item.email}"
    return all_data + "</h1>"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)