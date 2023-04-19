# (1) 예외 발생 가능한 코드

x = [10, 30, 25.2, 'num', 14, 0, 'jj', 51]

#for i in x:
#    print(i)
#    y = i**2  # 예외 발생 가능
#    print('y =', y)

#print('플로그램 종료')

# 예외 처리 코드
print('프로그램 시작 !!!')
for i in x:
    try :
        y = i ** 2  # 예외 발생 가능
        print('i=', i, ', y=', y)
    except :
        print('숫자 아님 : ', i)

print('프로그램 종료')