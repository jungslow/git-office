'''
csv ==> db table
    1st : table creation ==> record insertion
    2nd : query record
'''

import pandas as pd
import pymysql

bmi = pd.read_csv('D:/git_office/workspace/chap10/data10/bmi.csv')
print(bmi.info())
print(bmi.head())

# (2)  각 칼럼 추출
height = bmi['height']
weight = bmi['weight']
label = bmi['label']

config = {                      # DB 환경 변수 지정
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # (3) table 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()

    # (4) 스위칭 기법
    sw = False
    for table in tables :
        if table[0] == "bmi_tab" :
            sw = True

    # (5) table 생성
    if not sw :
        print('테이블 없음')
        sql = """create table bmi_tab(
        height int not null,
        weight int not null,
        label varchar(20) not null)"""
        cursor.execute(sql)

    # (6) 레코드 검색
    cursor.execute("select * from bmi_tab")
    rows = cursor.fetchall()

    if rows :   # (7) 레코드 있는 경우
        for row in rows :
            print(f"row[0] row[1] row[2]")
            print('전체 레코드 수 : ', len(rows))
    else : # (8) 레코드 없는 경우
        print('레코드 100개 추가')
        for i in range(100) :
            h = height[i]
            w = weight[i]
            lab = label[i]
            cursor.execute(f"insert into bmi_tab values({h}, {w}, '{lab}')")
            conn.commit()
except Exception as e :
    print('db error : ', e)

finally:
    cursor.close()
    conn.cursor()