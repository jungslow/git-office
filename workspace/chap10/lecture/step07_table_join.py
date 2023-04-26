import pymysql

config = {
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

    # (1) table join




    # (2) 레코드 조회




except Exception as e :
    print('db error : ', e)

finally:
    cursor.close()
    conn.close()
