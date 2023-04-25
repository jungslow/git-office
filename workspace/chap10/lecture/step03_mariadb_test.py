import pymysql
print(pymysql.version_info)

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}

try :
    # (3) db 연동 객체
    conn = pymysql.connect(**config)
    # (4) sql문 실행 객체
    cursor = conn.cursor()

    # (5) 테이블 조회
    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    # (6) 전체 table 목록 출력
    print(tables)

    # (7) Table 존재 유무 확인
    if tables :
        print('table 있음')
    else :
        print('table 없음')
except Exception as e :
    print('DB Error!!! : ', e)

finally :
    cursor.close()
    conn.close()
