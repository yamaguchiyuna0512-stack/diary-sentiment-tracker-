import pandas as pd
from datetime import datetime
from textblob import TextBlob

def save_entry(entry:str, csv_file="diary.csv"):
          # 日付
          date = datetime.now().strftime("%Y-%m-%d")
          # 感情分析
          blob = TextBlob(entry)
          sentiment = blob.sentiment.polarity # -1(ネガ) 〜 +1(ポジ)
          # csvに保存
          df = pd.DataFrame([[date, entry, sentiment]],columns=["date", "text", "sentiment"])
          df.to_csv("diary.csv", mode="a", header=not os.path.exists("diary.csv"), index=False)
          return sentiment









