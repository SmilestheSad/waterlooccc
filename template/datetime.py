from datetime import datetime,date,time,timedelta

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2010-01-01 17:31:22', fmt) #datatime object
d2 = datetime.strptime('2012-01-11 18:31:22', fmt) #datatime object
d1String = d1.strftime(fmt)

timeDiff = timedelta(days=1,hours=2,minutes=10)
vDatetime1 = datetime(2017,10,8,10,56)
vDatetime2 = datetime(2017,12,8,11,56)
vDate = date(2017,12,8)
vTime = time(10,11)
vTime2 = time(12)
s = vTime2.minute

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print((d2-d1).seconds + (d2-d1).days*24*3600)  #output 867600
print(d1 + timeDiff) # output 2010-01-02 19:41:22
print(d2.timestamp()-d1.timestamp()) # output 867600.0

#4 January Jan Friday Jan PM
print(d1.weekday() , d1.strftime("%B"),d1.strftime("%b"),d1.strftime("%A"),d1.strftime("%b"),d1.strftime("%p")) 

# Output 2010 1 1 17 31 22
print(d1.year,d1.month,d1.day,d1.hour,d1.minute,d1.second) 
#2010 10 01 31 17 00
print(d1.strftime("%Y"),d1.strftime("%y"),d1.strftime("%m"),d1.strftime("%M"),d1.strftime("%H"),d1.strftime("%W"))

print(d1.timetuple())  #time.struct_time(tm_year=2010, tm_mon=1, tm_mday=1, tm_hour=17, tm_min=31, tm_sec=22, tm_wday=4, tm_yday=1, tm_isdst=-1)
print(d1.timetuple().tm_hour)  # output 17


