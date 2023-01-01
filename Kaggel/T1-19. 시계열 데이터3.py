## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv",parse_dates=["Date"])

## Events가 1인 Sales 데이터 80퍼센트 반영
df1 = df[df["Events"]==1]["Sales"]*0.8
df2 = df[df["Events"]!=1]["Sales"]
df["Sales"] = pd.concat([df1,df2]).sort_index()

## year 데이터와 month 데이터 추출
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month

## 년도별로 데이터 나누기
df1 = df[df["year"]==2022]
df2 = df[df["year"]==2023]

## 그룹바이를 통해 각각의 데이터 합계 중 가장 큰 금액 추출
df1.groupby("month").sum().max()[0]
df2.groupby("month").sum().max()[0]

## 각 합계의 차이를 절대값으로 추출(소수점 반올림 후 정수 출력)
round(abs(df1.groupby("month").sum().max()[0] - df2.groupby("month").sum().max()[0]))
