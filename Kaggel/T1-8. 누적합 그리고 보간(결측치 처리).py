# 라이브러리 및 데이터 불러오기
import numpy as np
import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# 조건에 따른 누적합
df[df["f2"]==1]["f1"].cumsum()

# 결측치 처리 (뒤에 나오는 값으로 채움)
df[df["f2"]==1]["f1"].cumsum().fillna(method = "bfill")

# 평균 출력
df[df["f2"]==1]["f1"].cumsum().fillna(method = "bfill").mean()
