# streamlit run app.py

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

import sqlite3 
import hashlib


# ----------------------------------------------------------------------

# st.title('W一時表示サイト')

a = st.text_input('パスワード入力', '')

if a == 'mmm':

    df_f = pd.read_json('w_forsave.json').T

    def page1():
        st.title("SS")
        df_s = df_f[df_f['category'] == '主日の御言葉'][['query', 'date', 'category', 'body']].sort_values('date')
        st.dataframe(df_s, width=1000, height=700)


    def page2():
        st.title("WS")
        df_w = df_f[df_f['category'] == '水曜日の御言葉'][['query', 'date', 'category', 'body']].sort_values('date')
        st.dataframe(df_w, width=1000, height=700)

    def page3():
        st.title("General_revelation")
        df_gr = df_f[df_f['category'] == '一般の啓示'][['query', 'date', 'category', 'body']].sort_values('date')
        st.dataframe(df_gr, width=1000, height=700)

    def page4():
        st.title("Dawn_proverb")
        df_dp = df_f[df_f['category'] == '明け方の箴言'][['query', 'date', 'category', 'body']].sort_values('date')
        st.dataframe(df_dp, width=1000, height=700)

    def page5():
        st.title("Dawn")
        st.write("""
        ## 
        """)
        df_d = df_f[df_f['category'] == '明け方または朝の御言葉'][['query', 'date', 'category', 'body']].sort_values('date')
        st.dataframe(df_d, width=1000, height=700)

    pages = dict(
        page1="SS",
        page2="WS",
        page3="General_revelation",
        page4="Dawn_proverb",
        page5="Dawn"
    )

    page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
        "ページ名",
        ["page1", "page2", "page3", "page4", "page5"],
        format_func=lambda page_id: pages[page_id], # 描画する項目を日本語に変換
    )

    if page_id == "page1":
        page1()
    if page_id == "page2":
        page2()
    if page_id == "page3":
        page3()
    if page_id == "page4":
        page4()
    if page_id == "page5":
        page5()


# st.write("""
# ### Danw_revelation
# """)
# df_dr = df_f[df_f['category'] == '明け方の啓示'][['query', 'date', 'category', 'body']].sort_values('date')
# df_dr

