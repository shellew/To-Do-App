from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

class Task:
    def __init__(self, title, description, due_date, status, priority):
        self.title = title
        self.description = description
        self.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
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

# 以下のコードをapp.pyに追加して、フィルタリングを行うエンドポイントを作成

import datetime

@app.route('/filter', methods=['POST'])
def filter_tasks():
    # フロントエンドから送信されたフィルターの値を取得
    filter_data = request.json
    priority = filter_data.get('priority')
    status = filter_data.get('status')
    due_date_from = filter_data.get('dueDateFrom')
    due_date_to = filter_data.get('dueDateTo')

    # フィルタリング処理
    filtered_tasks = []
    for task in tasks:
        if (not priority or task.priority == priority) and \
           (not status or task.status == status) and \
           (not due_date_from or task.due_date >= datetime.datetime.strptime(due_date_from, '%Y-%m-%d').date()) and \
           (not due_date_to or task.due_date <= datetime.datetime.strptime(due_date_to, '%Y-%m-%d').date()):
            filtered_tasks.append(task)

    # フィルタリングされたタスクリストをHTML形式で返す
    return render_template('task_list.html', tasks=filtered_tasks)

if __name__ == '__main__':
    #ローカル開発サーバーでのみ実行
    app.run(debug=True)


