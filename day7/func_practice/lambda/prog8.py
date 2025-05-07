
from datetime import datetime
from datetime import date
date1 = date('2020-01-15 09:03:32:744178')
new_date = datetime.fromisoformat(date1)

#year = (lambda x : datetime.date(x))
#print(year(new_date))
month = (lambda x : x.month())
print(month(date1))
#date = (lambda x : datetime.datetime.date(x))
#print(date(new_date))
time = (lambda x : datetime.time(x))
print(time(new_date))
