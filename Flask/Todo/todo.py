
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# configure DB
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

#build the table on DB
class Todo(db.Model):
# create 3  Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default= False)


@app.route('/')
def index():
    todo_list = Todo.query.all() # bring the table content
    return render_template('base.html',todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form["task"]
    new_todo = Todo(title = title) #transter the data to DB class
    db.session.add(new_todo) # what to do (add value)
    db.session.commit() # act - do the action / commit
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() # bring the row of the ID
    todo.complete  = not todo.complete # change the status
    db.session.commit() # update the DB
    return redirect(url_for("index")) # return to home page

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()  # update the DB
    return redirect(url_for("index"))  # return to home page


if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)