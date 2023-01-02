# Question 64. 데이터를 로드하고 각 열의 데이터 타입을 파악하라
DataUrl = "https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv"
df = pd.read_csv(DataUrl)
df.info()

# Question 65. Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df["Yr_Mo_Dy"] = pd.to_datetime(df["Yr_Mo_Dy"])
df = pd.read_csv(DataUrl,parse_dates=["Yr_Mo_Dy"])
df["Yr_Mo_Dy"]

# Question 66. Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
df["Yr_Mo_Dy"].dt.year.unique()

# Question 67. Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
def fix_year(x):
    year = x.year - 100 if x.year>=2061 else x.year
    return(pd.to_datetime(datetime.date(year,x.month,x.day)))

df["Yr_Mo_Dy"] = df["Yr_Mo_Dy"].apply(lambda x: fix_year(x))

# Question 68. 년도별 각컬럼의 평균값을 구하여라
df["year"] = df["Yr_Mo_Dy"].dt.year
df.groupby("year").mean()

# Question 69. weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
df["weekday"] = df["Yr_Mo_Dy"].dt.dayofweek

# Question 70. weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
df["WeekCheck"] = df["weekday"].apply(lambda x: 1 if x>4 else 0)
df["WeekCheck"].value_counts()

# Question 71. 년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
df["month"] = df["Yr_Mo_Dy"].dt.month
df.groupby("month").mean()

# Question 72. 모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
df = df.fillna(method="ffill").fillna(method="bfill")
df.isna().sum()

# Question 73. 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
df["year"] = df["Yr_Mo_Dy"].dt.year
df["month"] = df["Yr_Mo_Dy"].dt.month
df.groupby(["year","month"],as_index=False).mean()
df.groupby(df["Yr_Mo_Dy"].dt.to_period("M")).mean()

# Question 74. RPT 컬럼의 값을 일자별 기준으로 1차차분하라
df["RPT"].diff()

# Question 75. RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라
df[["RPT","VAL"]].rolling(7).mean()
