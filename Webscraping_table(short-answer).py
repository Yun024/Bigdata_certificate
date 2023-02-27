### 패키지 설치
from bs4 import BeautifulSoup as bs
import requests
from html_table_parser import parser_functions
import pandas as pd
import openpyxl
import os
# Python 설치 시 SSL인증서 관련 에러가 나는 경우 아래와 같은 명령어를 사용하여 문제를 해결 할 수 있음
#pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org xlwt
# 워링 경고문 없애주는 역할 
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
----------------------------------
----------------------------------
----------------------------------

### Web scraping
url = "https://5ohyun.tistory.com/113"
res = requests.get(url,verify=False)
res.raise_for_status()
soup  = bs(res.text,"lxml")
data = soup.find("table") ## 테이블 데이터
table = parser_functions.make2d(data) 

### 데이터 추출
short_answer =pd.DataFrame(data=table[1:],columns=table[0])
short_answer.to_excel("단답형_기출문제.xlsx",index=False)
