import streamlit as st
uploaded_file = st.file_uploader("Apacheのアクセスログをアップロードしてください。")
if uploaded_file is not None:
    # ファイルがアップローできたら、処理を開始します。
