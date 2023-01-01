# 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv")

# 상관관계 구하기 
df.corr()

# quality와의 상관관계가 가장 큰 값과 가장 작은 값 (절대값으로 확인)
abs(df.corr())["quality"][abs(df.corr()["quality"])!=1].max()
abs(df.corr())["quality"][abs(df.corr()["quality"])!=1].min()

# 결과 출력
round(abs(df.corr())["quality"][abs(df.corr()["quality"])!=1].max() + abs(df.corr())["quality"][abs(df.corr()["quality"])!=1].min(),2)
