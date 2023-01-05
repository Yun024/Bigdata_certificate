#1번
# 데이터셋(basic1.csv)의 'f5' 컬럼을 기준으로 상위 10개의 데이터를 구하고,
# 'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후,
# 'age'컬럼에서 80 이상인 데이터의'f5 컬럼 평균값 구하기
## 라이브러리 및 데이터 불러오기
import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
## "f5"기준 내림차순 정렬
df = df.sort_values("f5",ascending=False)
## 상위 10개 최솟값 추출 및 입력
df_min = df["f5"].iloc[:10].min()
df["f5"].iloc[:10] = df_min
## "age"가 80이상인 데이터 추출하고 "f5"평균값 추출
df[df["age"]>=80]["f5"].mean()

# #2번
# 데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
# 'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
# 두 표준편차 차이 계산하기
## 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
## 70% 데이터 활용
df2 = df.iloc[:int(len(df)*0.7)].copy()
df2_before=df2["f1"].std()
df2["f1"] = df2["f1"].fillna(df2["f1"].median())
df2_after = df2["f1"].std()
df2_before - df2_after

# 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
# 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함
#3번
# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df2 = df["age"].copy()
cond1 = df2>df2.mean() + (df2.std() * 1.5)
cond2 = df2<df2.mean() - (df2.std() * 1.5)
df2[(cond1 | cond2)].sum()
