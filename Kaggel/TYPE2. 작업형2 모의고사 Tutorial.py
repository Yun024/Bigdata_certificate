# 대학원 입학 예측(회귀)
# 예측할 값(target): "Chance of Admit "
# 평가: r2
# data(3개): t2-2-X_train, t2-2-y_train, t2-2-X_test
# 제출 형식(Serial No.-> id, 예측 값 -> target)

######## 전처리
# 라이브러리 불러오기
import pandas as pd
import numpy as np

# 데이터 불러오기
X_train = pd.read_csv("../input/big-data-analytics-certification/t2-2-X_train.csv")
y_train = pd.read_csv("../input/big-data-analytics-certification/t2-2-y_train.csv")
X_test = pd.read_csv("../input/big-data-analytics-certification/t2-2-X_test.csv")

X_train.shape, y_train.shape, X_test.shape


X_train.isna().sum()
X_test.isna().sum()
y_train["Chance of Admit "].value_counts()

X_train.info()
X_train.describe()

cat = pd.concat([X_train[["Research"]],X_test[["Research"]]])



from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
zz = ohe.fit_transform(cat[["Research"]])
zz = pd.DataFrame(zz,columns=["Research_0","Research_1"])

train_cat = zz.iloc[:len(X_train),:]
test_cat = zz.iloc[len(X_train):,:].reset_index(drop=True)

train_id = X_train["Serial No."].copy()
test_id = X_test["Serial No."].copy()

X_train = X_train.drop(["Research","Serial No."],axis=1)
X_test = X_test.drop(["Research","Serial No."],axis=1)

X_train = pd.concat([X_train,train_cat],axis=1)
X_test = pd.concat([X_test,test_cat],axis=1)

######## 모델링
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor

model_list = [RandomForestRegressor,ExtraTreesRegressor,BaggingRegressor,
              GradientBoostingRegressor,AdaBoostRegressor,VotingRegressor,
             StackingRegressor,HistGradientBoostingRegressor]

from sklearn.model_selection import train_test_split
x_tr,x_val,y_tr,y_val = train_test_split(X_train,y_train,test_size=0.2,random_state=2022)

try:
    for i in model_list:
        model = i()
        model.fit(x_tr,y_tr["Chance of Admit "])
        pred = model.predict(x_val)
        print(i,model.score(x_val,y_val["Chance of Admit "]))
except:
    pass

    
model = GradientBoostingRegressor()
model.fit(X_train,y_train["Chance of Admit "])
pred = model.predict(X_test)
output = pd.DataFrame({"id": test_id,"target": pred})
output.to_csv("145325.csv",index=False)
print(output)
