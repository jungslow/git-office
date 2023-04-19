print('\n유형별 예외처리 ')
try :
    div = 1000/2.53
    print('div = %5.2f'%div)
#    div = 1000 / 0
#    f = open('C:\\test.txt')
    num = int(input('숫자를 입력해 주세요 : '))
    print('num =', num)
except ZeroDivisionError as e :
    print('오류 정보 : ', e)
except FileNotFoundError as e :
    print('오류 정보 : ', e)
except Exception as e :
    print('오류 정보 : ', e)
finally :
    print('finally 영역 - 항상 실행되는 영역')
