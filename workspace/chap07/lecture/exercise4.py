from re import findall
from statistics import mean

emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def pay_pro(x):
    from statistics import mean
    import re

    tmp = [re.findall('[가-힣]{3}', user) for user in x]
    name = [user[0] for user in tmp]
    print(tmp)

    pay = []
    tmp = [re.findall('[가-힣]{3}[0-9]{3}', user) for user in x]
    print(tmp)

    for user in tmp :
        str_user = user[0]
        print(str_user)
        pay.append(int(re.findall(r'\d+', str_user)))

    pay_avg = mean(pay)
    print('전체 급여 평균 :%d'%pay_avg)

    print('평균 아상 급여 수령자')
    for i in range(len(x)):
        if pay[i] >= pay_avg:
            print(name[i], '==>', pay[i])

pay_pro(emp)
