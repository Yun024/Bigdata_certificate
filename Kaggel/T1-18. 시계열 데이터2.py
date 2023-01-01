## 패키지 불러오기
import numpy as np
import pandas as pd
from datetime import datetime

## 2022년 5월 데이터 필터링
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df["Date"] = pd.to_datetime(df["Date"])
cond1 = df["Date"] >= "2022-05-01"
cond2 = df["Date"] <= "2022-05-31"
df2 = df[cond1 & cond2]

## 주말과 주중 데이터 추출 후 각각의 평균 구하기 
df_weekend = df2[df2["Date"].apply(lambda x: x.weekday()) >  4]
df_weekday = df2[df2["Date"].apply(lambda x: x.weekday()) <=  4]
df_weekend["Sales"].mean()
df_weekday["Sales"].mean()

## 평균의 차이 구하기(소수점 둘째자리까지 출력, 반올림)
round(df_weekend["Sales"].mean() - df_weekday["Sales"].mean(),2)

## 다른 풀이
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month
df["day of week"] = df["Date"].dt.dayofweek
cond1 = df["year"]==2022
cond2 = df["month"] == 5
df2 = df[cond1 & cond2]
cond3 = df2["day of week"] > 4 
cond4 = df2["day of week"] <= 4
df_weekend= df2[cond3]
df_weekday= df2[cond4]
round(df_weekend["Sales"].mean() - df_weekday["Sales"].mean(),2)
