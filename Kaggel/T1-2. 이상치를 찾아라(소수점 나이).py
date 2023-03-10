# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df.head()

# 소수점 데이터 찾기
df_flt=df[df["age"].astype("int64") - df["age"]!=0]

# 이상치를 포함한 데이터 올림, 내림, 버림의 평균값 
ceil = np.ceil(df["age"]).mean()
floor = np.floor(df["age"]).mean()
trunc = np.trunc(df["age"]).mean()

# 평균값 더한 다음 출력
ceil + trunc + floor 

