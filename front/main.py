import streamlit as st
import requests
import json
from datetime import datetime, timedelta
from tools import priority_to_index, index_to_priority, filter_complete_dic, filter_priority_dic, sort_deadline_dic, sort_priority_dic
from registration import registration_page
from list import list_page


page = st.sidebar.selectbox('Choose your page', ['registration', 'list'])

if page == 'registration':
    registration_page()
    

elif page == 'list':  
    list_page()

    
