lst = [1, 3, 5]
for i, c in enumerate(lst) :
    print("색인 : ", i, end= ', ')
    print('내용 :', c)

dit = {'name' : '홍길동', 'job' : '회사원', 'addr' : '서울시'}
for i, k in enumerate(dit) :
    print('순서 :', i, end =', ')
    print('키 :', k, end =', ')
    print('값 :', dit[k])