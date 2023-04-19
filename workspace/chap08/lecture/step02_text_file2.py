# 현재 작업 디렉토리
import os
print('\n현재경로 : ', os.getcwd())

# 예외 처리
try :
    # (1) 전체 텍스트 자료 읽기
    ftest = open('../data/ftest.txt', mode = 'r')
    full_txt = ftest.read()
#    print(full_txt)
#    print(type(full_txt))

    # (2) 전체 텍스트 줄단위 읽기
    ftest = open('../data/ftest.txt', mode = 'r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단 수 :', len(lines))

    # (3) 문장 추출
    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)
    print(type(docs))

    # (4) 한줄 읽기
    ftest = open('../data/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))

    # (5) 6줄 전체를 한 줄씩 읽기
    ftest = open('../data/ftest.txt', mode='r')
    for i in range(6):
        line = ftest.readline()
        line_strip = line.strip()
        print(line_strip)
#    print(type(line_strip))

except Exception as e:
    print("Error 발생 : ", e)

finally:
    ftest.close()

try :
    with open('../data/ftest3.txt', mode='w', encoding = 'utf-8') as ftest :
        ftest.write('파이썬 파일 작성 연습')
        ftest.write('\n파이썬 파일 작성 연습2')
        # with 블록 벗어나면 파일은 자동으로 close
    with open('../data/ftest3.txt', mode='r', encoding = 'utf-8') as ftest :
        print(ftest.read())
except Exception as e :
    print('Error 발생 :', e)
finally :
    pass