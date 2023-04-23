# (1) 패키지 import
import matplotlib.pyplot as plt
import random

# 음수 부호 지원
import matplotlib
plt.rcParams['axes.unicode_minus'] = False

# (3) 차트 자료 생성
print(random.randint(a=1, b=5))
print(random.random())
print(random.normalvariate(mu=0, sigma=1))

# (2 기본 차트 그리기
# (2-1) 1개 데이터
data = range(10)
plt.plot(data)
plt.plot(data, 'r+')
plt.show()

# (2-2) 2개 데이터
data2 = [random.random() for i in range(10)]
plt.plot(data, data2)
plt.plot(data, data2, 'bo')
plt.show()

# (3) 산점도 그리기
# (3-1) 단색 산점도
plt.scatter(x=data, y=data2, marker='o')
plt.show()

# (3-2) 여러 가지 색 산점도
cdata = [random.randint(a=1, b=3) for i in range(10)]
cdata
print(cdata)
plt.scatter(x=data, y=data2, c=cdata, marker='o')
plt.show()

# (4) 히스토그램
data3 =  [random.normalvariate(mu=0, sigma=1) for i in range(10000)]
plt.hist(data3) # 정규 분포
plt.show()

data4 =  [random.uniform(a=1, b=100) for i in range(10000)]
plt.hist(data4) # 균등 분포
plt.show()






