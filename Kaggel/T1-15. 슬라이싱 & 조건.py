## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

## 주어진 데이터 셋에서 age컬럼 상위 20개 데이터 추출
df2 = df.sort_values("age",ascending=False).head(20)

## f1의 결측치를 중앙값으로 채운다.
df2["f1"] = df2["f1"].fillna(df2["f1"].median())

## f4가 ISFJ와 f5가 20 이상인 데이터 추출
df2 = df2[(df2["f4"] == "ISFJ") & (df2["f5"]>= 20)]

## f1의 평균값을 출력
df2["f1"].mean()
