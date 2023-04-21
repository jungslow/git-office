import os

print(os.getcwd())
print('='*55)

txt_data = 'D://hello-git//workspace/chap08/data/txt_data/'

# (2) 텍스트 디렉토리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)

# (3) 각 디렉토리의 텍스트 자료 수집 함수
def textPro(sub_dir) :
    first_txt = []
    second_txt = []

    for sdir in sub_dir :
        dirname = txt_data + sdir
#        print(dirname)
        file_list = os.listdir(dirname)
        print(file_list)

        for fname in file_list :
            file_path = dirname + '/' + fname

            if os.path.isfile(file_path):
                try :
                    file = open(file_path, 'r')
                    if sdir == 'first' :
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())

                except Exception as e :
                    print('예외 발생 :', e)
                finally :
                    file.close()

    return first_txt, second_txt

# (4) 함수 호출
first_txt, second_txt = textPro(sub_dir)

print("first_txt 길이 : ", len(first_txt))
print("second_txt 길이 : ", len(second_txt))

tot_texts = first_txt + second_txt
print("total_texts 길이 : ", len(tot_texts))

print(tot_texts)
print(type(tot_texts))

# 이진파일 형태로 저장, 처리
import pickle

txtt_data = 'D://hello-git//workspace/chap08/data/txt_data/tot_texts.pck'
pfile_w = open('txtt_data', mode = 'wb')
pickle.dump(tot_texts, pfile_w)

pfile_r = open('txtt_data', mode = 'rb')
tot_texts_read = pickle.load(pfile_r)

print("total_texts 길이 : ", len(tot_texts_read))

print(tot_texts_read)
print(type(tot_texts_read))







