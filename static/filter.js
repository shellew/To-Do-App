// filter.js

function applyFilters() {
    // フォームからフィルターの値を取得
    const priority = document.getElementById('priority-filter').value;
    const status = document.getElementById('status-filter').value;
    const dueDateFrom = document.getElementById('due-date-from-filter').value;
    const dueDateTo = document.getElementById('due-date-to-filter').value;
  
    // サーバーにフィルターの値を送信（Ajaxリクエスト）
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          // フィルタリングされたタスクリストを表示
          const taskList = document.getElementById('task-list');
          taskList.innerHTML = xhr.responseText;
        } else {
          console.error('フィルターの適用に失敗しました。');
        }
      }
    };
    xhr.open('POST', '/filter', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ priority, status, dueDateFrom, dueDateTo }));
  }
  
//   JavaScriptコードで送信するJSONデータが正しい形式であることを確認
//   console.log(JSON.stringify({ priority, status, dueDateFrom, dueDateTo }));
