# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# 조건에 맞는 데이터
df2 = df[df["age"]>=20].copy()
print("전처리 전:",len(df),",","전처리 후:",len(df2))

# 최빈값으로 'f1' 컬럼 결측치 대체
df2["f1"] = df2["f1"].fillna(df2["f1"].mode()[0])
print(df["f1"].isna().sum())
print(df2["f1"].isna().sum())

# 'f1'데이터 여-존슨 yeo-johnson 값 구하기
from sklearn.preprocessing import power_transform
df2["yeo"]=power_transform(df2[["f1"]])

# 'f1'데이터 박스-콕스 box-cox 값 구하기
df2["box"]=power_transform(df2[["f1"]], method="box-cox")

# 두 값의 차이를 절대값으로 구한다음 모두 더해 소수점 둘째 자리까지 출력(반올림)
round(abs(df2["yeo"]-df2["box"]).sum(),2)
