import os

print(os.getcwd())

txt_data = 'D://hello-git//Pywork//workspace/chap08/lecture/txt_data/'

sub_dir = os.listdir(txt_data)
print(sub_dir)

def textPro(sub_dir) :
    first_txt = []
    second_txt = []

    for  sdir in sub_dir :
        dirname = txt_data + sdir
        file_list = os.listdir(dirname)

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

first_txt, second_txt = textPro(sub_dir)

print("first_txt 길이 : ", len(first_txt))
print("second_txt 길이 : ", len(second_txt))

tot_texts = first_txt + second_txt
print("total_texts 길이 : ", len(tot_texts))

print(tot_texts)
print(type(tot_texts))


import pickle

pfile_w = open('D://hello-git//Pywork//workspace/chap08/lecture/txt_data/tot_texts.pck', mode = 'wb')
pickle.dump(tot_texts, pfile_w)

pfile_r = open('D://hello-git//Pywork//workspace/chap08/lecture/txt_data/tot_texts.pck', mode = 'rb')
tot_texts_read = pickle.load(pfile_r)

print("total_texts 길이 : ", len(tot_texts_read))

print(tot_texts_read)
print(type(tot_texts_read))







