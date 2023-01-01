## 패키지설치 및 데이터 불러오기
import pandas as pd 
import numpy as np
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df

## city와 f4를 기준으로 f5의 평균값을 구하기
df.groupby(["city","f4"])["f5"].mean()

## f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
round(sum(sorted(df.groupby(["city","f4"])["f5"].mean(),reverse=True)[:7]),2)
