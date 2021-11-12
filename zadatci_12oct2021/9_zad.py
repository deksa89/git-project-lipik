"""import datetime
a = int(input("Unesi neki broj: "))

if a < 86400:
    print(datetime.timedelta(seconds = a))"""

a = int(input("Unesi neki broj: "))
if a < 86400:
    m, s = divmod(a, 60)
    h, m = divmod(m, 60)

print(f'{h:d}:{m:02d}:{s:02d}')






