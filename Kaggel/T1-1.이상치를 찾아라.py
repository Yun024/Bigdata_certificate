
## 라이브러리 및 데이터 불러오기
import pandas as pd
df = pd.read_csv("../input/titanic/train.csv")
df.head()

## 간단한 탐색적 데이터 분석 (EDA)
df.info()
print(df.describe())
df.isnull().sum()

## IQR 구하기
Q1 = df["Fare"].describe()["25%"]
Q3 = df["Fare"].describe()["75%"]
print("Q1:",Q1)
print("Q3:",Q3)

## 이상치 데이터 구하기
IQR = abs(Q1 - Q3)
lower = df[df["Fare"] < (Q1 - 1.5* IQR)]
upper = df[df["Fare"] > (Q3 + 1.5* IQR)]

## 이상치 데이터에서 여성 수 구하기, 출력하기 print()
print(len(upper[upper["Sex"]=="female"]))
upper[upper["Sex"]=="female"]
#df[(df["Fare"] < Q1 -1.5*IQR) | (df["Fare"] > Q3+ 1.5* IQR) & (df["Sex"]=="female")] 

