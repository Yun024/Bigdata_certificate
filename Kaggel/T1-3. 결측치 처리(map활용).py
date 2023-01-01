# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df.head()

# EDA - 결측값 확인(비율 확인)
df.isna().sum() / len(df)


# 80%이상 결측치 컬럼, 삭제
na_column = df.columns[(df.isna().sum() / 100 >= 0.8)][0]
df.pop(na_column)


# 80%미만 결측치 컬럼, city별 중앙값으로 대체
na_column = df.columns[(df.isna().sum() / 100 > 0.0)][0]
df.isna().sum()
print(df["city"].unique())
k,d,b,s= df.groupby("city").median()["f1"]
df["f1"] = df["f1"].fillna(df["city"].map({'서울': s, '대구':d ,'부산': b,'경기': k}))
df.isna().sum()


# f1 평균값 결과 출력
df["f1"].mean()
