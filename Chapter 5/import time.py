from datetime import timedelta
import datetime

print("=======Special Day Anniversary========")
for item in range(1):
    year = int(input("Enter the year:"))
    month = int(input("Enter month:"))
    day = int(input("Enter the day:"))
    special_day = int(input("Enter the special day you want to count from Anniversary:"))
d= datetime.datetime(year,month,day)
delta = datetime.timedelta(special_day)

print("Your Special day:",d + delta)
