# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

# 조건에 맞는 데이터 (ENFJ, INFP)
df[(df["f4"]=="ENFJ") | (df["f4"]=="INFP")]

# 조건에 맞는 f1의 표준편차 (ENFJ, INFP)
infp = np.sqrt(df[df["f4"]=='INFP']["f1"].var())
enfj = df[df["f4"]=='ENFJ']["f1"].std()

# 두 표준편차 차이 절대값 출력
abs(infp-enfj)
