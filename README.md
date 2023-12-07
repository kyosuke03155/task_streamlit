# Streamlit, FastAPIを使ったタスク管理アプリケーション
## 実行方法

ターミナルでbackディレクトリに移動し、バックエンドアプリを起動
```
cd back
uvicorn main:app --reload
```

別のターミナルタブでルートディレクトリから、フロントエンドアプリを起動
```
streamlit run front/main.py
```

## バックエンド

### 概要
- FastAPIでAPIを作成
- データベースはSQLiteを使用
- ORMとしてSQLAlchemyを使用

### APIエンドポイント
- GET /tasks: タスクの取得
- POST /tasks: タスクの登録
- DELETE /tasks/{task_id}: タスクの削除
- PUT /tasks/{task_id}: タスクの更新

### ファイルの概要
- main.py: FastAPIアプリのエンドポイントの定義
- crud.py: データベース操作関連の関数
- model.py: タスクモデルモデルの定義
- schema.py: データのバリデーション
- datebase.py: データベース接続関連

### タスクモデル
- model.pyに記載
- task_id: タスクID (Integer)
- content: タスク内容 (String)
- priority: 優先度 (Integer)
- is_completed: 完了フラグ (Boolean)
- deadline: 期限 (String)



## フロントエンド

### 概要
- Streamlitを使用して実装
- タスク登録画面とタスク一覧画面を表示

### ファイルの概要
- registration.py: タスク登録画面の関数
- list.py: タスク一覧画面の関数

### タスク登録画面
- タスク内容、優先度、期限を入力
- POST APIでタスクを登録

### タスク一覧画面
- Streamlitの仕様によって、ボタンを一度押すと以前の変数が初期化されてしまうため、Session Stateを使用
- セレクトボックスで、タスクの絞り込み(完了状態、優先度)を受け付ける
- セレクトボックスで、タスクのソート(優先度、期限のそれぞれ昇順、降順)を受け付ける
- ソートは両方が有効な場合、期限→優先度の順で行われる
- タスクの完了状態の確認、変更
- タスクの内容の表示
- タスクの期限と優先度の表示
- タスクの更新

### タスク登録
<img width="1287" alt="スクリーンショット 2023-12-07 10 41 53" src="https://github.com/kyosuke03155/task_streamlit/assets/88703973/a15e5b1b-f931-4707-80a6-51f549e01917">

### タスク一覧
<img width="1285" alt="スクリーンショット 2023-12-07 10 30 31" src="https://github.com/kyosuke03155/task_streamlit/assets/88703973/228c9394-480f-4f64-bc7c-065e6ae7d231">

### タスク更新
<img width="1265" alt="スクリーンショット 2023-12-07 10 41 38" src="https://github.com/kyosuke03155/task_streamlit/assets/88703973/a7481395-3ce3-4a9d-abc1-3e7a267e155c">

### 絞り込み
<img width="1291" alt="スクリーンショット 2023-12-07 10 32 22" src="https://github.com/kyosuke03155/task_streamlit/assets/88703973/ccc8e637-73b7-48e5-9915-1a805bcecc4b">

### ソート
<img width="1284" alt="スクリーンショット 2023-12-07 10 33 09" src="https://github.com/kyosuke03155/task_streamlit/assets/88703973/5d7d48a0-9db0-4fd3-931a-44c9c09500fd">


