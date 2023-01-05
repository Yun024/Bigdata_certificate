### 패키지 불러오기
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

### EDA
X_train.describe(include="O") # 오브젝트 컬럼 없음 
X_train.isna().sum() # na값 없음
X_train.describe()

### 데이터 전처리
## 이상치 처리 (Glucose, BloodPressure, SkinThickness, Insulin, BMI가 0인 값)
col = ["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]
for i in range(5):
    print(len(X_train[col[i]][X_train[col[i]]==0]))
for i in range(5):
    print(len(X_test[col[i]][X_test[col[i]]==0]))
del_idx = X_train[col[0]][X_train[col[0]]==0].index.tolist()
X_train[~X_train.index.isin(del_idx)]
X_train = X_train.drop(del_idx)
y_train = y_train.drop(del_idx)
cols_mean = X_train[col[1:]].median()
X_train[col[1:]] =  X_train[col[1:]].replace(0,cols_mean)

X_train.drop("id",axis=1)
X_train = X_train.drop("id",axis=1)
target = y_train["Outcome"]
test_id = X_test.pop("id")

### 모델링
model = RandomForestClassifier()
model.fit(X_train,target)
pred=model.predict(X_test)
output = pd.DataFrame({"ID":test_id, "Outcome":pred})
output.to_csv("132345.csv",index=False)
model.score(X_test,y_test["Outcome"])
