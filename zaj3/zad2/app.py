from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Task
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/task", methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    tasks = list(map(lambda task: task.serialize(), tasks))
    return tasks

@app.route("/add", methods=['POST'])
def add_task():
    name = request.form.get('name')
    if name:
        new_task = Task(name=name)
        db.session.add(new_task)
        db.session.commit()

        return new_task.serialize()
    return redirect(url_for('index'))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route("/modify/<int:task_id>", methods=['POST'])
def modify_task(task_id):
    task = db.session.get(Task, task_id)
    name = request.form.get('name')
    if task:
        task.name = name
        db.session.commit()
        return task.serialize()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')

