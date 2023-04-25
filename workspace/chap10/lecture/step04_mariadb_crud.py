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

    '''
    # (1) 테이블 생성
    sql = """create table goods(
                    code integer primary key,
                    name text(30) unique not null,
                    su integer default 0,
                    dan real default 0.0)"""

    cursor.execute(sql)
    '''

    # (2) 레코드 추가
    '''
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()  # db 반영

    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"

    cursor.execute(sql)
    conn.commit()       #db 반영
    '''

    # (2) code 이용 레코드 수정
    '''
    code = int(input('수정할 code 입력 : '))
    name = input('수정할 name 입력 : ')
    su = int(input('수정할 su 입력 : '))
    dan = int(input('수정할 dan 입력 : '))

    sql = f"update goods set name = '{name}', su ={su}, dan = {dan} where code = {code}"
    cursor.execute(sql)
    conn.commit()
    '''

    # (7) 레코드 삭제
    code = int(input('삭제할 code 입력 : '))
    sql = f"delete from goods where code = {code}"
    cursor.execute(sql)     # 삭제 반영
    rows = cursor.fetchall()

    for r in rows:
        #print(r)
        print('%d     %s        %d      %s' % r)
    print('레코드 삭제')

    sql = f"delete from goods where code = {code}"
    cursor.execute(sql)  # 삭제 반영
    conn.commit()

    '''
    # (3) 전체 목록 보기
    sql = "select * from goods"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for r in rows:
        # print(r)
        print('%d     %s        %d      %s'%r)
    print('검색 레코드 수 : ', len(rows))
    '''

    # (4) 상품명 조회
    name = input("\n조회할 상품명 입력 : ")
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)  # 조회
    rows = cursor.fetchall()

    if rows :
        for r in rows :
            print(r[0], r[1], r[2], r[3])
    else :
        print('해당 상품 없음')

except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()


