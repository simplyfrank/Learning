from datetime import time, date, datetime

now = datetime.now()
print(now.year)
print(now.hour)
print(now.second)
print(now.minute)

print(date(2014, 5, 6))
print(date(year=2014, month=12, day=5))


print(date.fromtimestamp(10000000000))

print(date.today().isoformat())

d = datetime.now()
print(d.strftime('%A %d %B %Y'))

a = [(x,y) for x in range(10) for y in range(x)]
print(a)