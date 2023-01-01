## 패키지 및 데이터 불러오기 
import pandas as pd
import numpy as np 
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")

## 1일 이전 시차 컬럼 만들기
df["pv_previous"] = df["PV"].shift(1)

## 결측값은 이후 값으로 채우기
df["pv_previous"]=df["pv_previous"].fillna(method="bfill")

## 조건 생성 후 데이터 추출
cond1 = df["Events"]==1
cond2 = df["Sales"]<=1000000
df2 = df[cond1 & cond2]

## 새로운 데이터 컬럼의 합산
df2["pv_previous"].sum()
