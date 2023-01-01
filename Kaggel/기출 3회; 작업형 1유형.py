# Q. 2022년 데이터 중 2022년 중앙값보다 큰 값의 데이터 수
## 패키지 및 데이터 불러오기 
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data2.csv",index_col="year")
df = df.transpose()
## 2022년 중앙값 
df_median = df["2022년"].median()
## 중앙값보다 큰 값의 데이터 수 
len(df[df["2022년"] > df_median]) 
###(df["2022년"] > df_median).sum()


# Q. 결측치 데이터(행)을 제거하고, 앞에서부터 60% 데이터만 활용해, 'f1' 컬럼 3사분위 값을 구하시오
## 패키지 및 데이터 불러오기 
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
## 결측치 확인 및 행 제거 
df.isna().sum()
df2 = df.dropna()
## 60% 데이터 활용
df2 = df2[:int(len(df2)* 0.6)]
## 'f1'컬럼 3사분위 값을 구하시오
df2["f1"].quantile(0.75)


# Q. 결측치가 제일 큰 값의 컬럼명을 구하시오
## 패키지 및 데이터 불러오기
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
df.head()
## 결측치 확인 
df.isna().sum()
## 결측치가 제일 큰 값의 컬럼명 
# 방법1 
df2 = pd.DataFrame(df.isna().sum(),columns=["cnt_na"])
df2.sort_values("cnt_na",ascending=False)
df2.sort_values("cnt_na",ascending=False).index[0]
# 방법2
df2 = pd.DataFrame(df.isna().sum())
df2.reset_index().max()["index"]
