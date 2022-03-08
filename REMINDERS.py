
# import REMINDERS as reminders
# reminders.reminder()

# import REMINDERS as reminders
# datetimeString = reminders.toReadableDatetime(datetime)
# datetime = reminders.toRegularDatetime(datetimeString)

# y, m, d, h, m1, s = varsFromDatetime(datetime)
# y, m, d, h, m1, s = varsFromDatetimeString(datetimeString = "2009-10-05 18:00:00")

# dt = reminders.createAdateTime(y=2022,m=1,d=1,h=18,m1=00,s=00)

# dateTimeStr = reminders.getTimeAndDateAMPM()



#----------------------

"""
# Simple Reminder System - Schedule Reminders

import time
time.sleep(5*60) #every 5 minutes, check if it's this time and date:
# set time and date for each reminder
timeAndDate = "2/3/2022 at 3:00 pm"
# set message of reminder
reminderMessage = "This is the reminder message"
# set any other actions that go with reminder

# gui that displays the pop-up window ready
# import GuiAPPs as apps
# apps.note("Hello World")

# email the reminders
# import SendAnEMAIL as email
# email.sendAnEMAIL(message_body,subject1,to_who,from_who)

# 1 file, reminders.txt, put the reminder note storage
# reminder date-time + message + reminder schedule
["10/12/2022 at 1:00 pm"],["Happy Birthday"],["7 d", "6 d", "5 d", "4 d", "3 d", "2 d", "1 d", "4 h", "2 h", "1 h", "30 m", "15 m", "0 m"]
["2/4/2022 at 11:25 pm"],["Quick Reminder"],["2 h", "1 h", "30 m", "15 m", "0 m"]


"""


# import REMINDERS as r
# r.remindersON()
def remindersON():
  import REMINDERS as r
  import time
  while True:
    r.remind()
    time.sleep(60)



# import REMINDERS as r
# r.remind()

# reminders.txt
# 10/12/2022 at 1:00 pm|Happy Birthday|7 d, 6 d, 5 d, 4 d, 3 d, 2 d, 1 d, 4 h, 2 h, 1 h, 30 m, 15 m, 0 m
# 2/4/2022 at 12:10 pm|Quick Reminder|2 h, 1 h, 30 m, 15 m, 0 m
def remind():
  import OPENsomething as open
  import REMINDERS as r

  filename = "reminders.txt"
  lines = open.readFile(filename) # array of lines
  #print(f"lines ({len(lines)}): {lines}")

  count = 1
  for line in lines:
    #print(f"line ({len(line)}): {line}")
    parts = line.split("|")
    datetime_string = parts[0]
    # NEED THIS TO BE A DATETIME:
    datetime = r.toRegularDatetime(datetime_string)
    print(f"\n\nTHE DATETIME STRING = {datetime_string} / datetime: {str(datetime)}")
    print(f"\n{count}) reminder part 1 (datetime_string): {datetime_string} ... datetime: {datetime}") #date
    message = parts[1]
    print(f"reminder part 2: (message): {message}") #message
    when = parts[2].split(", ") #remind when
    #
    # loop through all the times to remind for one reminder note
    #
    for w1 in when: # like - 2 d, 1 d, 2 h, 1 h, 30 m, 15 m, 0 m
      w = w1.split(" ")
      num = w[0] #number of how many min/hours/days before
      timeType = w[1] # 'm', 'h', 'd' # min/hours/days - designation
      print(f"reminder when part: {w}")
      message2 = message + f" ... {num}{timeType}" #add the type of reminder
      if timeType=="d":
        print(f"Remind: {num} days before ... {datetime} ... otherTime: {r.otherTime(num,timeType,datetime)}")
        #y, m, d, h, m1, s = r.varsFromDatetimeString(r.otherTime(num,timeType,datetime))
        r.ifTimeShowReminder2(r.otherTime(num, timeType, datetime), message=message2) # y=y, m=m, d=d, h=h, m1=m1, s=s
      if timeType=="h":
        print(f"Remind: {num} hours before ... {datetime} ... otherTime: {r.otherTime2(num,timeType,datetime)}")
        r.ifTimeShowReminder2(r.otherTime(num, timeType, datetime), message=message2)
      if timeType=="m":
        print(f"Remind: {num} minutes before ... {datetime} ... otherTime: {r.otherTime2(num,timeType,datetime)}")
        r.ifTimeShowReminder2(r.otherTime(num, timeType, datetime), message=message2)
      #check which reminders it can show - if any
    count += 1
  # it keeps running # checks every minute









# import REMINDERS as reminders
# result = reminders.isItSameMinuteAsNow(datetime) #returns True or False

def isItSameMinuteAsNow(datetime1):
  import datetime, time
  now = datetime.datetime.now()  # print(t1 > t2)
  now = now.replace(second=0, microsecond=0)  # same minute
  print(now)
  print(datetime1)
  if datetime1==now:
    return True
  else:
    return False


#--------------------------------------------------------
# if it's the same minute as now, show the reminder
#--------------------------------------------------------
# easy way to compare date and hour/min - no second
# see if it is the same - down to the minute
#

# import REMINDERS as reminder
# reminder.ifTimeShowReminder2(datetimeString,message="Time to brush your teeth")

def ifTimeShowReminder2(datetimeString="2022-10-12 14:00:00",message="Hello World"):
    import REMINDERS as r
    import GuiAPPs as apps
    import sayTHIS as say
    import SendAnEMAIL as e
    import datetime
    datetimeString = str(datetimeString)
    print(f"\n\n---MESSAGE---: {message}\n\n")
    nowDatetime1 = datetime.datetime.now()
    nowDatetime1 = nowDatetime1.replace(second=0, microsecond=0) #same minute
    #import REMINDERS as r
    y, m, d, h, m1, s = r.varsFromDatetimeString(datetimeString)
    print("6 datetime vars:")
    print(y, m, d, h, m1, s)
    nowDatetime2 = r.createAdateTime(y=int(y),m=int(m),d=int(d),h=int(h),m1=int(m1),s=int(s))
    print(f"nowDatetime1: {nowDatetime1} ... nowDatetime2: {nowDatetime2}")
    if nowDatetime1==nowDatetime2:
        print("THEY ARE THE SAME!")
        print("SHOW THE REMINDER!!!")
    result = r.isItSameMinuteAsNow(nowDatetime2) #returns True or False
    print(f"result: {result}")
    if result==True:
        #import GuiAPPs as apps
        apps.note(message)
        #import sayTHIS as say
        say.say(message)
        # ------------------------
        # send an email
        to_who = from_who = "myvortexlife1012@gmail.com"  # Enter receiver address
        body = str(message)+"\n\n\n"+str(nowDatetime1)
        subject1 = "Reminder from Python - " + str(message)
        # import SendAnEMAIL as e
        e.sendEmail2(body,subject1,to_who,from_who)
        # ------------------------

    #minutes_diff = (nowDatetime1 - nowDatetime2).total_seconds() / 60.0
    #import REMINDERS as r



# import REMINDERS as reminder
# reminder.ifTimeShowReminder(y=2022,m=2,d=4,h=21,m1=00,s=00,message="Time to brush your teeth")

def ifTimeShowReminder(y=2022,m=2,d=4,h=20,m1=51,s=00,message="Hello World"):
    import REMINDERS as r
    import datetime
    nowDatetime1 = datetime.datetime.now()
    nowDatetime1 = nowDatetime1.replace(second=0, microsecond=0) #same minute
    nowDatetime2 = r.createAdateTime(y=int(y),m=int(m),d=int(d),h=int(h),m1=int(m1),s=int(s))
    print(f"nowDatetime1: {nowDatetime1} ... nowDatetime2: {nowDatetime2}")
    if nowDatetime1==nowDatetime2:
        print("THEY ARE THE SAME!")
        print("SHOW THE REMINDER!!!")
    result = r.isItSameMinuteAsNow(nowDatetime2) #returns True or False
    print(f"result: {result}")
    if result==True:
        import GuiAPPs as apps
        apps.note(message)
    #minutes_diff = (nowDatetime1 - nowDatetime2).total_seconds() / 60.0
    #import REMINDERS as r

#use this for each amount of time before - the reminders
# import REMINDERS as r
# r.ifTimeShowReminder(y=2022,m=2,d=4,h=21,m1=00,s=00,message="Time to brush your teeth")






# timeType is only 3, d, h, m ... day, hour, minute
# creates datetimes for past times - for reminding
def otherTime2(n, timeType, datetime1):
  datetime = otherTime(n, timeType, datetime1)
  readable = toReadableDatetime(datetime)
  return readable



#timeType is only 3, d, h, m ... day, hour, minute
#creates datetimes for past times - for reminding
def otherTime(n,timeType,datetime1):
  from datetime import datetime, timedelta
  n = int(n)

  if timeType == "d":
    newDatetime = datetime1 - timedelta(days=n)
  elif timeType == "h":
    newDatetime = datetime1 - timedelta(hours=n)
  elif timeType == "m":
    newDatetime = datetime1 - timedelta(minutes=n)
  return newDatetime



#----------------------------------

# import REMINDERS as reminders

def datetimeStringToDatetime(datetime1): # 2022-10-12 14:00:00
  str = datetime1.split(" ")
  date = str[0]
  d = date.split("-")
  print("date-split:")
  print(d)
  m = d[0]
  d = d[1]
  y = date.split("-")[2]
  time2 = str[1]
  t = time2.split(" ")
  h = t[0].split(":")[0]
  h = int(h)
  m1 = t[0].split(":")[1]
  dt = createAdateTime(y,m,d,h,m1)
  return dt


#------------------------------------------


# import REMINDERS as reminders
# datetimeString = reminders.toReadableDatetime(datetime)
def toReadableDatetime(datetime):
  print(f"is this a string?: It shouldn't be: {isString(datetime)}")
  var = notReadableDatetimeToReadable(datetime) # 2022-10-12 14:00:00
  print(f"var - to dt: {var}")
  return var

# import REMINDERS as reminders
# datetime = reminders.toRegularDatetime(datetimeString)
def toRegularDatetime(datetimeString):
  print(f"is this a string?: It should be: {isString(datetimeString)}")
  var = readableDatetimeStringToDateTime(datetimeString)
  print(f"var - to reg: {var}")
  return var # "10/12/2022 at 2:00 pm"


#---------------------------------

def isString(var):
  res = isinstance(var, str)
  return res

# import REMINDERS as reminders
# reminders.readableDatetimeStringToDateTime(datetimeString="2/4/2022 at 12:10 pm")
# 2022-10-12 14:00:00 --> 10/12/2022 at 2:00 pm

def notReadableDatetimeToReadable(datetime): # 2022-10-12 14:00:00
  string = str(datetime)
  s = string.split(" ")
  date = s[0]
  d1 = date.split("-")
  y=d1[0]
  m=d1[1]
  d=d1[2]
  time = s[1]
  t = time.split(":")
  h=int(t[0])
  m1=t[1]
  ampm = "am"
  if h==12:
    ampm="pm"
  elif h>12:
    ampm="pm"
    h = h-12

  datetime = f"{m}/{d}/{y} at {h}:{m1} {ampm}" #"%m/%d/%Y at %I:%M %p"
  #print(datetime)
  return datetime




# import REMINDERS as reminders
# reminders.readableDatetimeStringToDateTime(datetimeString="2/4/2022 at 12:10 pm")
# 10/12/2022 at 2:00 pm --> 2022-10-12 14:00:00

def readableDatetimeStringToDateTime(datetimeString="2/4/2022 at 12:10 pm"):
  string = datetimeString # "2/4/2022 at 12:10 pm"
  str = string.split(" at ")
  date = str[0]
  d = date.split("/")
  #print("date-split:")
  #print(d)
  m=d[0]
  d=d[1]
  y=date.split("/")[2]
  time2 = str[1]
  t = time2.split(" ")
  h = t[0].split(":")[0]
  h = int(h)
  m1 = t[0].split(":")[1]
  ampm = t[1]
  if ampm=="pm":
    #print(f"pm exists ... hour starts at {h}")
    if(h!=12): #only add 12 if it's not 12 to start with
      h = h + 12
    #print(f"added 12 hours ... hour starts at {h}")
    pass
  #print("int(y), int(m), int(d), int(h), int(m1):")
  #print(int(y), int(m), int(d), int(h), int(m1))
  thisDatetime = createAdateTime(int(y), int(m), int(d), int(h), int(m1))
  #print(f"thisDatetime: {thisDatetime}")
  return thisDatetime




#---------------------------------




def addReminder():
  #["10/12/2022 at 1:00 pm"], ["Happy Birthday"], ["7 d", "6 d", "5 d", "4 d", "3 d", "2 d", "1 d", "4 h", "2 h", "1 h", "30 m", "15 m", "0 m"]
  #["2/4/2022 at 11:25 pm"], ["Quick Reminder"], ["2 h", "1 h", "30 m", "15 m", "0 m"]
  pass





# import REMINDERS as reminders
# result = reminders.compareDates2()

def compareDates2():
  import datetime, time
  t1 = datetime.datetime.now()#print(t1 > t2)  # False #print(t1 < t2)  # True
  print(f"t1: {t1}")
  time.sleep(0.1)
  t2 = datetime.datetime.now()
  print(f"t2: {t2}")
  print(t1 > t2)  # False
  print(t1 < t2)  # True




# import FUNCTIONS as fns
# result = fns.compareDates1()

def compareDates1():
  from datetime import datetime
  present = datetime.now()
  print (f"present: {present}")
  differentDay = datetime(2022,1,15,1,1,1)
  print (f"differentDay: {differentDay} - datetime(2022,1,15,1,1,1)")
  # COMPARE DATES HERE:
  result = differentDay < present
  print (f"result: {result}") #should return true
  return result





# y, m, d, h, m1, s = varsFromDatetime(datetime)
# y, m, d, h, m1, s = varsFromDatetimeString(datetimeString = "2009-10-05 18:00:00")

def varsFromDatetime(datetime):
  datetimeString = str(datetime) # 2009-10-05 18:00:00
  dt = datetimeString.split(" ")
  date = dt[0]
  d1 = date.split("-")
  y=d1[0]
  m=d1[1]
  d=d1[2]
  time = dt[1]
  tm = time.split(":")
  h=tm[0]
  m1=tm[1]
  s=0
  return y, m, d, h, m1, s

# y, m, d, h, m1, s = varsFromDatetime(datetime)
# y, m, d, h, m1, s = varsFromDatetimeString(datetimeString = "2009-10-05 18:00:00")
def varsFromDatetimeString(datetimeString = "2009-10-05 18:00:00"):
  datetimeString = str(datetimeString)
  dt = datetimeString.split(" ")
  date = dt[0]
  d1 = date.split("-")
  y=d1[0]
  m=d1[1]
  d=d1[2]
  time = dt[1]
  tm = time.split(":")
  h=tm[0]
  m1=tm[1]
  s=0
  return y, m, d, h, m1, s




# import REMINDERS as reminders
# dt = reminders.createAdateTime(y=2022,m=1,d=1,h=18,m1=00,s=00)

def createAdateTime(y=2022,m=1,d=1,h=18,m1=00,s=00):
  import datetime
  # 05/10/09 18:00
  d1 = datetime.datetime(y, m, d, h, m1, s)
  # easy access: d.year, d.month, d.day, d.hour, d.second
  # print (f"d1.isoformat(' '): {d1.isoformat(' ')}") # looks like a timestamp
  # 2009-10-05 18:00:00
  return d1


#------------------------------

# import REMINDERS as reminders
# date = reminders.createAdateTime(y=2022,m=2,d=3,h=18,m1=00,s=00)
# true = reminders.hasExpired(date)
# print(f"true: {true}")

def hasExpired(date):
  import datetime
  date2 = datetime.datetime.now()
  #true or false
  result = date < datetime.datetime.now()
  print(f"hasExpired(date): {date2} ... {result}")
  return result





def hasThisTimePassed(time="2022-01-11 16:00:00"):
  from datetime import datetime
  datetime.now()





def checkAheadOfTime():
  from datetime import datetime, timedelta
  #how to subtract or add time
  last_hour_date_time = datetime.now() - timedelta(minutes = 1) - timedelta(hours = 1) - timedelta(days = 1)
  print(last_hour_date_time.strftime('%Y-%m-%d %I:%M %p'))

  fullReminderSET = ["7 d", "6 d", "5 d", "4 d", "3 d", "2 d", "1 d", "4 h", "2 h", "1 h", "30 m", "15 m", "0 m"]
  # "This is your 7 day out reminder of...", ReminderMessage

  # Reminders:
  # 7 days before
  # 3 days before
  # 2 days before
  # 1 day before
  # 4 hours before
  # 2 hours before
  # 1 hour before
  # 30 minutes before
  # 15 minutes before
  # on the time




#not a working function
def daysBefore(date):
  # n day's before date:
  from datetime import date, timedelta

  current_date = date.today().isoformat()
  days_before = (date.today() - timedelta(days=30)).isoformat()

  print("\nCurrent Date: ", current_date)
  print("30 days before current date: ", days_before)
  #Output:
  #  "Current Date:  2019-11-02
  # 30 days before current date:  2019-10-03"


#n day's after date:
def daysAfter(date):
  from datetime import date, timedelta

  current_date = date.today().isoformat()
  days_after = (date.today()+timedelta(days=30)).isoformat()

  print("\nCurrent Date: ",current_date)
  print("30 days after current date : ",days_after)
  # Output:

  # Current Date:  2019-11-02
  # 30 days after current date :  2019-12-02


#-------------------------

# import REMINDERS as reminders
# dateTimeStr = reminders.getTimeAndDateAMPM()

def getTimeAndDateAMPM():
  from datetime import datetime
  now = datetime.now()
  # dd/mm/YY
  dateTimeString = now.strftime("%m/%d/%Y %I:%M %p") # 02/03/2022 03:08 PM
  #dt_string = now.strftime("%m/%d/%Y %H:%M %p") # 02/03/2022 15:08 PM
  print("dateTimeString: ", dateTimeString)
  return dateTimeString






# import SOUND as sound
# sound.beep()
