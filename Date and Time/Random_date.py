import random

from datetime import date,timedelta
start_date=date(2024,8,14)
last_date=date(2026,9,17)
k=7
result=[start_date]

while start_date!=last_date:
    start_date+=timedelta(days=1)
    result.append(result)
result=choices(result,k=k)
print(result)

