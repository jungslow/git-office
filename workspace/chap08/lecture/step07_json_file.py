import json

# (1) json 인코딩
user = {'id':1234, 'name':'홍길동'}
print(type(user))
print(user['name'])

# (2) json 인코딩
jsonString = json.dumps(user, ensure_ascii=False)
# ASCII 인코딩 방식 적용 안함

# 문자열 출력
print(jsonString)
print(type(jsonString))
#print(jasonString['name'])

# (3) json 디코딩
pyObj = json.loads(jsonString)
print(type(pyObj))

# (4) Dict 자료 확인
print(pyObj['name'])
for key in pyObj :
    print(key, ':', pyObj[key])
print('='*60)

# (5) json 파일 읽기
file = open('D:/git_office/workspace/chap08/data/usagov_bitly.txt', mode = 'r', encoding = 'utf-8')
lines = file.readlines()

# (6) json 디코딩(json파일 ==> python dict로)
rows = [json.loads(row) for row in lines]
print('rows : ', len(rows))

for row in rows[:10] :
    print(row)
    print(type(row))
file.close()

# (7) dict ==> DataFrame 변환
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info())









