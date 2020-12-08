from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__) # declare the Object of Flask here

@app.route("/login", methods=["GET","POST"]) # declare that the root of http is the main WEB page
def home():
    if request.method =="POST":
        username = request.form["username"]
        email = request.form["email"]
        return f"<h1> {username},{email} </h1> "
    else:
        return render_template("login.html")






if __name__ == '__main__':
    app.run(debug=True) # run the flask web