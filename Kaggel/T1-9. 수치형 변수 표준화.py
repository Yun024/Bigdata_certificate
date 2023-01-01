# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# 표준화
### (df["f5"] - df["f5"].mean())/df["f5"]
scaler = StandardScaler()
df["f5"] = scaler.fit_transform(df[["f5"]])


# 중앙값 출력
df["f5"].median()
