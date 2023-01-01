## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

## 주어진 데이터 셋에서 f2가 0값인 데이터 추출
df2 =df[df["f2"]==0]

## 추출한 데이터를 age기준으로 오름차순 정렬
df2 = df2.sort_values("age")

## 정렬한 데이터를 앞에서 부터 20개의 데이터 추출
df2 = df2.head(20)

## f1 결측치(최소값)를 채우기 전과 후의 분산 차이를 계산하시오 (소수점 둘째 자리까지)
var_1 = df2["f1"].var(); print("결측치 채우기 전 분산:",var_1)
df2["f1"] = df2["f1"].fillna(df2["f1"].min())
var_2 = df2["f1"].var(); print("결측치 채운 후 분산:",var_2)
print("결측치 채우기 전과 후의 분산 차이:",round(var_1 - var_2,2))
