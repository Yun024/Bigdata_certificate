# Question 20. 데이터를 로드하라.
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(DataUrl)

# Question 21. quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라
df[df["quantity"]== 3].head()

# Question 22. quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라
df[df["quantity"]== 3].reset_index(drop=True).head()

# Question 23. quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라
pd.concat([df["quantity"],df["item_price"]],axis=1)
df[["quantity","item_price"]]

# Question 24. item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라
df["new_price"] = df["item_price"].str.strip("$").astype(float)
df["new_price"] = df["item_price"].str[1:].astype(float)
df["new_price"]

# Question 25. new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라
len(df[df["new_price"]<=5])

# Question 26. item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라
df[df["item_name"]=="Chicken Salad Bowl"].reset_index(drop=True)

# Question 27. new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
df_use = df[df["new_price"]<=9]; df_use[df_use["item_name"]=="Chicken Salad Bowl"]
df[(df["item_name"]=="Chicken Salad Bowl") & (df["new_price"]<=9)]

# Question 28. df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
df.sort_values("new_price").reset_index(drop=True)

# Question 29. df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
## df[df["item_name"].str.find("Chips")== 0]/ find는 앞에 있는 경우만 찾아냄 
df[df["item_name"].str.contains("Chips")]

# Question 30. df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
df.iloc[:,::2]

# Question 31. df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
df.sort_values("new_price",ascending=False).reset_index(drop=True)

# Question 32. df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
df[(df["item_name"]=="Steak Salad") | (df["item_name"]=="Bowl")]

# Question 33. df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후,item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
df[(df["item_name"]=="Steak Salad") | (df["item_name"]=="Bowl")].drop_duplicates("item_name",keep="first")

# Question 34. df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
df[(df["item_name"]=="Steak Salad") | (df["item_name"]=="Bowl")].drop_duplicates("item_name",keep="last")

# Question 35. df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
df[df["new_price"]>= df["new_price"].mean()]

# Question 36. df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
df["item_name"]=df["item_name"].replace("Izze","Fizzy Lizzy")
df[df["item_name"]=="Izze"]

# Question 37. df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
df["choice_description"].isna().sum()

# Question 38. df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
## df["choice_description"].fillna("NoData")
df.loc[df["choice_description"].isna(),"choice_description"] = "NoData"
## df["choice_description"]

# Question 39. df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
df[df["choice_description"].str.contains("Black")]

# Question 40. df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
len(df[~df["choice_description"].str.contains("Vegetables")])

# Question 41. df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
df[df["item_name"].str.startswith("N")]

# Question 42. df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
temp = pd.DataFrame(index=range(len(df["item_name"])),columns=['column1'])
for i in range(len(df["item_name"])):
    if len(df["item_name"][i])>= 15:
        temp["column1"][i] = True
    else:
        temp["column1"][i] = False
df[temp["column1"]]
## df[df["item_name"].str.len() >=15]

# Question 43. df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
temp = []
for i in range(len(df["new_price"])):
    if df["new_price"][i] in lst:
        temp.append(True)
    else:
        temp.append(False)
len(df[temp])
## df[df["new_price"].isin(lst)]
