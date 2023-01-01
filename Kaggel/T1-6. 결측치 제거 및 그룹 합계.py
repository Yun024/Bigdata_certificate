# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# f3컬럼 제거 후 결측치 제거
### f3 = df.pop("f3")
### df = df.dropna()


# f1컬럼 결측치 제거
df.isna().sum()
df = df[df["f1"].isnull()==False]

# 그룹 합계 계산name
df.groupby(["city","f2"]).sum()


# 조건에 맞는 값 출력
### df[(df["city"]=="경기")&(df["f2"]==0)]["f1"].sum()
### df.groupby(["city","f2"]).sum()["f1"][0]
df[(df["city"]=="경기")&(df["f2"]==0)].groupby(["city","f2"]).sum()["f1"][0]
