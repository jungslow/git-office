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

    while True :  # 무한 루프
        print('\t[ 레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')
        menu_num = int(input('\t메뉴번호 입력 :'))

        if menu_num == 1:
            # 1. 레코드 조회
            sel = int(input('1. 전체조회,  2. 상품명 조회 :'))
            if sel == 1 :
                # 1) 전체 레코드 조회
                sql = "select * from goods"
                cursor.execute(sql)
                dataset = cursor.fetchall()

                for row in dataset :
                    print(row[0], row[1], row[2], row[3])

                print('검색된 레코드 수 :', len(dataset))

            elif sel == 2 :
                # (2) 상품명 조회
                name = input("\n조회할 상품명 입력 : ")
                sql = f"select from goods where name like '%{name}%'"
                cursor.execute(sql)
                dataset = cursor.fetchall()

                if dataset :
                    for row in dataset :
                        print(row)
                else :
                    print('검색된 레코드 없음')


        elif menu_num == 2 :
            # 2. 레코드 추가
            code = int(input('code 입력 : '))
            name = input('name 입력 : ')
            su = int(input('su 입력 : '))
            dan = int(input('dan 입력 : '))
            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            conn.commit()

        elif menu_num == 3:
            # 3. 레코드 수정
            code = int(input('수정 code 입력 : '))
            su = int(input('su 입력 : '))
            dan = int(input('dan 입력 : '))
            sql = f"update into goods set su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()

        elif menu_num == 4:
            # 4. 레코드 삭제
            code = int(input('삭제할 code 입력 : '))
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)
            conn.commit()

        elif menu_num == 5:
            print('프로그램 종료 : ')
            break

    else :
        print('해당 메뉴는 없습니다.')

except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
