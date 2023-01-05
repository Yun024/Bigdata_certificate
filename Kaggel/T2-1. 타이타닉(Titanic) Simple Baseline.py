# 생존여부 예측모델 만들기
# 학습용 데이터 (X_train, y_train)을 이용하여 생존 예측 모형을 만든 후, 이를 평가용 데이터(X_test)에 적용하여 얻은 예측값을 다음과 같은 형식의 CSV파일로 생성하시오

## 수치형 데이터 확인
X_train.describe().columns.tolist()
X_train.select_dtypes(exclude="object")

## 생존 비율 확인
y_train["Survived"].value_counts()

## 요약값 확인
X_train.describe(include="object")
X_train.describe(exclude="object")
X_train.isna().sum()

## 평균 생존률 비교 
z =pd.merge(X_train, y_train, on="PassengerId")
z[["Sex","Survived"]].groupby("Sex",as_index=False).mean()
z[["Pclass","Survived"]].groupby("Pclass",as_index=False).mean()

## 학습 데이터의 종속변수 추출
y = y_train["Survived"]

## 원핫 인코딩 실행
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(X_train[features])
test = pd.get_dummies(X_test[features])

## 랜덤포레스트 모델 피팅
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=200, max_depth=7, random_state=2021)
model.fit(X, y)
predictions = model.predict(test)
model.score(X, y)

## 결과물 확인
output = pd.DataFrame({'PassengerId': X_test.PassengerId, 'Survived': predictions})
output.head()

## csv파일 쓰기 
output.to_csv('1234567.csv', index=False)

## 결과 채점
model.score(test, y_test['Survived'])
