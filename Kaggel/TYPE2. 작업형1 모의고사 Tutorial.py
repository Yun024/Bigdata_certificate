#1번 index가 짝수인 행만(0포함) 선택해 "petal width (cm)" 값을 모두 더하시오
from sklearn.datasets import load_iris
dataset = load_iris()
data_df = pd.DataFrame(dataset.data, columns=dataset.feature_names )
data_df.to_csv("data.csv", index=False)
del data_df, dataset
df = pd.read_csv("data.csv")
df.iloc[::2,:]["petal width (cm)"].sum()

#2번  city를 기준으로 'f1'컬럼의 그룹합을 더한 뒤 그 값이 가장 큰 인덱스 명을 구하시오
import pandas as pd
df = pd.read_json(data)
df.groupby("city").sum()["f1"][df.groupby("city").sum()["f1"] == df.groupby("city").sum()["f1"].max()].index[0]

#3번  f1 컬럼 중 결측치가 있는 데이터를 선택하고, 그 데이터의 f5 컬럼 중앙값을 구하시오
import pandas as pd
df = pd.read_json(data)
df[df["f1"].isna()]["f5"].median()
