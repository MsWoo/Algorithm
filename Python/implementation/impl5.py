yoil = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1,d1,m2,d2 = map(int, input().split())

flag = 0
month = m1
day = d1
idx=0

if m2 < m1 or (m2 == m1 and d2<d1):
    flag = 1

while True:
    if flag == 0:
        if month == m2 and day == d2:
            break
        day+=1
        idx+=1
        if day > num_months[month]:
            month+=1
            day=1
        if idx > 6 :
            idx = 0
    else:
        if month == m2 and day == d2:
            break
        day-=1
        idx-=1
        if day == 0:
            month-=1
            day=num_months[month]
        if idx == -8 :
            idx = 6
print(yoil[idx])