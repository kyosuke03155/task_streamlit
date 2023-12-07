import streamlit as st
import requests
import json
from datetime import datetime
from tools import priority_to_index, index_to_priority, filter_complete_dic, sort_deadline_dic, sort_priority_dic, filter_priority_dic

def change_complete(record):
    # タスク完了状態の変更
    data = {
            'task_id': int(record.get('task_id')),
            'content': record.get('content'),
            'is_completed': not record.get('is_completed'),
            'priority': record.get('priority'),
            'deadline': record.get('deadline'),
        }
    task_id = int(record.get('task_id'))
    url = f'http://127.0.0.1:8000/tasks/{task_id}'
    requests.put(
        url,
        data=json.dumps(data),
    )
    
def list_page():
    st.title('タスク一覧画面')

    # 絞り込み、ソート用のセレクトボックスの表示
    col1, col2, col3, col4, col5 = st.columns(5)  

    # 完了状態絞り込み
    with col1:
        filter_complete = st.selectbox('完了状態絞り込み', ['全て', '完了', '未完了'])

    # 優先度絞り込み
    with col2:
        filter_priority = st.selectbox('優先度絞り込み', ['全て','高', '中', '低'])
    
    # 期限ソート
    with col3:
        sort_deadline = st.selectbox('期限ソート', ['無効','昇順', '降順'])
    
    # 優先度ソート
    with col4:
        sort_priority = st.selectbox('優先度ソート', ['無効','昇順', '降順'])
    params = {'filter_complete': filter_complete_dic[filter_complete], 'filter_priority': filter_priority_dic[filter_priority], 'sort_deadline': sort_deadline_dic[sort_deadline], 'sort_priority': sort_priority_dic[sort_priority]}
    url = 'http://127.0.0.1:8000/tasks'
    res = requests.get(url, params=params)
    records = res.json()

    for index, record in enumerate(records):

        if 'on_edit' not in st.session_state or len(st.session_state.on_edit) != len(records):
            st.session_state.on_edit = [False] * len(records)
        col1, col2, col3, col4, col5 = st.columns(5) 

        # タスクの完了状態状態の確認、変更
        with col1:
            st.checkbox("完了", key="check"+str(index), value=record.get('is_completed'), on_change=change_complete, args=(record,))
        
        # タスクの内容の表示
        with col2:
            st.subheader(record.get('content'))

        # タスクの期限と優先度の表示
        with col3:
            st.write("期限：",record.get('deadline'))
            st.write("優先度：",index_to_priority[record.get('priority')])
        
        # 編集ボタン
        with col4:
            edit = st.button("編集", key="edit_button"+str(index))
            if edit:
                if st.session_state.on_edit[index]:
                    st.session_state.on_edit[index] = False
                else:
                    st.session_state.on_edit[index] = True
        
        # 削除ボタン
        with col5:  
            delete = st.button("削除", key="delete_button"+str(index))
            if delete:
                task_id = int(record.get('task_id'))
                url = f'http://127.0.0.1:8000/tasks/{task_id}'
                res = requests.delete(
                    url,
                )   
                st.experimental_rerun()
        
        # 編集フォーム
        if st.session_state.on_edit[index]:
            with st.form(key='edit'+str(index)):
                # タスク内容入力
                content: str = st.text_input('タスク内容', value=record.get('content') ,max_chars=100)
                # 優先度入力
                priority: str = st.selectbox('優先度', ['高', '中', '低'], index=2-int(record.get('priority')))
                # 期限入力
                deadline = st.date_input('期限', value=datetime.strptime(record.get('deadline'), '%Y-%m-%d').date())
                col1, col2, col3, col4, col5 = st.columns(5)

                #　更新キャンセルボタン
                with col2:
                    cancel_button = st.form_submit_button(label='キャンセル')
                    if cancel_button:
                        st.session_state.on_edit[index] = False
                        st.experimental_rerun()

                # 更新ボタン
                with col3:
                    submit_button = st.form_submit_button(label='タスク更新')
                    # タスク更新処理
                    if submit_button:
                        data = {
                            'task_id': int(record.get('task_id')),
                            'content': content,
                            'priority': priority_to_index[priority],
                            'is_completed': record.get('is_completed'),
                            'deadline': str(deadline),
                        }
                        task_id = int(record.get('task_id'))
                        url = f'http://127.0.0.1:8000/tasks/{task_id}'
                        requests.put(
                            url,
                            data=json.dumps(data),
                        )
                        st.session_state.on_edit[index] = False
                        st.experimental_rerun()
        st.divider()  