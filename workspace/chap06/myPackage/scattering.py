from statistics import mean
from math import sqrt

# data = [1, 3, 5, 7, 9, 15]

def Avg(data) :
    avg = mean(data)
    return avg

def var_sd(data) :
    avg = Avg(data)
    diff = [(d-avg)**2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd

# print("평균 = %.2f"%(Avg(data)))

# v, s = var_sd(data)
# print('분산 = ', v)
# print('표준편차 = ', s)

# 프로그램 시작점
if __name__ == "__main__" :
    data = [1, 3, 5, 7, 9, 15]

    print('평균 =', Avg(data))
    var, sd = var_sd(data)

    print('분산 = ', var)
    print('표준편차 = ', sd)


