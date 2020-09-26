sec = int(input())
minutes = int((sec / 60) % 60)
hours = int((sec / 3600) % 24)
sec = sec % 60

if sec < 10:
    sec = '0' + str(sec)

if minutes < 10:
    minutes = '0' + str(minutes)

print(str(hours) + ':' + str(minutes) + ":" + str(sec))
