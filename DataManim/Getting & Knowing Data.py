# Q1. 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv",sep="\t")

# Q2. 데이터의 상위 5개 행을 출력하라
df.head()

# Q3. 데이터의 행과 열의 갯수를 파악하라
print("행,열:",df.shape)
print("행:",data.shape[0])
print("열:",data.shape[1])

# Q4.전체 컬럼을 출력하라
df.columns

# Q5. 6번째 컬럼명을 출력하라
df.columns[5]

# Q6. 6번째 컬럼의 데이터 타입을 확인하라
df.iloc[:,5].dtype

# Q7. 데이터셋의 인덱스 구성은 어떤가
df.index

# Q8. 6번째 컬럼의 3번째 값은 무엇인가?
df.iloc[:,5][2]

# Question 9. 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv",encoding="cp949")

# Question 10. 데이터 마지막 3개행을 출력하라
df.tail(3)

# Question 11. 수치형 변수를 가진 컬럼을 출력하라
df.describe().columns
## 데이터 타입이 오브젝트인 데이터 추출 exclude
df.select_dtypes(exclude=object).columns 

# Question 12. 범주형 변수를 가진 컬럼을 출력하라¶
df.select_dtypes(include=object).columns  
## 데이터 타입이 오브젝트인 데이터 추출 include

# Question 13. 각 컬럼의 결측치 숫자를 파악하라
df.isnull().sum()   # isna와 sum을 통해 결측치 숫자 파악이 가능 

# Question 14. 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라
df.info()

# Question 15. 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하라
df.describe()

# Question 16. 거주인구 컬럼의 값들을 출력하라¶
df["거주인구"]

# Question 17. 평균 속도 컬럼의 4분위 범위(IQR) 값을 구하여라
abs(df["평균 속도"].describe()["25%"] - df["평균 속도"].describe()["75%"])
df["평균 속도"].quantile(0.75) - df["평균 속도"].quantile(0.25)

# Question 18. 읍면동명 컬럼의 유일값 갯수를 출력하라
len(list(df["읍면동명"].unique()))
df["읍면동명"].nunique()

# Question 19. 읍면동명 컬럼의 유일값을 모두 출력하라
df["읍면동명"].unique()

















