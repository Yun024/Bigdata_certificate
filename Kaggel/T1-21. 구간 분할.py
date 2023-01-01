## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

## "age"컬럼 이상치 제거(이상치는 음수(0포함), 소수점 값)
cond1 =  df["age"] > 0
cond2 =  df["age"].apply(lambda x: int(x)) == df["age"]
df2 = df[cond1 & cond2]
df2 = df2.sort_values("age").reset_index(drop=True)

## 동일한 개수로 나이 순으로 3그룹으로 나누기
age1 = df2.iloc[0:30]
age2 = df2.iloc[30:60]
age3 = df2.iloc[60:90]

## 각 그룹의 중앙값 더하기
age1["age"].median() + age2["age"].median() + age3["age"].median()
