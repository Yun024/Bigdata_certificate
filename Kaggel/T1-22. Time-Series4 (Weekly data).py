## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv",parse_dates=["Date"])

### resample함수 없이 풀기
## weekday변수 생성 후 떨어지는 주단위 데이터 추출
df["weekday"] = df["Date"].dt.weekday
start = df[df["weekday"]==0].index[0]
end = df[df["weekday"]==6].index[-1]
df2 = df.iloc[start:end+1]

## 앞 부분의 남는 데이터 입력
zz = []
for i in range(start):
    zz.append(0)

## 몇주차 데이터인지 리스트 생성
for i in range(len(df2)):
    j = i // 7
    zz.append(j+1)

## 뒷 부분의 남는 데이터 입력 후 주 단위 변수 생성
if (len(df)  - (end+1)) != 0:
    for i in range(len(df) - (end+1)):
        zz.append(j+2)
df["week"] = zz

## 주 단위 Sales변수 합계의 최소값과 최대값을 구하고 그 차이를 절대값으로 추출
Sales_min=df.groupby(zz)["Sales"].sum().min()
Sales_max=df.groupby(zz)["Sales"].sum().max()
abs(Sales_max - Sales_min)


#### resample을 이용한 풀이
## resample을 사용하기 위해 "Date"변수를 index로 세팅
df = df.set_index("Date")

## resample을 이용한 주 단위 데이터 프레임 생성
df2 = df.resample("W").sum()

## 주 단위 Sales변수 합계의 최소값과 최대값을 구하고 그 차이를 절대값으로 추출
Sales_min = df2["Sales"].min()
Sales_max = df2["Sales"].max()
abs(Sales_max - Sales_min)
