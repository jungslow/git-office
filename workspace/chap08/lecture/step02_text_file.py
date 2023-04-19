# 현재 작업 디렉토리
import os
print('\n현재경로 : ', os.getcwd())

# 예외 처리
try :
    ftest1 = open('../data/ftest.txt', mode = 'r')
    print(ftest1.read())

    ftest2 = open('../data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~')

    ftest3 = open('../data/ftest2.txt', mode='a')
    ftest3.write('\nmy second text~~~')
except Exception as e:
    print("Error 발생 : ", e)

finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()

