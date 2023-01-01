## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

## f1의 데이터 중 내림차순 정렬 후 10번째 값으로 f1의 결측치 채우기
sorted(df["f1"].dropna(),reverse=True)[9]
df["f1"] = df["f1"].fillna(sorted(df["f1"].dropna(),reverse=True)[9])

## age컬럼 중복 제거 전 "f1"중앙 값
df_median = df["f1"].median()

## age컬럼 중복 제거 후 "f1"중앙 값
df2 = df.drop_duplicates("age")
df_drop_median = df2["f1"].median()

## 중복 제거 전과 후의 중앙 값 차이(절대값)
abs(df_median - df_drop_median)
