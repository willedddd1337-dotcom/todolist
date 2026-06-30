from flask import Flask, render_template, request, redirect 
from todo import AddTask, completed, show, delete, Task
from db import SessionLocal


app = Flask(__name__)


@app.route('/')
def index(): 
    tasks = show()
    print(tasks)
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=["POST"])
def add_new_task(): 
    new_task = request.form["todo"]
    AddTask(new_task)
    return redirect('/')

@app.route('/delete/<int:id>')
def Delete(id: int): 
    delete(id)
    return redirect('/')

@app.route('/complete/<int:id>', methods=["POST"])
def Сomplete(id: int): 
    completed(id)
    return redirect('/')

if __name__ == "__main__": 
    app.run(debug=True)