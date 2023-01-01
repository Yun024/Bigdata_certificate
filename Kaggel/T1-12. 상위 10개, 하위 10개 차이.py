###데이터 불러오기 및 패키지 설치
import pandas as pd
import numpy as np
df = pd.read_csv("../input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv",index_col=0)

### 평균,100%가 넘는 접종률 제거(이상치 제거)
df = df[df["ratio"] < 100]

### 상위 10개 국가의 접종률 ,
df_head = pd.DataFrame(sorted(df.groupby("country")["ratio"].max())).tail(10)

### 하위 10개 국가의 접종률 평균
df_tail = pd.DataFrame(sorted(df.groupby("country")["ratio"].max())).head(10)

### 상위10개, 하위10개 국가의 접종률 평균 차이 (, 소수 첫째자리까지 출력)
round(df_head.mean() - df_tail.mean(),1)
