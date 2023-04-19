import datetime
from datetime import date, time

# help(date)

today = date(2019, 10, 23)
print(today)

print(today.year)
print(today.month)
print(today.day)

w = today.weekday()
print('요일 정보 : ', w)    # monday = 0, ...sunday = 6
print()

currTime = time(21, 4, 30)
print(currTime)

print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime = currTime.isoformat()  #HH:MM:SS
print(isoTime)

