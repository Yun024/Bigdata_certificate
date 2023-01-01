# [1-1. age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력]
## 사용할 패키지 설치 및 데이터 불러오기
import pandas as pd
import math
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
## age컬럼의 3사분위수 
df["age"].quantile(0.75)
## age컬럼의 1사분위수
df["age"].quantile(0.25)
## age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력
math.floor(abs(df["age"].quantile(0.75) - df["age"].quantile(0.25)))
### int(abs(df["age"].quantile(0.75) - df["age"].quantile(0.25)))


# [1-2.(loves반응+wows반응)/(reactions반응) 비율이 0.4보다 크고 0.5보다 작으면서, status_type 컬럼이 'video'인 데이터의 갯수]
## 사용할 패키지 설치 및 데이터 불러오기 
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/fb.csv")
## status_type컬럼이 video인 데이터 추출 
df2 = df[df["type"]=="video"]
## (loves반응+wows반응)/(reactions반응)을 이용한 컬럼 생성
df2["new"] = (df2["loves"] + df2["wows"]) / df2["reactions"]
## 비율이 0.4보다 크고 0.5보다 작은 데이터의 갯수
len(df2[(df2["new"] > 0.4)& (df2["new"]<0.5)])
## 다른방법
df["new"] = (df["loves"]+df["wows"])/ df["reactions"]
len(df[(df["new"] >0.4) & (df["new"]<0.5)& (df["type"]=="video")])


# [1-3. date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수]
## 패키지 설치 및 데이터 불러오기 
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")
## date_added값이 NA인 데이터 제거 
df["date_added"].isna().sum()
df = df[df["date_added"].isna()==False]
df["date_added"].isna().sum()
## 1월 데이터 추출 
df2 = df[df["date_added"].str.contains("January")==True]
## 2018년 데이터 추출
df2 = df2[df2["date_added"].str.contains("2018")==True]
## country가 United Kingdom 단독 제작인 데이터의 갯수
len(df2[df2["country"] == "United Kingdom"])
## 다른 풀이1
df["date_added"] = pd.to_datetime(df["date_added"])
df["year"] = df["date_added"].dt.year
df["month"] = df["date_added"].dt.month
cond1 = df["country"]== "United Kingdom"
cond2 = df["year"] == 2018
cond3 = df["month"] == 1 
len(df[cond1 & cond2 & cond3])
## 다른 풀이2
df["date_added"] = pd.to_datetime(df["date_added"])
cond1 = df["date_added"] >= "2018-01-01"
cond2 = df["date_added"] <= "2018-01-31"
cond3 = df["country"]== "United Kingdom"
len(df[cond1 & cond2 & cond3])


# [1-4. 그런데 만약 'country'컬럼에 대소문자 함께 있고, 띄어쓰기가 있는 것도 있고 없는 것도 있다면?]
## 대문자로 통일
df2["country"] = df2["country"].str.upper()
## 띄어쓰기 제거로 통일
df2["country"] = df2["country"].str.replace(" ","")
## country가 United Kingdom 단독 제작인 데이터의 갯수
len(df2[df2["country"]=="UNITEDKINGDOM"])









