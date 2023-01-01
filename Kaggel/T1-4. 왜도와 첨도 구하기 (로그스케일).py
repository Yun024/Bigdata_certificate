# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")
df

# 'SalePrice'컬럼 왜도와 첨도계산 
df_skew =  df["SalePrice"].skew()
df_kurt =  df["SalePrice"].kurt()
print("왜도:",df_skew)
print("첨도:",df_kurt)
df["SalePrice"].describe()

# 'SalePrice'컬럼 로그변환
df["SalePrice"] = np.log(df["SalePrice"])
df["SalePrice"].describe()

# 'SalePrice'컬럼 왜도와 첨도계산 
df_log_skew =  df["SalePrice"].skew()
df_log_kurt =  df["SalePrice"].kurt()
print("왜도:",df_log_skew)
print("첨도:",df_log_kurt)

# 모두 더한 다음 소수점 둘째 자리에서 출력
round(df_skew + df_kurt + df_log_skew + df_log_kurt,2)
