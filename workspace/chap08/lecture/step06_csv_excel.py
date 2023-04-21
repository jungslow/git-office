# (1)
import pandas as pd
import os

# 현재 작업 디렉토리 확인
print(os.getcwd())

# (2) csv 화일 읽기
score = pd.read_csv('D:/hello-git/workspace/chap08/data/score.csv')
print(score.info())
print(score.head())

# (3) 칼럼 추출
kor = score.kor
eng = score.eng
mat = score['mat']
dept = score['dept']

# (4) 과목별 최고 첨수
print('max kor : ', max(kor))
print('max eng : ', max(eng))
print('max mat : ', max(mat))

# (5) 과목별 최하 첨수
print('min kor : ', min(kor))
print('min eng : ', min(eng))
print('min mat : ', min(mat))

# (6) 과목별 평균 점수
from statistics import mean
print('국어 점수 평균 :', round(mean(kor),3))
print('영어 점수 평균 :', round(mean(eng),3))
print('수학 점수 평균 :', round(mean(mat),3))

# (7) dept 빈도수
dept_count = {}     # dict 형
for key in dept :
    dept_count[key] = dept_count.get(key, 0) + 1

print(dept_count)
print("*"*55)

# (11) 엑셀 화일 읽기
import openpyxl
sam = pd.ExcelFile('D:/hello-git/workspace/chap08/data/sam_kospi.xlsx')

# (12) 엑셀 화일 파싱
kospi = sam.parse("sam_kospi")
print(kospi.info())

# (13) 칼럼 추출
high = kospi['High']
low = kospi['Low']

# (14) 평균 계산
from statistics import mean
print('high mean =', mean(high))
print('low  mean =', mean(low))

# (14) 평균 계산
from statistics import mean
print('High mean =', high.mean)
print('Low  mean =', low.mean)





