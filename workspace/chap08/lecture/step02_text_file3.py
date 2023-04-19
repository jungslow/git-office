# 현재 작업 디렉토리
import os
print('\n현재경로 : ', os.getcwd())

try :
    with open('../data/ftest3.txt', mode='w', encoding = 'utf-8') as ftest :
        ftest.write('파이썬 파일 작성 연습')
        ftest.write('\n파이썬 파일 작성 연습2 - Good luck!')
        # with 블록 벗어나면 파일은 자동으로 close
    with open('../data/ftest3.txt', mode='r', encoding = 'utf-8') as ftest :
        print(ftest.read())
except Exception as e :
    print('Error 발생 :', e)
finally :
    pass
