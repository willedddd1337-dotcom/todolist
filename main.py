from flask import Flask, render_template, request, redirect 

todos = ["почистити зуби", "зробити дз", "пограти в доту"]

app = Flask(__name__)


@app.route('/')
def index(): 
    return render_template("index.html", text=todos)


@app.route('/add', methods=["POST"])
def add_new_task(): 
    todos.append(request.form['todo'])
    return redirect("/")


@app.route('/delete/<int:id>')
def delete(id): 
    if 0 <= id < len(todos):
        todos.pop(id)
    return redirect('/')

if __name__ == "__main__": 
    app.run(debug=True)