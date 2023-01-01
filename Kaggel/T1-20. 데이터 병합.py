## 패키지 및 데이터 불러오기
import pandas as pd
import numpy as np
df1 = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df3 = pd.read_csv("../input/bigdatacertificationkr/basic3.csv")

## df1과 df3 "f4"를 기준으로 left_join을 하여 인덱스 바뀌지 않는 병합 진행
df_join = pd.merge(df1,df3,how="left",left_on="f4" ,right_on="f4")

## "r2"컬럼의 결측치 제거
df_join2 = df_join[df_join["r2"].isna()==False]

## 앞에서 부터 20개 데이터를 선택하고 'f2'컬럼 합을 구하기
df_join2.head(20)["f2"].sum()
