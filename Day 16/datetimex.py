# import datetime
from datetime import datetime, time, timedelta
import pytz
import time as sleepTime

print(dir())
print(dir(datetime))

now = datetime.now()
print(now)
print('*' * 50)
print(dir(now))
print('*' * 50)
print(now.day)
print(now.year)
print(now.month)
print(now.second)
print(now.timestamp())
print(now.weekday())

print(datetime.today().strftime('%a'))
print(datetime.today().strftime('%A'))

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)  # 1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0


now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

date_string = "5 December- 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B- %Y")
print("date_object =", date_object)


# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)


today = datetime(year=2000, month=1, day=1)
new_year = datetime(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)


t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
# Time left for new year: 26 days, 23: 01: 00
print('Time left for new year:', diff)


t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t1 =", t1)
print("t2 =", t2)
print("t3 =", t3)


# Using current time
ini_time_for_now = datetime.now()
# printing initial_date
print("initial_date", str(ini_time_for_now))
# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + \
    timedelta(days=730)

future_date_after_2days = ini_time_for_now + \
    timedelta(days=2)

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))

print(datetime.now())

print(timedelta(hours=5, minutes=30) - timedelta(hours=3, minutes=20))

t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("total seconds =", t.total_seconds())


date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# The strptime() method creates a datetime
# The strftime() method is defined under classes date, datetime and time.


local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


print("Printed immediately.")
sleepTime.sleep(2.4)
print("Printed after 2.4 seconds.")
