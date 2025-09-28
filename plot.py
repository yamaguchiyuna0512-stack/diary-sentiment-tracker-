import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_diary(target_month:str):
    #　データ集計
    df = pd.read_csv("diary.csv")
    df["date"] = pd.to_datetime(df["date"])

    # デフォルトは今月
    if target_month is None:
        target_month = datetime.now().strftime("%Y-%m")

    # 対象月だけフィルタ
    df_month = df[df["date"].dt.to_period("M") == target_month]
    start = pd.to_datetime(target_month + "-01" )
    end = start + pd.offsets.MonthEnd(1)

    #　グラフ化
    plt.figure(figsize=(8, 4))
    if not df_month.empty:
        plt.plot(df_month["date"],df_month["sentiment"],marker="o", linestyle="-")
    else:
        plt.plot([], [])
 
    plt.title(f"Sentiment Trend in {target_month}")
    plt.ylabel("Sentiment Score （-1 ~ +1）")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.xlim(start, end)
    plt.tight_layout()
    st.pyplot(plt)
