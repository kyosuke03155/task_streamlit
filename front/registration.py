import streamlit as st
import requests
import json
from datetime import datetime, timedelta
from tools import priority_to_index

def registration_page():
    st.title('タスク登録画面')
    with st.form(key='registration'):
        # タスク内容入力
        content: str = st.text_input('タスク内容', max_chars=100)
        # 優先度入力
        priority: str = st.selectbox('優先度', ['高', '中', '低'], index=1)
        # 期限入力
        deadline = st.date_input('期限', value=datetime.today() + timedelta(days=7))
        data = {
                'content': content,
                'priority': priority_to_index[priority],
                'deadline': str(deadline),
        }
        submit_button = st.form_submit_button(label='タスク登録')

        # タスク登録処理
        if submit_button:
            url = 'http://127.0.0.1:8000/tasks'
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('タスク登録完了')
            else:
                st.error('タスク登録失敗')
    