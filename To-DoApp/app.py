from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import secrets
 
app = Flask(__name__, template_folder="templates")
app.secret_key = secrets.token_hex(16)
todos = [{"task": "Welcome! Add your first todo", "done": False, "created_at": datetime.now()}]

@app.route("/")
def index():
    # sort tasks by first undone tasks , then by creation date
    sorted_todos = sorted(todos, key=lambda x: (x['done'], x['created_at']), reverse=False)
    return render_template("index.html", todos=sorted_todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo'].strip()
    if todo:  # add if todos non-empty
        todos.append({
            "task": todo, 
            "done": False, 
            "created_at": datetime.now()
        })
        flash('Todo added successfully!', 'success')
    else:
        flash('Todo cannot be empty!', 'error')
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        new_task = request.form["todo"].strip()
        if new_task:
            todo['task'] = new_task
            flash('Todo updated successfully!', 'success')
            return redirect(url_for("index"))
        else:
            flash('Todo cannot be empty!', 'error')
    return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)