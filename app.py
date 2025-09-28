import streamlit as st
import pandas as pd
from datetime import datetime
import os
from entry import save_entry
from plot import plot_diary
from dateutil.relativedelta import relativedelta

# 保存用CSVファイル
CSV_FILE = "diary.csv"

st.title("日記感情トラッカー📗")

# CSVがなければ新規作成
if not os.path.exists(CSV_FILE):
     df = pd.DataFrame(columns=["date", "text", "sentiment"])
     df.to_csv(CSV_FILE, index=False)

# 入力フォーム
entry = st.text_area("今日の日記を入力してください")

if st.button("保存"):
    if entry.strip() == "":
        st.warning("入力が空です！")
    else:
        sentiment = save_entry(entry, CSV_FILE)
        st.success(f"保存しました！（感情スコア: {sentiment:.2f}）")

if st.checkbox("保存済みの日記を見る"):
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df)

#  グラフ化(今月)
if st.button("今月の感情推移を見る"):
    target_month = datetime.now().strftime("%Y-%m")
    plot_diary(target_month)
    

# グラフ化（先月）
if st.button("先月の感情推移を見る"):
    target_month = (datetime.now() - relativedelta(months=1)).strftime("%Y-%m")
    plot_diary(target_month)
