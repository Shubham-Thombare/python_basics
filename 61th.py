# dates & times

import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

#print(today)
#print(time)
#print(now)

target_date = datetime.datetime(2026, 1, 2, 12, 30, 2)
current_date = datetime.datetime.now()

if target_date > current_date:
    print("The target date is in the future")
else:
    print("The target date is in the past")
