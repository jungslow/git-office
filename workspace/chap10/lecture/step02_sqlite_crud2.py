# sql 재미있게!!! 
import sqlite3
print(sqlite3.sqlite_version_info)


try :
    # db 연동 객체
    conn = sqlite3.connect('d:/hello-git/workspace/chap10/data10/sqlite_db')

    # sql 실행 객체
    cursor = conn.cursor()

    # (1 table 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0)"""

    cursor.execute(sql)  # sql 실행 ==> table 생성

    # (2) 레코드(행) 추가
    '''
    cursor.execute("insert into goods values(1, '냉장고', 2, 8500000)
    cursor.execute("insert into goods values(2, '세탁기', 3, 5500000)
    cursor.execute("insert into goods (code, name) values(3, '전자레인지')")
    cursor.execute("insert into goods (code, name, dan) values(4, 'HDTV', 1500000)")
    
    conn.commit()       # db 반영
    '''

    # (3) 레코드 조회
    sql = "select * from goods"
    cursor.execute(sql)
    rows = cursor.fetchall()    # 조회 레코드 가져 오기

    for row in rows :
        print(row[0], row[1], row[2], row[3])
    print('검색된 레코드 수 :', len(rows))

    # (5) 레코드 추가 : 2차
    '''
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))

    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()
    '''

    # (6) 레코드 수정 : code ==> su, dan 수정
    # (5) 단계 주석 처리
    '''
    code = int(input('수정 code 입력 : '))
    su = int(input('수정 su 입력 : '))
    dan = int(input('수정 dan 입력 : '))

    sql = f"update goods set su ={su}, dan = {dan} where code = {code}"
    cursor.execute(sql)
    conn.commit()
    '''

    # (7) 레코드 삭제
    '''
    code = int(input('삭제 code 입력 : '))
    sql = f"delete from goods where code = {code}"
    cursor.execute(sql)     # 삭제 반영
    conn.commit()           # db 반영
    '''

    # (4) 상품명 조회
    name = input("상품명 입력 : ")
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)     # 조회
    rows = cursor.fetchall()
    ...

    if rows :   # null ==> false
        for row in rows :
            print(row)
    else :
        print('검색된 레코드 없음')

except Exception as e :
    print('db 연동 error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
