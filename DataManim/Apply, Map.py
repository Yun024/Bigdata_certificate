# Question 56. 데이터를 로드하고 데이터 행과 열의 갯수를 출력하라
DataUrl = "https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv"
df = pd.read_csv(DataUrl,index_col=0)
df.shape

# Question 57 Income_Category의 카테고리를 map 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
# Unknown : N ; Less than  40𝐾:𝑎; 40K -  60𝐾:𝑏; 60K -  80𝐾:𝑐; 80K -  120𝐾:𝑑; 120K +’ : e ;
sorted(df["Income_Category"].unique())
dic = {'Unknown': "N",
      "Less than $40K": "a",
      "$40K - $60K": "b",
      '$60K - $80K': "c",
      '$80K - $120K': "d",
      '$120K +': "e"}
df["New Income"]=df["Income_Category"].map(lambda x: dic[x])

# Question 58. Income_Category의 카테고리를 apply 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
# Unknown : N Less than  40𝐾:𝑎 40K -  60𝐾:𝑏 60K -  80𝐾:𝑐 80K -  120𝐾:𝑑 120K +’ : e
sorted(df["Income_Category"].unique())
dic = {'Unknown': "N",
      'Less than $40K': "a",
      '$40K - $60K': "b",
      '$60K - $80K': "c",
      '$80K - $120K': "d",
      '$120K +': "e"}
df["new_income"] = df["Income_Category"].apply(lambda x: dic[x])

# Question 59. Customer_Age의 값을 이용하여 나이 구간을 AgeState 컬럼으로 정의하라.
# (09 : 0 , 1019 :10 , 20~29 :20 … 각 구간의 빈도수를 출력하라
df["new_age"] = df["Customer_Age"].apply(lambda x: x//10* 10)
df["new_age"].value_counts().sort_index()

# Question 60. Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼을 정의하고 빈도수를 출력하라
df["newEduLevel"] = df["Education_Level"].str.contains("Graduate").astype(int)
df["newEduLevel"].value_counts()
df["Education_Level"].str.contains("Graduate").apply(lambda x: 1 if x==True else 0).value_counts()

# Question 61. Credit_Limit 컬럼값이 4500 이상인 경우 1 그외의 경우에는 모두 0으로 하는 newLimit 정의하라. newLimit 각 값들의 빈도수를 출력하라¶
df["newLimit"] =df["Credit_Limit"].apply(lambda x:1 if x>=4500 else 0)
df["newLimit"].value_counts()
(df["Credit_Limit"]>=4500).astype(int).value_counts()

# Question 62. Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1, 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라. newState의 각 값들의 빈도수를 출력하라
cond1 = df["Marital_Status"]=="Married"
cond2 = df["Card_Category"]=="Platinum"
(cond1 & cond2).astype(int).value_counts()
df.apply(lambda x: 1 if x["Marital_Status"]=="Married" and x["Card_Category"]=="Platinum" else 0, axis=1).value_counts()        

# Question 63. Gender 컬럼값 M인 경우 male F인 경우 female로 값을 변경하여 Gender 컬럼에 새롭게 정의하라. 각 value의 빈도를 출력하라
df["Gender"].apply(lambda x: "male" if x=="M" else "female").value_counts()

