from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': '未着手'
    }
    tasks.append(task)
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        new_status = request.form.get('status')
        tasks[task_id]['status'] = new_status
        return redirect('/')
    else:
        return render_template('edit.html', task=tasks[task_id])

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
