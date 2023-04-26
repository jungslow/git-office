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
    pay = int(input('join 급여 입력 :'))
    sql = f"""select e.eno, e.ename, e.pay, d.dname, d.daddr
              from emp e inner join dept d
              on e.dname = d.dname and e.pay >= {pay}"""

    # (2) 레코드 조회
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data :
        print(row[0], row[1], row[2], row[3], row[4])
    print('검색된 레코드 수 : ', len(data))

except Exception as e :
    print('db error : ', e)

finally:
    cursor.close()
    conn.close()
