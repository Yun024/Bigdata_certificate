# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# EDA
df.describe()
df.info()
df.shape
df.isna().sum()

# min-max scale 방법1
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
df["f5_1"] = mms.fit_transform(df[["f5"]])

# min-max scale 방법2
df["f5_2"] = df["f5"].transform(lambda x: ((x - x.min())/ (x.max() - x.min())))

# 방법1과 2 비교
df.head()

# 하위 5%, 상위 5% 값 구하기
df["f5_1"].quantile(0.05)
df["f5_1"].quantile(0.95)
