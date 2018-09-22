import datetime, time
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(time.time())
print(time.asctime(time.localtime(time.time())))
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))
