import sys
today_eat = 1
for day in range(9, 0, -1):
    lastday_eat = (today_eat + 1) * 2
    today_eat = lastday_eat
print lastday_eat

    
