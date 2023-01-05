# ## 1. 첫번째 데이터 부터 순서대로 50:50으로 데이터를 나누고, 
# ### 앞에서 부터 50%의 데이터(이하, A그룹)는 'f1'컬럼의 결측치를 A그룹의 중앙값으로 채우고, 
# ### 뒤에서부터 50% 데이터(이하, B그룹)는 'f1'컬럼의 결측치를 B그룹의 최대값으로 채운 후, 
# ### A그룹과 B그룹의 표준편차 합을 구하시오
# ### 단, 소수점 첫째자리까지 구하시오 (둘째자리에서 반올림)

wh = int(len(df)*0.5)
A = df.iloc[:wh,:]
B = df.iloc[wh:,:]
A["f1"] = A["f1"].fillna(A["f1"].median())
B["f1"] = B["f1"].fillna(B["f1"].max())
ans = A["f1"].std() + B["f1"].std()
round(ans,1)

## 2. 'f4'컬럼을 기준 내림차순 정렬과 'f5'컬럼기준 오름차순 정렬을 순서대로 다중 조건 정렬하고나서 
## 앞에서부터 10개의 데이터 중 'f5'컬럼의 최소값 찾고, 
## 이 최소값으로 앞에서 부터 10개의 'f5'컬럼 데이터를 변경함. 
## 그리고 'f5'컬럼의 평균값을 계산함
## 단 소수점 둘째자리까지 출력(셋째자리에서 반올림)

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df2 = df.sort_values(["f4","f5"],ascending=[False,True])
df_min = df2.iloc[:10,:]["f5"].min()
df2.iloc[:10,:]["f5"] = df_min
round(df2["f5"].mean(),2)

# ## 3. 'age' 컬럼의 IQR방식을 이용한 이상치 개수와 표준편차*1.5방식을 이용한 이상치의 개수를 더하시오
# - IQR방식 : Q1 - 1.5 * IQR, Q3 + 1.5 * IQR에서 벗어나는 영역을 이상치라고 판단함 
# - (Q1은 데이터의 25%, Q3는 데이터의 75% 지점임)
# - 표준편차*1.5방식: 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함
q1 = df["age"].quantile(0.25) 
q3 = df["age"].quantile(0.75)
IQR = q3 -q1
outlier1 = q1 - 1.5*IQR 
outlier2 = q3 + 1.5*IQR
df["age"].describe()
# cond1 = df["age"] < outlier1
# cond2 = df["age"] > outlier2
# df["age"][cond1 & cond2]
method_IQR = len(df["age"][(df["age"]< outlier1)| (df["age"] > outlier2)])


age_mean = df["age"].mean()
outlier3 = age_mean - df["age"].std() * 1.5
outlier4 = age_mean + df["age"].std() * 1.5
method_std = len(df["age"][(df["age"] < outlier3) | (df["age"] > outlier4)])

method_std + method_IQR
