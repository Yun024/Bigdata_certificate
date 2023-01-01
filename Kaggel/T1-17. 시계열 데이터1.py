## 패키지 불러오기
import pandas as pd
import numpy as np

## datetime안쓰고 풀이
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df2 = df[df["Date"].str.contains("2022")]
df3 = df2[df2["Date"].apply(lambda x:x.split("-")[1]) == "05"]
df3["Sales"].median() 

## datetime쓰고 풀이
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df["Date"]= pd.to_datetime(df["Date"])
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month
cond1 = df["year"]==2022 
cond2 = df["month"]==5
df2 = df[cond1 & cond2]
df2["Sales"].median()

## datetiem쓰고 두번째 풀이
df["Date"]= pd.to_datetime(df["Date"])
cond1 = df["Date"] >= "2022-05-01"
cond2 = df["Date"] <= "2022-05-31"
df2 = df[cond1 & cond2]
df2["Sales"].median()
