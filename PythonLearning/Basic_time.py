import datetime as dt
now=dt.datetime.now()

print str(now)
print now.strftime ('%a,%d %B %Y')
timevalue=now+dt.timedelta(hours=2)
print str(timevalue)

