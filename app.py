from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

class Task:
    def __init__(self, title, description, due_date, status, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    status = '未着手'
    priority = request.form.get('priority')
    task = Task(title, description, due_date, status, priority)
    tasks.append(task)
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        new_status = request.form.get('status')
        priority = request.form.get('priority')
        tasks[task_id].status = new_status
        tasks[task_id].priority = priority
        return redirect('/')
    else:
        task = tasks[task_id]
        return render_template('edit.html', task=task, task_id=task_id)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
