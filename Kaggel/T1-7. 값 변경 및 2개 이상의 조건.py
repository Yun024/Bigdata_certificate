# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

# ESFJ 값을 가진 데이터 확인
df[df["f4"]=="ESTJ"]

# 값 변경하기
df["f4"]=df["f4"].replace("ESTJ","ISFJ")
df[df["f4"]=="ESTJ"]

# 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력
df[(df["city"]=="경기")& (df["f4"]=="ISFJ")]["age"].max()
