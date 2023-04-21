import os
from glob import glob # *, ? 파일 검색

# (1) image 파일 경로
print(os.getcwd())

img_path = 'D:\hello-git\workspace\chap08\image12\images'
img_path2 = 'D:\hello-git\workspace\chap08\image12\images2'

# (2) 디렉토리 존재 유무 확인
if os.path.exists(img_path) :
    print('해당 디렉토리가 존재함')

    images = []
    os.mkdir(img_path2)

    os.chdir(img_path)
    print(os.getcwd())

    img_path_set = glob('*.png')
    print(len(img_path_set))

    for pic_path in img_path_set :

        img_path = os.path.split(pic_path)
        print(img_path)
        images.append(img_path[1])
        print(images)

        rfile = open(pic_path, mode ='rb')
        output = rfile.read()

        wfile = open(img_path2+img_path[1], mode ='wb')

        wfile.write(output)
        rfile.close()
        wfile.close()
else :
    print('해당 디렉토리가 없음')

print('png file : ', images)
