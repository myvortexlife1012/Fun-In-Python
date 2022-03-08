#ASTROLOGYfunctions.py # other functions


# import ASTROLOGYfunctions as aa
# aa.loopingThruTheLinkages2()


# aa.oneSETofData()

#-------------
# peopleCSV = aa.pdnaBankGetMyPeopleCSV()
# people = aa.pdnaBankGetMyPeopleCSV_BirthchartStuff()
#-------------

# aa.savingSettingPowerNumber(): #practice



# aa.loopingThruTheLinkages2()
# aa.loopingThruTheLinkages1()
# aa.oneSETofData()
# aa.getMidPointsFrom2Birthcharts()

# import ASTROLOGYfunctions as aa
# planets60 = aa.openSaveBirthchartCSVcache(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")
# planets360 = aa.degrees360convert(planets60) # <--
# print(f"planets360: {planets360}")

# degrees360 = aa.sign30to360(sign="Libra",sign30=18)
# sign,degrees30 = aa.sign360to30(deg360=198)
# aa.getPlanetName(string) #Sun: Libra (18) ... it pulls it from this string
# aa.getNumberInString(string) #Sun: Libra (18)
# midNum = aa.midpointFrom2_360s(n1, n2) #2 numbers that are 360's

# aa.midpointsFrom2Planets360(planets360_P1, planets360_P2)

#import OPENsomething as o
#import ASTROLOGYfunctions as aa
#planets30_P1 = o.openSaveBirthchartCSVcache(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")
#planets360_P1 = aa.degrees360convert(planets30_P1)
# print(f"planets360_P1: {planets360_P1}")
#planets60_P2 = o.openSaveBirthchartCSVcache(y=1984,m=4,d=18,h=12,m1=0,lat="19N25",long="99W7")
#planets360_P2 = aa.degrees360convert(planets60_P2) # <--
# print(f"planets360_P2: {planets360_P2}")
#mids = aa.midpointsFrom2Planets360(planets360_P1, planets360_P2) # <--
#print(f"mids: {mids}")

# aa.cacheALLlatLong() #ALL at once

# aa.cacheLatLong(city="San Jose, CA")

# aa.cacheAllCitiesLatLong()

# aa.cacheTheCity(city="Phoenix, AZ")

# import ASTROLOGYfunctions as aa
# cached = aa.findTheCityInCache(city = "Phoenix, AZ")
# if cached==False:
#   aa.cacheTheCity(city="Phoenix, AZ")

# lat, long = aa.findTheLatLongOfCityInCache(city = "Phoenix, AZ")
# decimalLat = aa.letterLatToDecimalLat(string="39N6")
# decimalLong = aa.letterLongToDecimalLong(string="94W34")
# letterLat = aa.decimalLatToLetterLat(d=39.10)
# letterLong = aa.decimalLongToLetterLong(d=-94.57)

# latDecimal, longDecimal = aa.mapQuestLatLong(city)
# latDecimal, longDecimal = aa.bingMapsLatLong(city)

# mainPlanets, otherAstroids = aa.parseBirthchartHTMLAllPlanetsCached(html)

# import ASTROLOGYfunctions as aa
# import OPENsomething as o
# html = o.openSaveBirthchartAsFile() #defaults to mine
# mainPlanets, otherAstroids = aa.parseBirthchartHTMLAllPlanetsCached(html)
# print(f"mainPlanets: {mainPlanets}")
# print(f"otherAstroids: {otherAstroids}")

# planets = aa.parseBirthchartHTML(html)

# import ASTROLOGYfunctions as aa
# html = aa.openSaveBirthchartAsFile()
# planets = aa.parseBirthchartHTML(html)
# print(f"planets: {planets}")

# aa.birthchartCSVsave(filenameCSV, CSVstring) #helper function
# aa.cachedAllMiniBirthchartCSVs() # just needed to do it once
# aa.cacheAllBirthchartHTMLs()
# planets = aa.openSaveBirthchartCSVcache(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")
# html = aa.openSaveBirthchartAsFile(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")
# import ASTROLOGYfunctions as aa
# csv = aa.loadCachedCSVbirthchart(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")

#-------------------------------


# import ASTROLOGYfunctions as aa
# orb, orbMax = aa.getOrb(me, aspect_string="Sun-Conjunct-Jupiter")
def getOrb(me, aspect_string="Sun-Conjunct-Jupiter"):
    a = aspect_string.split("-")
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    planets1 = me['planets']['360']
    planets = aa.p360planetsToDict(planets1)
    planetName1 = a[0]
    planetDegree1 = planets[planetName1 + "_g"].split("/")[0]
    planetName2 = a[2]
    planetDegree2 = planets[planetName2 + "_g"].split("/")[0]
    angleName = a[1]
    ao = m.aspects_organized
    angleDegree = ao[angleName]['degrees']
    AngleOrb = ao[angleName]['meaningful_orb']
    ap = anglePower = ao[angleName]['power'] # - or + nums
    po = m.planets_organized
    p1=planet1Power = po[planetName1]['power']
    p2=planet2Power = po[planetName2]['power']
    planets_power = planet1Power + planet2Power

    # orb - is the number - less than 10
    longer_diff, shorter_diff = aa.diffByAspectString(me, aspect_string)
    #longer_diff
    #shorter_diff
    #angleDegree
    matches = ""
    if shorter_diff >= angleDegree - AngleOrb and shorter_diff < angleDegree + AngleOrb:
        matches = "shorter_diff"
    elif longer_diff >= angleDegree - AngleOrb and longer_diff < angleDegree + AngleOrb:
        matches = "longer_diff"

    # --------------------------------------
    # GETTING THE ORB - Less than  10 degs
    #--------------------------------------
    # when u know there's an aspect

    orb = 0
    if matches == "longer_diff":
        orb = longer_diff - angleDegree
    elif matches == "shorter_diff":
        orb = shorter_diff - angleDegree
    else:
        orb = "-" # nothing

    #orb has to be positive
    if orb<0:
        orb = orb * -1
    #----------------------
    orb = f.round_down4(orb)
    var = orb, AngleOrb
    return var


#-----------------------------


# import ASTROLOGYfunctions as aa
# powerNum = aa.powerFor(me, aspect_string="Sun-Conjunct-Jupiter")
def powerFor(me, aspect_string="Sun-Conjunct-Jupiter"):
    a = aspect_string.split("-")
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    planets1 = me['planets']['360']
    planets = aa.p360planetsToDict(planets1)
    planetName1 = a[0]
    planetDegree1 = planets[planetName1 + "_g"].split("/")[0]
    planetName2 = a[2]
    planetDegree2 = planets[planetName2 + "_g"].split("/")[0]
    angleName = a[1]
    ao = m.aspects_organized
    angleNum = ao[angleName]['degrees']
    angle_orb_max = ao[angleName]['meaningful_orb']
    angle_orb_power = ao[angleName]['power'] # - or +
    po = m.planets_organized
    planet1_power = po[planetName1]['power']
    planet2_power = po[planetName2]['power']
    planets_power = planet1_power + planet2_power

    #orb - is the number - less than 10
    orb, orbMax = getOrb(me, aspect_string) # when u know there's an aspect

    #if the orb is less then 4.625
    #angle_orb * 2
    # pychologically relevant is an orb of 4.5 degrees
    if orb < 4.625:
        angle_orb_power = angle_orb_power * 2
    else:
        good = 4.625
        beg = orb-good
        end = orbMax - good
        r = ((end-beg)/end) + 1
        angle_orb_power = angle_orb_power * r
    #

    angle_orb_power2 = angle_orb_power
    if angle_orb_power<0:
        angle_orb_power2 = angle_orb_power * -1

    reducing_num_for_large_numbers = 10

    power_of_tightness_of_orb = f.round_down( (1-(orb/orbMax)) * 72 )

    power = (planets_power + angle_orb_power2) * power_of_tightness_of_orb / reducing_num_for_large_numbers

    #add back if it was negative
    if angle_orb_power < 0:
        power = power * -1


    power = f.round_down(power)

    return power



#-------------------------------

# import ASTROLOGYfunctions as aa
# small_num, large_num = aa.smallLargeNumSort(n1,n2)
def smallLargeNumsSort(n1, n2):
    import FUNCTIONS as f
    n1 = f.round_down4(float(n1))
    n2 = f.round_down4(float(n2))
    if n1 > n2:  # small first, then large
        return n2, n1
    elif n2 > n1:  # small first, then large
        return n1, n2
    else:  # just return them, if they're equal
        return n1, n2


# import ASTROLOGYfunctions as aa
# longer_diff, shorter_diff = aa.diffByAspectString(me, "Neptune-Quincunx-Chiron")
def diffByAspectString(me, aspectString="Neptune-Quincunx-Chiron"):
    a = aspectString.split("-")
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    planets1 = me['planets']['360']
    planets = aa.p360planetsToDict(planets1)
    planetName1 = a[0]
    planetDegree1 = planets[planetName1+"_g"].split("/")[0]
    planetName2 = a[2]
    planetDegree2 = planets[planetName2+"_g"].split("/")[0]
    angleName = a[1]
    ao = m.aspects_organized
    angleNum = ao[angleName]['degrees']
    orbNum = ao[angleName]['meaningful_orb']

    #print(f"planetDegree1: {planetDegree1}, planetDegree2: {planetDegree2}")
    n1 = planetDegree1
    n2 = planetDegree2
    small_num, large_num = aa.smallLargeNumsSort(n1, n2)
    # far diff - or longer diff
    # you take the large number - minus - the small number
    longer_diff = f.round_down4(large_num - small_num)
    #print(f"longer_diff is ... large_num - small_num = longer_diff ")
    #print(f"longer_diff is ... {large_num} - {small_num} = {longer_diff} ")
    # near diff - or - shorter diff
    # you take 360-the large number + plus + the small number
    shorter_diff = f.round_down4(360-large_num + small_num)
    #print(f"shorter_diff  is... (360 - large_num) + small_num = shorter_diff ")
    #print(f"shorter_diff  is... (360 - {large_num}) + {small_num} = {shorter_diff} ")
    # returns 2 numbers, the far-deg, and near-degrees
    return longer_diff, shorter_diff


#-------------------------------


# import ASTROLOGYfunctions as aa
# user = aa.me()
def me():
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa

    #look me up in the users folder
    filename = "mycosmicdna/db_users.txt"  # C:/Users/myvor/PycharmProjects/pythonProject/
    users = f.readFile(filename)  # array of lines
    #print(f"USERS ({len(users)}):")
    #print(users) # i'm first after the titles, [1]
    nameFields = users[0].split("', '") #loading from csv - so it's not exploded yet into pieces
    #print(f"nameFields ({len(nameFields)}):")
    # LATER: SOME SELECTION MECHANISM - TO CHOOSE ANOTHER USER
    # [1] is me
    user1 = users[1].split("', '")  #loading from csv - so it's not exploded yet into pieces
    #print(f"user1: ({len(user1)}):")
    user = {'info':{}, 'planets':{}}
    for c in range(len(nameFields)):
        key = nameFields[c].strip("\n").strip("'").strip('"')
        value = user1[c].strip("\n").strip("'").strip('"')
        user['info'].update({key: value})
    #adding full name in 'name', like pdnabank has
    name = user['info']['fname']+" "+user['info']['lname']
    name = name.replace("  ", " ") # there were 2 spaces
    user['info'].update({'name': name})
    # -- pull out the useful info --

    name = user['info']['fname'] + " " + user['info']['lname']
    datetime = user['info']['datetime']
    city = user['info']['city']
    timezone = user['info']['timezone']
    timeknown = user['info']['timeknown'] # time_given, time_not_given
    email = user['info']['email']

    # -- get this ready for the right birthchart to be loaded in --
    # break down the time and date
    dt = datetime.split(" ") # '1981-10-12 03:06:00'
    date = dt[0]
    d1 = date.split("-")
    y = int(d1[0])
    m = int(d1[1])
    d = int(d1[2])
    time = dt[1]
    t = time.split(":")
    h = int(t[0])
    m1 = int(t[1])

    #initialize these 2
    planets360 = {}
    planets30 = {}

    # -- load in the birthchart - from the user info above --
    #print(1)
    # aa.cache1Birthchart() adds retrograde


    lat, long = aa.cacheTheCity(city) # get this info from the city
    foldernameCSV = "birthchart-cache/csv/"
    lat, long = aa.cacheTheCity(city)
    # 1984-4-18--12-0--19N25-99W7.csv ... get the format
    filenameCSV = f"{y}-{m}-{d}--{h}-{m1}--{lat}-{long}.csv"  # db_pdnabank2.txt[4] = "timezone" "-5" ...
    filenameCSV = foldernameCSV + filenameCSV
    status = f.fileExists(filenameCSV)

    if status==True:
        planets360 = aa.load1Birthchart(filenameCSV)  # format: birthchart-cache/csv/1981-10-12--9-6--39N6-94W34.csv
        #print(2)
    else:
        #print(3)
        planets360 = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, timezone=timezone, city=city)
    #print(f"planets360: {planets360}") #should have Rx on some
    planets30 = aa.degrees30convert(planets360)
    #print(f"planets30: {planets30}")

    # -- add the user's planets to the user dict --

    user['planets'].update({'360': planets360})
    user['planets'].update({'30': planets30})

    # -- print it so you can see it all set up --

    #print("user: me")
    #print(user)
    #f.print2(user)
    #print("user: me") # ...time_given # 'timeknown': 'MO', - something is off
    #print(user)

    # return the user - it seems logical to return that
    return user


#-------------------------------


# EASY WAY TO SELECT PEOPLE
# import ASTROLOGYfunctions as aa

def person(): #you can request people 2 ways, USE ONLY 1 of them
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Test")
    #print(f"personInfo: ({len(personInfo)}):")
    #f.print2(personInfo)
    #print(f"personInfo: ({len(personInfo)}):")
    # -- get this ready for the right birthchart to be loaded in --
    # break down the time and date

    #--------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------

    #print(f"personInfo: ({len(personInfo)}):")
    #f.print2(personInfo)
    #print(f"personInfo: ({len(personInfo)}):")
    #print("")
    #print(f"planets: ({len(planets)}):")
    #f.print2(planets)
    #print(f"planets: ({len(planets)}):")

    person = {'info': {}, 'planets': {}}

    person['planets']["360"] = planets[0]
    person['planets']["30"] = planets[1]
    person['info'] = personInfo

    #print(f"person: ({len(person)}):")
    #f.print2(person)
    #print(f"person: ({len(person)}):")

    return person

#-------------------------------
"""
Miriam
Crystal
Michelle
Carly
Kristi
Rosemary
Maryann
"""
# import ASTROLOGYfunctions as aa
# aa.woman1()
def woman1():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Miriam")
    #--------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person

def woman2():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Crystal")
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person



def woman3():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Michelle")
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person

def woman4():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Carly")
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person


def woman5():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Kristi")
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person

def woman6():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Rosemary")
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person



def woman7():
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Maryann")
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------
    planets360 = planets[0]
    planets30 = planets[1]
    person = {'info': personInfo, 'planets': {'30':planets30, '360':planets360} }
    return person



def person3(): #you can request people 2 ways, USE ONLY 1 of them
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Josh")
    #print(f"personInfo: ({len(personInfo)}):")
    #f.print2(personInfo)
    #print(f"personInfo: ({len(personInfo)}):")
    #print("exiting")
    #exit()
    # -- get this ready for the right birthchart to be loaded in --
    # break down the time and date
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------

    #print(f"personInfo: ({len(personInfo)}):")
    #f.print2(personInfo)
    #print(f"personInfo: ({len(personInfo)}):")
    #print("")
    #print(f"planets: ({len(planets)}):")
    #f.print2(planets)
    #print(f"planets: ({len(planets)}):")

    person = {'info': {}, 'planets': {}}

    person['planets']["360"] = planets[0]
    person['planets']["30"] = planets[1]
    person['info'] = personInfo

    #print(f"person: ({len(person)}):")
    #f.print2(person)
    #print(f"person: ({len(person)}):")

    return person

#-------------------------------

def person2(): #you can request people 2 ways, USE ONLY 1 of them
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    personInfo = aa.pdnaBank1person("Miriam")
    #print(f"personInfo: ({len(personInfo)}):")
    #f.print2(personInfo)
    #print(f"personInfo: ({len(personInfo)}):")
    #print("exiting")
    #exit()
    # -- get this ready for the right birthchart to be loaded in --
    # break down the time and date
    # --------------------------------------------------
    # ** PERSON - PLANETS ** # ** PERSON - PLANETS **
    planets = aa.personPlanets(personInfo)
    # --------------------------------------------------

    #print(f"personInfo: ({len(personInfo)}):")
    #f.print2(personInfo)
    #print(f"personInfo: ({len(personInfo)}):")
    #print("")
    #print(f"planets: ({len(planets)}):")
    #f.print2(planets)
    #print(f"planets: ({len(planets)}):")

    person = {'info': {}, 'planets': {}}

    person['planets']["360"] = planets[0]
    person['planets']["30"] = planets[1]
    person['info'] = personInfo

    #print(f"person: ({len(person)}):")
    #f.print2(person)
    #print(f"person: ({len(person)}):")

    return person

#-------------------------------
# import ASTROLOGYfunctions as aa
# degSection = aa.degreesRoundedDownToA5(n)
def degreesRoundedDownToA5(n):
    n = float(n)
    base = 5
    nearest_multiple_of_5 = base * round(n / base)
    return nearest_multiple_of_5


# import ASTROLOGYfunctions as aa
# chartToday = aa.today()
def today():
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    from datetime import datetime

    today = {'info': {}, 'planets': {}}

    # -- pull out the useful info --
    name = "Today - A Date's Birthchart"
    datetime = datetime.now().strftime("%Y/%m/%d 12:00:00") # 2022/02/24 12:00:00
    #print(f"datetime: {datetime}")
    #print("exiting")
    #exit()
    city = "Phoenix, AZ"
    timezone = -6
    timeknown = "time_not_given" # time_given, time_not_given


    # -- get this ready for the right birthchart to be loaded in --
    # break down the time and date
    dt = datetime.split(" ") # '1981-10-12 03:06:00' #
    date = dt[0]
    d1 = date.split("/")
    y = int(d1[0])
    m = int(d1[1])
    d = int(d1[2])
    time = dt[1]
    t = time.split(":")
    h = int(t[0])
    m1 = int(t[1])

    today['info'] = {'datetimeYMD':datetime, 'dateYMD':date, 'time':time, 'city':city, 'timezone': timezone, 'gender':"None"}

    # -- load in the birthchart - from the user info above --

    # aa.cache1Birthchart() adds retrograde
    planets360 = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, timezone=timezone, city=city)
    # print(f"planets360: {planets360}") #should have Rx on some
    planets30 = aa.degrees30convert(planets360)
    # print(f"planets30: {planets30}")

    # -- add the user's planets to the user dict --
    #today
    today['planets'].update({'360': planets360})
    today['planets'].update({'30': planets30})

    # -- print it so you can see it all set up --

    #print("user: me")
    #print(user)
    #f.print2(user)
    #print("user: me") # ...time_given # 'timeknown': 'MO', - something is off
    #print(user)

    # return the user - it seems logical to return that
    return today


#-------------------------------


def compatibilityTest_7women():
    import ASTROLOGYfunctions as aa
    import FUNCTIONS as f
    me = aa.me()

    woman1 = aa.woman1()
    woman2 = aa.woman2()
    woman3 = aa.woman3()
    woman4 = aa.woman4()
    woman5 = aa.woman5()
    woman6 = aa.woman6()
    woman7 = aa.woman7()

    ln = 3  # lines of space
    f.someSpace(ln)
    print(f"-------{woman1['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman1)
    f.someSpace(ln)
    print(f"-------{woman2['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman2)
    f.someSpace(ln)
    print(f"-------{woman3['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman3)
    f.someSpace(ln)
    print(f"-------{woman4['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman4)
    f.someSpace(ln)
    print(f"-------{woman5['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman5)
    f.someSpace(ln)
    print(f"-------{woman6['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman6)
    f.someSpace(ln)
    print(f"-------{woman7['info']['name']}--------\n")
    aa.setOf6compatibility(me, woman7)
    f.someSpace(ln)


#-------------------------------


# import ASTROLOGYfunctions as aa
# me = aa.me()
# person2 = aa.person2()
# aa.setOf6compatibility(me, person2)
def setOf6compatibility(me, person2):
    import ASTROLOGYfunctions as aa
    print("Self - ME - Magi Numbers - Calibration:")
    powers4 = aa.csvSelfMagiAspects264_3(me, type="self", showLines=False)  # set up with passing vars
    print(f"powers4: {powers4}")

    print("Self - THEM - Magi Numbers - Calibration:")
    powers4 = aa.csvSelfMagiAspects264_3(person2, type="self", showLines=False)  # set up with passing vars
    print(f"powers4: {powers4}")

    print("\n------------------------\n")

    # THE INITIAL COMPATIBILITY - 1ST MEETING
    powers4 = aa.csvSYNASTRYMagiAspects264_2(me, person2)
    print("Synastry CAC - Calibration:")
    print(f"powers4: {powers4}")

    # print("Self - Calibration:") #there seems to be zero love in 3 people's - so it could be an error
    # print("Miriam - check it - Calibration:")
    # powers4 = aa.csvSelfMagiAspects264_3(person3) # set up with passing vars
    # print(f"powers4: {powers4}")

    # potiential
    me_planets = me['planets']['360']
    person2_planets = person2['planets']['360']
    potientialRelationshipMids = aa.midpointsFrom2Planets360(me_planets, person2_planets)  # <--
    person_potiential = {'info': {'name': "Potential Relationship Midpoints", 'gender': "None", 'city': "None"},
                         'planets': {'360': potientialRelationshipMids}}

    # THE POTENTIAL RELATIONSHIP - Midpoints of both charts
    # print(f"potientialRelationshipMids: {potientialRelationshipMids}")
    print("Potiential Relationship (Self) - Calibration:")
    powers4 = aa.csvSelfMagiAspects264_3(person_potiential, type="potiential", showLines=False)  # set up with passing vars
    print(f"powers4: {powers4}")
    # have a seperate setting for the multiplier when I'm using SELF for potiential--a 2nd number adjustment

    # Now we take Person 1 - to the Potiential/Midpoints - a CAC or Synastry ... how I feel about it
    powers4 = aa.csvSYNASTRYMagiAspects264_2(me, person_potiential, "how I feel about it")
    print("ME - Synastry CAC (Me-Potiential) - Calibration: ... How I Feel About The Relationship: ME:")
    print(f"powers4: {powers4}")

    # Now we take Person 2 - to the Potiential/Midpoints - a CAC or Synastry ... how they feel about it
    powers4 = aa.csvSYNASTRYMagiAspects264_2(person2, person_potiential, "how they feel about it")
    print(
        "PERSON 2 - Synastry CAC (Them-Potiential) - Calibration: ... How They Feel About The Relationship: PERSON 2:")
    print(f"powers4: {powers4}")

    # for person 1 - mids from - the mids - to my chart
    howItAffectsMe_mids = aa.midpointsFrom2Planets360(me_planets, person2_planets)  # <--
    person_howItAffectsMe_mids = {
        'info': {'name': "How I Feel About The Relationship Midpoints", 'gender': "None", 'city': "None"},
        'planets': {'360': howItAffectsMe_mids}}

    # for person 2 - mids from - the mids - to their chart
    howItAffectsThem_mids = aa.midpointsFrom2Planets360(me_planets, person2_planets)  # <--
    person_howItAffectsThem_mids = {
        'info': {'name': "How They Feel About The Relationship Midpoints", 'gender': "None", 'city': "None"},
        'planets': {'360': howItAffectsThem_mids}}

    # Now we take Person 1 - to the Affects Them/Midpoints - a CAC or Synastry ... how the relationship affects you
    powers4 = aa.csvSYNASTRYMagiAspects264_2(me, person_howItAffectsMe_mids, "how it affects me")
    print("ME - Synastry CAC (Me-Affects) - Calibration: ... How The Relationship Affects Me: ME:")
    print(f"powers4: {powers4}")

    # Now we take Person 2 - to the Affects Them/Midpoints - a CAC or Synastry ... how the relationship affects them
    powers4 = aa.csvSYNASTRYMagiAspects264_2(person2, person_howItAffectsThem_mids, "how it affects them")
    print("PERSON 2 - Synastry CAC (Them-Affects) - Calibration: ... How The Relationship Affects Them: PERSON 2:")
    print(f"powers4: {powers4}")


#-------------------------------


# import ASTROLOGYfunctions as aa
# aa.theFinanceParallels("g","g") #compare geo to geo - 1st planet - 2nd planet / try 'h'
def theFinanceParallels(t1="g",t2="g"):
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    #me = aa.me()
    #planets = me['planets']['360']
    today = aa.today()
    planets = today['planets']['360']
    #print(f"planets: {len(planets)}")
    #f.print2(planets)

    planetsDict = aa.p360planetsToDict(planets)
    #print(f"planetsDict: {len(planetsDict)}")
    #f.print2(planetsDict)

    magiAspectsFinancial = m.magiAspectsFinancial
    #print(f"magiAspectsFinancial: {len(magiAspectsFinancial)}")
    #f.print2(magiAspectsFinancial)

    for i in range(len(magiAspectsFinancial)):
        catWords = magiAspectsFinancial[i]
        cat = f.collapseArray(catWords['cat'], ", ")
        words3 = catWords['word3']
        w = words3.split("-")
        planet1 = w[0]
        angleOrParallel = w[1]
        planet2 = w[2]

        #print(f"{i}) cat: {cat} / planet1: {planet1} / planet2: {planet2} / angleOrParallel: {angleOrParallel}")
        planet1_str = planet1+"_"+t1 #"_g"
        degreesRxDecDisSpeed1 = planetsDict[planet1_str] # this is all 5 values # deg360/Rx/declination/distance/speed
        d1 = degreesRxDecDisSpeed1.split("/")
        deg1 = d1[0]
        try:
            Rx1 = d1[1]
            decl1 = d1[2]
            dist1 = d1[3]
            speed1 = d1[4]
        except:
            Rx1 = "-"
            decl1 = "-"
            dist1 = "-"
            speed1 = "-"

        planet2_str = planet2 +"_"+t2 #"_g"
        degreesRxDecDisSpeed2 = planetsDict[planet2_str]
        d2 = degreesRxDecDisSpeed2.split("/")
        deg2 = d2[0]
        try:
            Rx2 = d2[1]
            decl2 = d2[2]
            dist2 = d2[3]
            speed2 = d2[4]
        except:
            Rx2 = "-"
            decl2 = "-"
            dist2 = "-"
            speed2 = "-"

        a = angleOrParallel
        if a=="Conjunct" or a=="Trine" or a=="Quincunx":
            angles = m.aspects_organized
            angle = angles[a]
            angleDegree = angle['degrees']
            orb = angle['meaningful_orb']
            dd=diffDegrees = f.round_down4(angleDifference2_360s(deg1, deg2))
            #if dd is within the orb
            if dd>angleDegree-orb and dd<=angleDegree+orb: #doesn't handle conjunctions - it would have to be
                print(f"MATCH - Angle:")
                print(f"{i}) cat: {cat} / words3: {words3} / planet1: {planet1} / planet2: {planet2} / angle: {angleOrParallel} / deg1: {deg1} / deg2: {deg2} / diffDegrees: {dd}")

        if angleOrParallel=="Parallel" or angleOrParallel=="Contraparallel":
            #print(f"angleOrParallel: {angleOrParallel}")
            #test to see if it's true - with decl1, and decl2 (declinations)
            #are they on the same side, at the same degree? #parallel
            #or are they on the opposite sides, at the same degree? #contraparallel
            decl_before = f.round_down4(abs(float(decl1)) - 1.2) # orb is 1.2 degrees
            decl_after = f.round_down2(abs(float(decl1)) + 1.2)
            #are both numbers negative (parallel), both positive (parallel), or opposite (contraparllel)

            #------------------------------------------------------------------------------
            # handle checking if numbers are same or diff signs, and confirming the angle
            # ------------------------------------------------------------------------------
            r=signsReversed = aa.areSignsReversed(decl1,decl2)
            if float(decl2) > decl_before and float(decl2) < decl_after:
                if r==True:
                    if angleOrParallel=="Contraparallel":
                        print (f"MATCH - {angleOrParallel} - {words3} ... decl1: {decl1}, decl_before {decl_before}, (decl2: {decl2}), decl_after: {decl_after}")
                        print(f"{i}) cat: {cat} / planet1: {planet1} / planet2: {planet2} / angleOrParallel: {angleOrParallel}")
                elif r==False:
                    if angleOrParallel=="Parallel":
                        print (f"MATCH - {angleOrParallel} - {words3} ... decl1: {decl1}, decl_before {decl_before}, (decl2: {decl2}), decl_after: {decl_after}")
                        print(f"{i}) cat: {cat} / planet1: {planet1} / planet2: {planet2} / angleOrParallel: {angleOrParallel}")

#-------------------------------


# import ASTROLOGYfunctions as aa
# aa.selfMagiAspects264_2(me)
def selfMagiAspects264_2(me): #in order
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    #print(f"me ({len(me)}):")
    #f.print2(me)
    planets360 = me['planets']['360'] #'Sun: 198', # need to parse as I go
    planets = aa.p360planetsToDict(planets360)
    #print(f"planets ({len(planets)}):")
    #f.print2(planets)
    #exit()
    aspects = m.AspectsDictSelf
    print(f"\naspects: ({len(aspects)})")
    for i in range(len(aspects)):
        aspectInOrder = aspects[i]
        #
        #print(f"\nAspect {i} of 264) aspectInOrder: {aspectInOrder}")
        #
        #look for a linkage - before you - see what category it goes in
        word3 = aspectInOrder['word3']
        cat = aspectInOrder['cat'] #in a list, Luck, Love, Sex, Drama, if it |b |f|m
        p = word3.split("-")
        pl1 = planetName1 = p[0]
        deg1 = planets[pl1]
        angle = p[1]
        pl2 = planetName2 = p[2]
        deg2 = planets[pl2]
        #see if it's a linkage
        # see if it's a linkage
        linkageStatus = aa.testLinkage(planetName1,deg1,angle,planetName2,deg2)
        if linkageStatus>0:
            print(f"\n MATCH - Aspect {i} of 264) aspectInOrder: {aspectInOrder}")
            print(f"linkageStatus: {linkageStatus}")
        else:
            print(f"\n NO MATCH - Aspect {i} of 264) aspectInOrder: {aspectInOrder}")


# import ASTROLOGYfunctions as aa
# aa.selfMagiAspects264_3()
def selfMagiAspects264_3(): #in order
    import ASTROLOGYmagi as m
    aspects = m.AspectsDictSelf
    print(f"aspects: ({len(aspects)})")
    for i in range(len(aspects)):
        a = aspects[i]
        word3 = a['word3']
        cat = a['cat']
        print(f"{i}, {word3}, {cat}")



# import ASTROLOGYfunctions as aa
# aa.csv_TODAY_MagiAspects264()
def csv_TODAY_MagiAspects264():
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    aspects = m.AspectsDictSelf
    #print(f"aspects: ({len(aspects)})")
    #me = aa.me()
    today = aa.today()
    gender = today['info']['gender']
    myPlanets = today['planets']['360']
    planets = aa.p360planetsToDict(myPlanets)
    totals4powers = {'Luck': 0, 'Love': 0, 'Sex': 0, 'Drama': 0, }  # totals4powers['Luck']
    # print titles of columns
    print("'num', 'word3', 'cat', 'match', 'planet1', 'angle', 'planet2', 'degrees1', 'degrees2', 'diffDegrees', 'angleDegree', 'diffDiffAndAngle', 'angleOrb', 'angleOrbPercentUsed', 'powerPoints', '-IF A Match-', 'anglePower', 'planetOrb1', 'planetPower1', 'planetOrb2', 'planetPower2', 'Rx1', 'Rx2', 'bidirectional', 'gender1', 'gender2', 'powerLuck', 'powerLove', 'powerSex', 'powerDrama'")

    for i in range(len(aspects)):
        a = aspects[i]
        if len(aspects[i]) > 0:  # if I still keep consolidating copies - this fixes if it's empty
            word3 = a['word3']
            cat = "/".join(a['cat'])  # so all the categories will be in one field, for csv
            match = ''
            p = word3.split("-")
            planet1 = p[0]
            degrees1 = planets[planet1]
            # planet 1 - Rx
            if "Rx" in degrees1:
                Rx1 = "Rx"
                degrees1 = degrees1.strip(" Rx")
            else:
                Rx1 = ""
            angle = p[1]
            planet2 = p[2]
            degrees2 = planets[planet2]
            # planet 2 - Rx
            if "Rx" in degrees2:
                Rx2 = "Rx"
                degrees2 = degrees2.strip(" Rx")
            else:
                Rx2 = ""

            if Rx1 != Rx2:
                bidirectional = "bidirectional"
            else:
                bidirectional = ""

            aso = m.aspects_organized  # degrees, meaningful_orb, power
            angleDegree = aso[angle]['degrees']
            d1 = degrees1
            d2 = degrees2

            diffDegrees = 0
            diffDegrees = aa.diffDegrees1(d1, d2, aso[angle]['degrees'])  # finds the larger, minus the smaller
            diffDegrees2 = aa.diffDegrees2(d1, d2, aso[angle]['degrees'])  # finds the diffDegCloser to the angle #near diff, and far diff

            plo = m.planets_organized  # planet_orb, power
            planetOrb1 = plo[planet1]['planet_orb']
            planetPower1 = plo[planet1]['power']
            planetOrb2 = plo[planet2]['planet_orb']
            planetPower2 = plo[planet2]['power']
            #aso = m.aspects_organized  # degrees, meaningful_orb, power
            #angleDegree = aso[angle]['degrees']
            angleOrb = aso[angle]['meaningful_orb']
            anglePower = aso[angle]['power']

            angleOrbPercentUsed = angleOrb  # diffDegrees will always be less - or more
            # if diffDegreesPlanets-angleAspectDegree==positive number ... that/angleOrb
            num = 1
            if diffDegrees > angleDegree:
                num = diffDegrees - angleDegree  # less than angleOrb now
            if diffDegrees <= angleDegree:
                num = angleDegree - diffDegrees  # less than angleOrb now
            # make even barely connected planets - get some - leave it at 1
            # if num < 1:
            # num= num + .1
            angleOrbPercentUsed = f.round_down2(num / angleOrb)

            gender1 = gender  # "Male"
            gender2 = gender1

            match = "NO"
            if diffDegrees >= angleDegree - angleOrb and diffDegrees <= angleDegree + angleOrb:
                match = "YES"

            powerPoints = 0
            if match == "YES":
                # closer they are to a perfect orb of 0 - they get 100% points
                powerPoints = (anglePower * angleOrbPercentUsed) * (planetPower1 + planetPower2)
                # powerPoints - reduce to orbClosePercent
                if powerPoints < 0:  # if negative power
                    if bidirectional == "bidirectional":
                        powerPoints = powerPoints * -1.6
                elif powerPoints > 0:  # if positive power
                    powerPoints = powerPoints * 1.6
                # angleOrb

                # diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle = 0
                if diffDegrees >= angleDegree:
                    diffDiffAndAngle = diffDegrees - angleDegree
                elif angleDegree > diffDegrees:
                    diffDiffAndAngle = angleDegree - diffDegrees

                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck = 0
                powerLove = 0
                powerSex = 0
                powerDrama = 0

                # keep it positive - when putting points into the category
                powerPoints2 = powerPoints
                if powerPoints < 0:
                    powerPoints2 = powerPoints * -1

                # parse the cat var
                # go thru all 4, if it has those words in the cat
                if "Luck" in cat:
                    powerLuck = powerPoints2  # powerLuck, powerLove, powerSex, powerDrama
                    totals4powers['Luck'] += f.round_down2(powerLuck)
                if "Love|f" == cat:
                    if gender1 == "Female":
                        powerLove = powerPoints2
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love|m" == cat:
                    if gender1 == "Male":
                        powerLove = powerPoints2
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love" in cat:
                    powerLove = powerPoints2
                    totals4powers['Love'] += f.round_down2(powerLove)
                if "Sex|m" == cat:
                    # only option
                    if gender1 == "Male":
                        powerSex = powerPoints2
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    else:
                        powerPoints = 0
                elif "Sex" in cat:
                    powerSex = powerPoints2
                    totals4powers['Sex'] += f.round_down2(powerSex)
                if "Drama" in cat:
                    powerDrama = powerPoints2
                    totals4powers['Drama'] += f.round_down2(powerDrama)
                # that's the simple version ... if there is

            if match == "YES":  # if abs(powerPoints)>0 and match=="YES":
                print(f"{i}, {word3}, {cat}, {match}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees2}, {diffDegrees}, {angleDegree}, {diffDiffAndAngle}, {angleOrb}, {angleOrbPercentUsed}, {powerPoints}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}, {powerLuck}, {powerLove}, {powerSex}, {powerDrama}")  # pl1 Rx	pl2 Rx
            #if match == "NO":  # if abs(powerPoints)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, {match}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees2}, {diffDegrees}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}, -, -, -, -")  # pl1 Rx	pl2 Rx

    # post processing
    # this is setting up the multipliers - and turn it into percents
    t = totals4powers
    luck = t['Luck']
    luck = f.round_down2(luck / 700 * 100)
    love = t['Love']
    love = f.round_down2(love / 400 * 100)
    sex = t['Sex']
    sex = f.round_down2(sex / 400 * 100)  # 100 to make it a percent
    drama = t['Drama']
    drama = f.round_down2(drama / 600 * 100)  # 100 to make it a percent
    print("How Good is Today? MagiAngles for Today are:")
    print("Luck %, Love %, Sex %, Drama %")  # titles
    print(f"{luck}%, {love}%, {sex}%, {drama}%, ")  # values





# import ASTROLOGYfunctions as aa
# powers4 = aa.csvSYNASTRYMagiAspects264_2(me, person)
def csvSYNASTRYMagiAspects264_2(me, person, type="how I feel about it"): #in order
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    aspects = m.AspectsDictSynastry
    #print(f"aspects: ({len(aspects)})")
    #-------------------------------
    #me = aa.me() #person 1
    #person = aa.person2() #person 2 gets miriam loaded
    #-------------------------------
    #today = aa.today()
    gender1 = me['info']['gender']
    gender2 = person['info']['gender']
    myPlanets = me['planets']['360']
    herPlanets = person['planets']['360']
    planets_me = aa.p360planetsToDict(myPlanets)
    planets_her = aa.p360planetsToDict(herPlanets)
    totals4powers = {'Luck':0,'Love':0,'Sex':0,'Drama':0,} # totals4powers['Luck']
    #print titles of columns
    #print("'num', 'word3', 'cat', 'Match Num 1 or 2', 'match', 'planet1', 'angle', 'planet2', 'degrees1', 'degrees4', 'diffDegrees1', 'angleDegree', 'diffDiffAndAngle1', 'angleOrb', 'angleOrbPercentUsed1', 'powerPoints1', '-IF A Match-', 'anglePower', 'planetOrb1', 'planetPower1', 'planetOrb2', 'planetPower2', 'Rx1', 'Rx4', 'bidirectional1', 'gender1', 'gender2', 'powerLuck1', 'powerLove1', 'powerSex1', 'powerDrama1'")

    for i in range(len(aspects)):
        a = aspects[i]
        if len(aspects[i])>0: #if I still keep consolidating copies - this fixes if it's empty
            word3 = a['word3']
            cat = "/".join(a['cat']) #so all the categories will be in one field, for csv
            match1 = ''
            match2 = ''
            p = word3.split("-")
            planet1 = p[0]
            degrees1 = planets_me[planet1]
            degrees3 = planets_her[planet1]  # 1-4 - Per1 to Per2 / 3-2 - Per2 to Per1
            #planet 1 - Rx - person 1
            if "Rx" in degrees1:
                Rx1 = "Rx"
                degrees1 = degrees1.strip(" Rx")
            else:
                Rx1 = ""
            #planet 1 - Rx - person 2
            if "Rx" in degrees3:
                Rx3 = "Rx"
                degrees3 = degrees3.strip(" Rx")
            else:
                Rx3 = ""
            angle = p[1]
            planet2 = p[2]
            degrees2 = planets_me[planet2]
            degrees4 = planets_her[planet2]  # 1-4 - Per1 to Per2 / 3-2 - Per2 to Per1
            #planet 2 - Rx
            if "Rx" in degrees2:
                Rx2 = "Rx"
                degrees2 = degrees2.strip(" Rx")
            else:
                Rx2 = ""
            #planet 2 - Rx - person 2
            if "Rx" in degrees4:
                Rx4 = "Rx"
                degrees4 = degrees4.strip(" Rx")
            else:
                Rx4 = ""

            # bidirectional1
            if Rx1!=Rx4: # 1-4 - P1 to P2  /  3-2 - P2 to P1
                bidirectional1 = "bidirectional"
            else:
                bidirectional1 = ""

            # bidirectional2
            if Rx3!=Rx2: # 1-4 - P1 to P2  /  3-2 - P2 to P1
                bidirectional2 = "bidirectional"
            else:
                bidirectional2 = ""


            diffDegrees1 = 0 # 1-4 - P1 to P2  /  3-2 - P2 to P1
            if float(degrees1)>float(degrees4):
                diffDegrees1 = float(degrees1)-float(degrees4)
            else:
                diffDegrees1 = float(degrees4)-float(degrees1)

            diffDegrees2 = 0 # 1-4 - P1 to P2  /  3-2 - P2 to P1
            if float(degrees3) > float(degrees2):
                diffDegrees2 = float(degrees3) - float(degrees2)
            else:
                diffDegrees2 = float(degrees2) - float(degrees3)

            plo = m.planets_organized #planet_orb, power
            planetOrb1 = plo[planet1]['planet_orb']
            planetPower1 = plo[planet1]['power']
            planetOrb2 = plo[planet2]['planet_orb']
            planetPower2 = plo[planet2]['power']
            aso = m.aspects_organized # degrees, meaningful_orb, power
            angleDegree = aso[angle]['degrees']
            angleOrb = aso[angle]['meaningful_orb']
            anglePower = aso[angle]['power']

            angleOrbPercentUsed = angleOrb #diffDegrees will always be less - or more
            #if diffDegreesPlanets-angleAspectDegree==positive number ... that/angleOrb
            num1 = 0
            if diffDegrees1>angleDegree:
                num1 = diffDegrees1 - angleDegree #less than angleOrb now
            if diffDegrees1<=angleDegree:
                num1 = angleDegree - diffDegrees1 #less than angleOrb now
            #make even barely connected planets - get some - leave it at 1
            #if num1 < 1:
                #num1= num1 + .1
            angleOrbPercentUsed1 = f.round_down2(num1 / angleOrb)

            num2 = 0
            if diffDegrees2 > angleDegree:
                num2 = diffDegrees2 - angleDegree  # less than angleOrb now
            if diffDegrees2 <= angleDegree:
                num2 = angleDegree - diffDegrees2  # less than angleOrb now
            # make even barely connected planets - get some - leave it at 1
            # if num2 < 1:
                # num1= num2 + .1
            angleOrbPercentUsed2 = f.round_down2(num2 / angleOrb)

            gender1 = gender1 # "Male"
            gender2 = gender2 # "Female"

            match1 = "NO"
            if diffDegrees1>=angleDegree-angleOrb and diffDegrees1<=angleDegree+angleOrb:
                match1 = "YES"

            match2 = "NO"
            if diffDegrees2>=angleDegree-angleOrb and diffDegrees2<=angleDegree+angleOrb:
                match2 = "YES"


            # ------------------------------------------
            powerPoints1=0
            powerPoints_P1 = 0
            if match1 == "YES":
                # closer they are to a perfect orb of 0 - they get 100% points
                if angleOrbPercentUsed1==1:
                    addAbit = .1
                else:
                    addAbit = 0
                powerPoints1 = (anglePower * (1-angleOrbPercentUsed1+addAbit) ) * (planetPower1 + planetPower2)
                #powerPoints - reduce to orbClosePercent
                if powerPoints1<0: #if negative power
                    if bidirectional1=="bidirectional": # bidirectional1, bidirectional2
                        powerPoints1 = powerPoints1 * -1.6
                elif powerPoints1>0: #if positive power
                    powerPoints1 = powerPoints1 * 1.6
                # angleOrb

                #diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle1=0
                if diffDegrees1>=angleDegree:
                    diffDiffAndAngle1 = diffDegrees1 - angleDegree
                elif angleDegree>diffDegrees1:
                    diffDiffAndAngle1 = angleDegree - diffDegrees1

                # ------------------------------------------
                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck1 = 0
                powerLove1 = 0
                powerSex1 = 0
                powerDrama1 = 0

                #keep it positive - when putting points into the category
                powerPoints1a = powerPoints1
                if powerPoints1<0:
                    powerPoints1a = powerPoints1 * -1

                #parse the cat var
                #go thru all 4, if it has those words in the cat
                # synastry doesn't have the | anymore
                if "Luck" in cat:
                    powerLuck1 = powerPoints1a # powerLuck1, powerLove1, powerSex1, powerDrama1
                    totals4powers['Luck'] += f.round_down2(powerLuck1)
                if "Love" in cat:
                    powerLove1 = powerPoints1a
                    totals4powers['Love'] += f.round_down2(powerLove1)
                if "Sex" in cat:
                    powerSex1 = powerPoints1a
                    totals4powers['Sex'] += f.round_down2(powerSex1)
                if "Drama" in cat:
                    powerDrama1 = powerPoints1a
                    totals4powers['Drama'] += f.round_down2(powerDrama1)
                # that's the simple version ... if there is
                #
                #------------------------------------------

            # ------------------------------------------
            powerPoints2=0
            powerPoints_P2 = 0
            if match2 == "YES":
                # closer they are to a perfect orb of 0 - they get 100% points
                if angleOrbPercentUsed2 == 1:
                    addAbit = .1
                else:
                    addAbit = 0
                powerPoints2 = (anglePower * (1-angleOrbPercentUsed2+addAbit) ) * (planetPower1 + planetPower2)
                # powerPoints_P2 - reduce to orbClosePercent
                if powerPoints2 < 0:  # if negative power
                    if bidirectional2 == "bidirectional":  # bidirectional1, bidirectional2
                        powerPoints2 = powerPoints2 * -1.6
                elif powerPoints2 > 0:  # if positive power
                    powerPoints2 = powerPoints2 * 1.6
                # angleOrb

                # diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle2 = 0
                if diffDegrees2 >= angleDegree:
                    diffDiffAndAngle2 = diffDegrees2 - angleDegree
                elif angleDegree > diffDegrees2:
                    diffDiffAndAngle2 = angleDegree - diffDegrees2

                # ------------------------------------------
                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck2 = 0
                powerLove2 = 0
                powerSex2 = 0
                powerDrama2 = 0

                # keep it positive - when putting points into the category
                powerPoints2a = powerPoints2
                if powerPoints2 < 0:
                    powerPoints2a = powerPoints2 * -1

                # parse the cat var
                # go thru all 4, if it has those words in the cat
                #---------------
                if "Luck" in cat:
                    powerLuck2 = powerPoints2a  # powerLuck1, powerLove1, powerSex1, powerDrama1
                    totals4powers['Luck'] += f.round_down2(powerLuck2)
                if "Love" in cat:
                    powerLove2 = powerPoints2a
                    totals4powers['Love'] += f.round_down2(powerLove2)
                if "Sex" in cat:
                    powerSex2 = powerPoints2a
                    totals4powers['Sex'] += f.round_down2(powerSex2)
                if "Drama" in cat:
                    powerDrama2 = powerPoints2a
                    totals4powers['Drama'] += f.round_down2(powerDrama2)
                # that's the simple version ... if there is
                #
                # ------------------------------------------

            # Uncomment the 1st - if & print
            #if match1=="YES": # if abs(powerPoints_P1)>0 and match=="YES": # 1-4 - P1 to P2  /  3-2 - P2 to P1
                #print(f"{i}, {word3}, {cat}, 'MATCH 1', {match1}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees4}, {diffDegrees1}, {angleDegree}, {diffDiffAndAngle1}, {angleOrb}, {angleOrbPercentUsed1}, {powerPoints1}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx4}, {bidirectional1}, {gender1}, {gender2}, {powerLuck1}, {powerLove1}, {powerSex1}, {powerDrama1}")
            #if match1=="NO": # if abs(powerPoints_P1)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, 'NO MATCH 1', {match1}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees4}, {diffDegrees1}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx4}, {bidirectional1}, {gender1}, {gender2}, -, -, -, -") # 	pl1 Rx	pl2 Rx

            # Uncomment the 1st - if & print
            #if match2=="YES": # if abs(powerPoints_P2)>0 and match=="YES": # 1-4 - P1 to P2  /  3-2 - P2 to P1
                #print(f"{i}, {word3}, {cat}, 'MATCH 2', {match2}, {planet1}, {angle}, {planet2}, {degrees3}, {degrees2}, {diffDegrees2}, {angleDegree}, {diffDiffAndAngle2}, {angleOrb}, {angleOrbPercentUsed2}, {powerPoints2}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx3}, {Rx2}, {bidirectional2}, {gender2}, {gender1}, {powerLuck2}, {powerLove2}, {powerSex2}, {powerDrama2}")
            #if match2=="NO": # if abs(powerPoints_P2)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, 'NO MATCH 2', {match2}, {planet1}, {angle}, {planet2}, {degrees3}, {degrees2}, {diffDegrees2}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx4}, {bidirectional1}, {gender1}, {gender2}, -, -, -, -") # 	pl1 Rx	pl2 Rx


    #post processing
    # this is setting up the multipliers - and turn it into percents
    t = totals4powers
    luck = t['Luck']
    luck = f.round_down2(luck/700 /1.1 *100) # the *10 is a final calibration, for Miriam's chart to mine
    love = t['Love']
    love = f.round_down2(love/400 /3 *100) # the *1.1 is a final calibration
    sex = t['Sex']
    sex = f.round_down2(sex/400 /4 *100)  # the /5 is a final calibration ... # 100 to make it a percent
    drama = t['Drama']
    drama = f.round_down2(drama/600 /3 *100)  # the /3 is a final calibration ... # 100 to make it a percent

    #additional multipliers - to get consistent numbers between 1-100%
    if type=="how I feel about it":
        luck = f.round_down2(luck / 2)
        love = f.round_down2(love / 1.2)
        sex = f.round_down2(sex / 2.5)
        drama = f.round_down2(drama / 2)

    if type == "how they feel about it":
        luck = f.round_down2(luck / 1.6)
        love = f.round_down2(love / 1.3)
        sex = f.round_down2(sex * 1.2)
        drama = f.round_down2(drama * 1.1)

    if type == "how it affects me":
        luck = f.round_down2(luck * 1.4)
        love = f.round_down2(love / 5)
        sex = f.round_down2(sex / 5)
        drama = f.round_down2(drama * 1.2)

    if type == "how it affects them":
        luck = f.round_down2(luck * 2.1 )
        love = f.round_down2(love / 1.5 )
        sex = f.round_down2(sex * 1.2)
        drama = f.round_down2(drama / 2.5)

    #print("Luck %, Love %, Sex %, Drama %") #titles
    #print(f"{luck}%, {love}%, {sex}%, {drama}%, ") #values
    var = {'Luck':luck, 'Love':love, 'Sex':sex, 'Drama':drama}
    return var

#--------------------------------------



# import ASTROLOGYfunctions as aa
# aa.csvSYNASTRYMagiAspects264_1()
def csvSYNASTRYMagiAspects264_1(): #in order
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    aspects = m.AspectsDictSynastry
    print(f"aspects: ({len(aspects)})")
    #-------------------------------
    me = aa.me() #person 1
    person = aa.person2() #person 2 gets miriam loaded
    #-------------------------------
    #today = aa.today()
    gender1 = me['info']['gender']
    gender2 = person['info']['gender']
    myPlanets = me['planets']['360']
    herPlanets = person['planets']['360']
    planets_me = aa.p360planetsToDict(myPlanets)
    planets_her = aa.p360planetsToDict(herPlanets)
    totals4powers = {'Luck':0,'Love':0,'Sex':0,'Drama':0,} # totals4powers['Luck']
    #print titles of columns
    print("'num', 'word3', 'cat', 'Match Num 1 or 2', 'match', 'planet1', 'angle', 'planet2', 'degrees1', 'degrees4', 'diffDegrees1', 'angleDegree', 'diffDiffAndAngle1', 'angleOrb', 'angleOrbPercentUsed1', 'powerPoints1', '-IF A Match-', 'anglePower', 'planetOrb1', 'planetPower1', 'planetOrb2', 'planetPower2', 'Rx1', 'Rx4', 'bidirectional1', 'gender1', 'gender2', 'powerLuck1', 'powerLove1', 'powerSex1', 'powerDrama1'")

    for i in range(len(aspects)):
        a = aspects[i]
        if len(aspects[i])>0: #if I still keep consolidating copies - this fixes if it's empty
            word3 = a['word3']
            cat = "/".join(a['cat']) #so all the categories will be in one field, for csv
            match1 = ''
            match2 = ''
            p = word3.split("-")
            planet1 = p[0]
            degrees1 = planets_me[planet1]
            degrees3 = planets_her[planet1]  # 1-4 - Per1 to Per2 / 3-2 - Per2 to Per1
            #planet 1 - Rx - person 1
            if "Rx" in degrees1:
                Rx1 = "Rx"
                degrees1 = degrees1.strip(" Rx")
            else:
                Rx1 = ""
            #planet 1 - Rx - person 2
            if "Rx" in degrees3:
                Rx3 = "Rx"
                degrees3 = degrees3.strip(" Rx")
            else:
                Rx3 = ""
            angle = p[1]
            planet2 = p[2]
            degrees2 = planets_me[planet2]
            degrees4 = planets_her[planet2]  # 1-4 - Per1 to Per2 / 3-2 - Per2 to Per1
            #planet 2 - Rx
            if "Rx" in degrees2:
                Rx2 = "Rx"
                degrees2 = degrees2.strip(" Rx")
            else:
                Rx2 = ""
            #planet 2 - Rx - person 2
            if "Rx" in degrees4:
                Rx4 = "Rx"
                degrees4 = degrees4.strip(" Rx")
            else:
                Rx4 = ""

            # bidirectional1
            if Rx1!=Rx4: # 1-4 - P1 to P2  /  3-2 - P2 to P1
                bidirectional1 = "bidirectional"
            else:
                bidirectional1 = ""

            # bidirectional2
            if Rx3!=Rx2: # 1-4 - P1 to P2  /  3-2 - P2 to P1
                bidirectional2 = "bidirectional"
            else:
                bidirectional2 = ""


            diffDegrees1 = 0 # 1-4 - P1 to P2  /  3-2 - P2 to P1
            if float(degrees1)>float(degrees4):
                diffDegrees1 = float(degrees1)-float(degrees4)
            else:
                diffDegrees1 = float(degrees4)-float(degrees1)

            diffDegrees2 = 0 # 1-4 - P1 to P2  /  3-2 - P2 to P1
            if float(degrees3) > float(degrees2):
                diffDegrees2 = float(degrees3) - float(degrees2)
            else:
                diffDegrees2 = float(degrees2) - float(degrees3)

            plo = m.planets_organized #planet_orb, power
            planetOrb1 = plo[planet1]['planet_orb']
            planetPower1 = plo[planet1]['power']
            planetOrb2 = plo[planet2]['planet_orb']
            planetPower2 = plo[planet2]['power']
            aso = m.aspects_organized # degrees, meaningful_orb, power
            angleDegree = aso[angle]['degrees']
            angleOrb = aso[angle]['meaningful_orb']
            anglePower = aso[angle]['power']

            angleOrbPercentUsed = angleOrb #diffDegrees will always be less - or more
            #if diffDegreesPlanets-angleAspectDegree==positive number ... that/angleOrb
            num1 = 0
            if diffDegrees1>angleDegree:
                num1 = diffDegrees1 - angleDegree #less than angleOrb now
            if diffDegrees1<=angleDegree:
                num1 = angleDegree - diffDegrees1 #less than angleOrb now
            #make even barely connected planets - get some - leave it at 1
            #if num1 < 1:
                #num1= num1 + .1
            angleOrbPercentUsed1 = f.round_down2(num1 / angleOrb)

            num2 = 0
            if diffDegrees2 > angleDegree:
                num2 = diffDegrees2 - angleDegree  # less than angleOrb now
            if diffDegrees2 <= angleDegree:
                num2 = angleDegree - diffDegrees2  # less than angleOrb now
            # make even barely connected planets - get some - leave it at 1
            # if num2 < 1:
                # num1= num2 + .1
            angleOrbPercentUsed2 = f.round_down2(num2 / angleOrb)

            gender1 = gender1 # "Male"
            gender2 = gender2 # "Female"

            match1 = "NO"
            if diffDegrees1>=angleDegree-angleOrb and diffDegrees1<=angleDegree+angleOrb:
                match1 = "YES"

            match2 = "NO"
            if diffDegrees2>=angleDegree-angleOrb and diffDegrees2<=angleDegree+angleOrb:
                match2 = "YES"


            # ------------------------------------------
            powerPoints1=0
            if match1 == "YES":
                # closer they are to a perfect orb of 0 - they get 100% points
                powerPoints1 = (anglePower * angleOrbPercentUsed1) * (planetPower1 + planetPower2)
                #powerPoints - reduce to orbClosePercent
                if powerPoints1<0: #if negative power
                    if bidirectional1=="bidirectional": # bidirectional1, bidirectional2
                        powerPoints1 = powerPoints1 * -1.6
                elif powerPoints1>0: #if positive power
                    powerPoints1 = powerPoints1 * 1.6
                # angleOrb

                #diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle1=0
                if diffDegrees1>=angleDegree:
                    diffDiffAndAngle1 = diffDegrees1 - angleDegree
                elif angleDegree>diffDegrees1:
                    diffDiffAndAngle1 = angleDegree - diffDegrees1

                # ------------------------------------------
                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck1 = 0
                powerLove1 = 0
                powerSex1 = 0
                powerDrama1 = 0

                #keep it positive - when putting points into the category
                powerPoints1a = powerPoints1
                if powerPoints1<0:
                    powerPoints1a = powerPoints1 * -1

                #parse the cat var
                #go thru all 4, if it has those words in the cat
                if "Luck" in cat:
                    powerLuck1 = powerPoints1a # powerLuck1, powerLove1, powerSex1, powerDrama1
                    totals4powers['Luck'] += f.round_down2(powerLuck1)
                if "Love" in cat:
                    powerLove1 = powerPoints1a
                    totals4powers['Love'] += f.round_down2(powerLove1)
                if "Sex" in cat:
                    powerSex1 = powerPoints1a
                    totals4powers['Sex'] += f.round_down2(powerSex1)
                if "Drama" in cat:
                    powerDrama1 = powerPoints1a
                    totals4powers['Drama'] += f.round_down2(powerDrama1)
                # that's the simple version ... if there is
                #
                #------------------------------------------

            # ------------------------------------------
            powerPoints2=0
            if match2 == "YES":
                # closer they are to a perfect orb of 0 - they get 100% points
                powerPoints2 = (anglePower * angleOrbPercentUsed2) * (planetPower1 + planetPower2)
                # powerPoints - reduce to orbClosePercent
                if powerPoints2 < 0:  # if negative power
                    if bidirectional2 == "bidirectional":  # bidirectional1, bidirectional2
                        powerPoints2 = powerPoints2 * -1.6
                elif powerPoints2 > 0:  # if positive power
                    powerPoints2 = powerPoints2 * 1.6
                # angleOrb

                # diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle2 = 0
                if diffDegrees2 >= angleDegree:
                    diffDiffAndAngle2 = diffDegrees2 - angleDegree
                elif angleDegree > diffDegrees2:
                    diffDiffAndAngle2 = angleDegree - diffDegrees2

                # ------------------------------------------
                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck2 = 0
                powerLove2 = 0
                powerSex2 = 0
                powerDrama2 = 0

                # keep it positive - when putting points into the category
                powerPoints2a = powerPoints2
                if powerPoints2 < 0:
                    powerPoints2a = powerPoints2 * -1

                # parse the cat var
                # go thru all 4, if it has those words in the cat
                if "Luck" in cat:
                    powerLuck2 = powerPoints2a  # powerLuck1, powerLove1, powerSex1, powerDrama1
                    totals4powers['Luck'] += f.round_down2(powerLuck2)
                if "Love|f" == cat:
                    if gender2 == "Female":
                        powerLove2 = powerPoints2a
                        totals4powers['Love'] += f.round_down2(powerLove2)
                    else:
                        powerPoints = 0
                elif "Love|m" == cat:
                    if gender2 == "Male":
                        powerLove2 = powerPoints2a
                        totals4powers['Love'] += f.round_down2(powerLove2)
                    else:
                        powerPoints = 0
                elif "Love" in cat:
                    powerLove2 = powerPoints2a
                    totals4powers['Love'] += f.round_down2(powerLove2)
                if "Sex|m" == cat:
                    # only option
                    if gender2 == "Male":
                        powerSex2 = powerPoints2a
                        totals4powers['Sex'] += f.round_down2(powerSex2)
                    else:
                        powerPoints = 0
                elif "Sex" in cat:
                    powerSex2 = powerPoints2a
                    totals4powers['Sex'] += f.round_down2(powerSex2)
                if "Drama" in cat:
                    powerDrama2 = powerPoints1a
                    totals4powers['Drama'] += f.round_down2(powerDrama2)
                # that's the simple version ... if there is
                #
                # ------------------------------------------

            if match1=="YES": # if abs(powerPoints)>0 and match=="YES": # 1-4 - P1 to P2  /  3-2 - P2 to P1
                print(f"{i}, {word3}, {cat}, 'MATCH 1', {match1}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees4}, {diffDegrees1}, {angleDegree}, {diffDiffAndAngle1}, {angleOrb}, {angleOrbPercentUsed1}, {powerPoints1}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx4}, {bidirectional1}, {gender1}, {gender2}, {powerLuck1}, {powerLove1}, {powerSex1}, {powerDrama1}")
            #if match1=="NO": # if abs(powerPoints)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, 'NO MATCH 1', {match1}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees4}, {diffDegrees1}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx4}, {bidirectional1}, {gender1}, {gender2}, -, -, -, -") # 	pl1 Rx	pl2 Rx


            if match2=="YES": # if abs(powerPoints)>0 and match=="YES": # 1-4 - P1 to P2  /  3-2 - P2 to P1
                print(f"{i}, {word3}, {cat}, 'MATCH 2', {match2}, {planet1}, {angle}, {planet2}, {degrees3}, {degrees2}, {diffDegrees2}, {angleDegree}, {diffDiffAndAngle2}, {angleOrb}, {angleOrbPercentUsed2}, {powerPoints2}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx3}, {Rx2}, {bidirectional2}, {gender2}, {gender1}, {powerLuck2}, {powerLove2}, {powerSex2}, {powerDrama2}")
            #if match2=="NO": # if abs(powerPoints)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, 'NO MATCH 2', {match2}, {planet1}, {angle}, {planet2}, {degrees3}, {degrees2}, {diffDegrees2}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx4}, {bidirectional1}, {gender1}, {gender2}, -, -, -, -") # 	pl1 Rx	pl2 Rx


    #post processing
    # this is setting up the multipliers - and turn it into percents
    t = totals4powers
    luck = t['Luck']
    luck = f.round_down2(luck/700*10*100) # the *10 is a final calibration, for Miriam's chart to mine
    love = t['Love']
    love = f.round_down2(love/400*1.1*100) # the *1.1 is a final calibration
    sex = t['Sex']
    sex = f.round_down2(sex/400/5*100)  # the /5 is a final calibration ... # 100 to make it a percent
    drama = t['Drama']
    drama = f.round_down2(drama/600/3*100)  # the /3 is a final calibration ... # 100 to make it a percent
    print("Luck %, Love %, Sex %, Drama %") #titles
    print(f"{luck}%, {love}%, {sex}%, {drama}%, ") #values




# checks For Duplicates
# in self and synastry dicts
def checkForDuplicates():
    import ASTROLOGYmagi as m
    # check for duplicates - in the short 300-400 magi lists ***
    # self = m.AspectsDictSelf
    synastry = m.AspectsDictSynastry
    list = []
    for i in range(len(synastry)):
        print(i)
        aspectWithCat = synastry[i]
        if len(aspectWithCat)>1:
            print(f"aspectWithCat: {aspectWithCat}")
            word3 = aspectWithCat['word3']
            if word3 in list:
                print(f"duplicate: ({i}) {word3}")
            else:
                list.append(word3)




#this gave me completely different results - additional aspects
def getClosestNumber(n1,n2,myNumber):
  closestDegree = min([n1, n2], key=lambda x:abs(x-myNumber))
  return closestDegree

#--------------------------------------
# import ASTROLOGYfunctions as aa
# diffDegrees2 = diffDegrees2(deg1, deg2, angleDegree)
#
# finds the diffDegCloser to the angle #near diff, and far diff
def diffDegrees2(deg1=262.111, deg2=52.111, angleDegree=150):
    #print(f"deg1 {deg1}, deg2 {deg2}, angleDegree {angleDegree}")
    deg1 = float(deg1)
    deg2 = float(deg2)
    a = angleDegree

    # THREE EXAMPLES:
    # d1 262, d2 52, a 150 # NEED the calc for this
    # d1 50, d2 142, a 90
    # d1 50, d2 52, a 0

    if deg1>deg2:
        diff1 = deg1-deg2
        diff2 = 360-deg1+deg2
        # return whatever diff, is closer to a

    elif deg2>deg1:
        diff1 = deg2 - deg1
        diff2 = 360 - deg2 + deg1
        #return whatever diff, is closer to a
    else:
        #equal
        return 0

    #print(f" Get Closest Number: Which is closest?")
    c = float(getClosestNumber(deg1, deg2, a))
    #print(f"c: {c}")
    return c
    #if the angle is so large 150 ... 180 is half ... need to check
    # the bigger minus the smaller - does not catch the match
    # when the a=150


    #262, 52, 150


# import ASTROLOGYfunctions as aa
# diff1 = diffDegrees1(deg1,deg2,angleDegree)
def diffDegrees1(deg1=262.111, deg2=52.111, angleDegree=150):
    deg1 = float(deg1)
    deg2 = float(deg2)
    if deg1>deg2:
        diff1 = deg1-deg2
    elif deg2>deg1:
        diff1 = deg2 - deg1
    else:
        diff1 = 0
    return diff1

#--------------------------------------
# import ASTROLOGYfunctions as aa
# diffDiffAndAngle = aa.diffDiffAndAngle(diffDegrees1, angleDegree)
def diffDiffAndAngle(diffDegrees, angleDegree):
    diffDiffAndAngle = 0

    if diffDegrees>=angleDegree:
        diffDiffAndAngle = diffDegrees - angleDegree
    elif angleDegree>diffDegrees:
        diffDiffAndAngle = angleDegree - diffDegrees

    return diffDiffAndAngle
#--------------------------------------


# import ASTROLOGYfunctions as aa
# powers4 = aa.csvSelfMagiAspects264_3(me, type="potential", showLines=False, showOnlyMatches=True) #True
def csvSelfMagiAspects264_3(me, type="self", showLines=False, showOnlyMatches=True): # "potential"
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    #testing this out
    aspects = m.AspectsDictSynastry
    if type=="self":
        aspects = m.AspectsDictSelf
    #print(f"aspects: ({len(aspects)})")
    #me = aa.me()
    #today = aa.today()
    gender = me['info']['gender']
    myPlanets = me['planets']['360']
    planets = aa.p360planetsToDict(myPlanets)
    totals4powers = {'Luck':0,'Love':0,'Sex':0,'Drama':0,} # totals4powers['Luck']
    #print titles of columns
    # ----------------------------
    # UNCOMMENT THIS 1 LINE:
    if showLines==True:
        print("'num', 'word3', 'cat', 'match', 'powerPoints', 'degrees1', 'degrees2', 'diffDegrees1', 'diffDiffAndAngle1', 'angleDegree', 'diffDegrees2', 'diffDiffAndAngle2', 'angleOrb', 'angleOrbPercentUsed1', 'angleOrbPercentUsed2', '-IF A Match-', 'anglePower', 'planetOrb1', 'planetPower1', 'planetOrb2', 'planetPower2', 'Rx1', 'Rx2', 'bidirectional', 'gender1', 'gender2', 'powerLuck', 'powerLove', 'powerSex', 'powerDrama', 'planet1', 'angle', 'planet2'")

    for i in range(len(aspects)):
        a = aspects[i]
        if len(aspects[i])>0: #if I still keep consolidating copies - this fixes if it's empty
            word3 = a['word3']
            cat = "/".join(a['cat']) #so all the categories will be in one field, for csv
            match = ''
            p = word3.split("-")
            planet1 = p[0]
            #print(f"finding something ... planet1: {planet1}")
            d1 = planets[planet1+"_g"].split("/")
            # -----------------
            degrees1 = d1[0]
            try:
                Rx1 = d1[1]
                declination1 = d1[2]
                distance1 = d1[3]
                speed1 = d1[4]
            except:
                Rx1 = "-"
                declination1 = "-"
                distance1 = "-"
                speed1 = "-"
            #-----------------
            angle = p[1]
            planet2 = p[2]
            d2 = planets[planet2 + "_g"].split("/")
            # -----------------
            degrees2 = d2[0]
            try:
                Rx2 = d2[1]
                declination2 = d2[2]
                distance2 = d2[3]
                speed2 = d2[4]
            except:
                Rx2 = "-"
                declination2 = "-"
                distance2 = "-"
                speed2 = "-"
            # -----------------

            if Rx1!=Rx2:
                bidirectional = "bidirectional"
            else:
                bidirectional = ""

            d1 = degrees1
            d2 = degrees2
            aso = m.aspects_organized # degrees, meaningful_orb, power
            angleDegree = aso[angle]['degrees']
            angleOrb = aso[angle]['meaningful_orb']
            anglePower = aso[angle]['power']


            #diffDegrees1 = 0
            #diffDegrees1 = aa.diffDegrees1(d1,d2,aso[angle]['degrees']) # finds the larger, minus the smaller
            #diffDegrees2 = aa.diffDegrees2(d1,d2,aso[angle]['degrees']) # finds the diffDegCloser to the angle #near diff, and far diff

            aspect_string = word3
            longer_diff, shorter_diff = aa.diffByAspectString(me, aspect_string)
            diffDegrees1 = longer_diff
            diffDegrees2 = shorter_diff

            plo = m.planets_organized #planet_orb, power
            planetOrb1 = plo[planet1]['planet_orb']
            planetPower1 = plo[planet1]['power']
            planetOrb2 = plo[planet2]['planet_orb']
            planetPower2 = plo[planet2]['power']

            angleOrbPercentUsed1 = angleOrb #diffDegrees will always be less - or more
            #if diffDegreesPlanets-angleAspectDegree==positive number ... that/angleOrb

            # for: angleOrbPercentUsed1
            num1 = 1
            if diffDegrees1>angleDegree:
                num1 = diffDegrees1 - angleDegree #less than angleOrb now
            if diffDegrees1<=angleDegree:
                num1 = angleDegree - diffDegrees1 #less than angleOrb now
            #make even barely connected planets - get some - leave it at 1
            #if num1 < 1:
                #num1= num1 + .1
            angleOrbPercentUsed1 = f.round_down2(num1 / angleOrb)

            # for: angleOrbPercentUsed2
            num2 = 1
            if diffDegrees1 > angleDegree:
                num2 = diffDegrees1 - angleDegree  # less than angleOrb now
            if diffDegrees1 <= angleDegree:
                num2 = angleDegree - diffDegrees1  # less than angleOrb now
            # make even barely connected planets - get some - leave it at 1
            # if num2 < 1:
            # num2= num2 + .1
            angleOrbPercentUsed2 = f.round_down2(num2 / angleOrb)

            # only if you know there is one: #all orbs are 10 degs or less
            # orb, orbMax = aa.getOrb(me, aspect_string="Sun-Quincunx-Chiron")

            gender1 = gender # "Male"
            gender2 = gender1

            match = "NO"
            #the far - avoiding the 360-0 point
            if diffDegrees1>=angleDegree-angleOrb and diffDegrees1<=angleDegree+angleOrb:
                match = "YES"
            #the close - using the 360-0 point
            if diffDegrees2>=angleDegree-angleOrb and diffDegrees2<=angleDegree+angleOrb:
                match = "YES"

            powerPoints=0
            if match == "YES":
                powerPoints = aa.powerFor(me, aspect_string)
                """
                # closer they are to a perfect orb of 0 - they get 100% points
                powerPoints = (anglePower * angleOrbPercentUsed1) + (planetPower1 + planetPower2)
                #powerPoints - reduce to orbClosePercent
                if powerPoints<0: #if negative power
                    if bidirectional=="bidirectional":
                        powerPoints = powerPoints * -1.6
                elif powerPoints>0: #if positive power
                    powerPoints = powerPoints * 1.6
                """
                # angleOrb

                #diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle1 = aa.diffDiffAndAngle(diffDegrees1, angleDegree)
                diffDiffAndAngle2 = aa.diffDiffAndAngle(diffDegrees2, angleDegree)


                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck = 0
                powerLove = 0
                powerSex = 0
                powerDrama = 0

                #keep it positive - when putting points into the category
                powerPoints_Pos = powerPoints
                if powerPoints<0: #if negative - switch it - to add it to the category later - must be pos
                    powerPoints_Pos = powerPoints * -1

                #parse the cat var
                #go thru all 4, if it has those words in the cat
                # prepare for these SELF use cases: ... 'Sex|b/Sex|m', 'Sex/Love|f'
                # ------------------------
                if "Luck|b" == cat:
                    if bidirectional == "bidirectional":
                        powerLuck = powerPoints_Pos
                        totals4powers['Luck'] += f.round_down2(powerLuck)
                    else:
                        powerPoints_P1 = 0
                elif "Luck" in cat:
                    powerLuck = powerPoints_Pos # powerLuck, powerLove, powerSex, powerDrama
                    totals4powers['Luck'] += f.round_down2(powerLuck)
                #------------------------

                if "Sex/Love|f"== cat: #Love is on the right - Sex will be added later normally
                    if gender1 == "Female":
                        powerLove = powerPoints_Pos #positive powerPoints
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        pass#powerPoints = 0
                elif "Luck/Love|f"== cat: #Love is on the right - Sex will be added later normally
                    if gender1 == "Female":
                        powerLove = powerPoints_Pos #positive powerPoints
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        pass#powerPoints = 0
                elif "Love|f" == cat:
                    if gender1 == "Female":
                        powerLove = powerPoints_Pos
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love|m" == cat:
                    if gender1 == "Male":
                        powerLove = powerPoints_Pos
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love" in cat:
                    powerLove = powerPoints_Pos
                    totals4powers['Love'] += f.round_down2(powerLove)
                if "Sex|m/Drama" == cat:
                    #only option
                    if gender1=="Male":
                        powerSex = powerPoints_Pos
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    else:
                        pass#powerPoints = 0
                elif "Sex|m" == cat:
                    #only option
                    if gender1=="Male":
                        powerSex = powerPoints_Pos
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    else:
                        powerPoints = 0
                elif "Sex|b/Sex|m"== cat:
                    #check both, add power once
                    if gender1 == "Male":
                        powerSex = powerPoints_Pos
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    elif bidirectional == "bidirectional":
                        powerLuck = powerPoints_Pos
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    else:
                        powerPoints = 0
                elif "Sex" in cat:
                    powerSex = powerPoints_Pos
                    totals4powers['Sex'] += f.round_down2(powerSex)
                if "Drama" in cat:
                    powerDrama = powerPoints_Pos
                    totals4powers['Drama'] += f.round_down2(powerDrama)
                # that's the simple version ... if there is

            if match == "YES":
                diffDegrees1 = f.round_down4(diffDegrees1)
                diffDegrees2 = f.round_down4(diffDegrees2)
                diffDiffAndAngle1 = f.round_down4(diffDiffAndAngle1)
                diffDiffAndAngle2 = f.round_down4(diffDiffAndAngle2)
                powerPoints = f.round_down4(powerPoints)
                powerLuck = f.round_down4(powerLuck)
                powerLove = f.round_down4(powerLove)
                powerSex = f.round_down4(powerSex)
                powerDrama = f.round_down4(powerDrama)

            # ----------------------------
            # UNCOMMENT THESE 4 LINES:
            if showLines == True:
                if match=="YES": # if abs(powerPoints)>0 and match=="YES":
                    print(f"{i}, {word3}, {cat}, {match}, {powerPoints}, {degrees1}, {degrees2}, {diffDegrees1}, {diffDiffAndAngle1}, {angleDegree}, {diffDegrees2}, {diffDiffAndAngle2}, {angleOrb}, {angleOrbPercentUsed1}, {angleOrbPercentUsed2}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}, {powerLuck}, {powerLove}, {powerSex}, {powerDrama}, {planet1}, {angle}, {planet2}, ")
                if showOnlyMatches == False:
                    if match=="NO": # if abs(powerPoints)>0 and match=="YES":
                        print(f"{i}, {word3}, {cat}, {match}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees2}, {diffDegrees1}, {diffDegrees2}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}, -, -, -, -") # 	pl1 Rx	pl2 Rx

    #post processing
    # this is setting up the multipliers - and turn it into percents

    #THIS IS FOR SELF ONLY - numbers have been adjusted
    t = totals4powers
    allcap = 170 # same as in mycosmicdna
    luck = t['Luck']
    luck = f.round(luck/allcap/5 * 100) # looks presentable
    love = t['Love']
    love = f.round(love/allcap/3 * 100)
    sex = t['Sex']
    sex = f.round(sex/allcap/5 * 100) # 100 to make it a percent
    drama = t['Drama']
    drama = f.round(drama/allcap/5 * 100) # 100 to make it a percent

    if type == "affects-you":  # further adjust
        luck = f.round(luck / allcap / 5 * 100)
        love = f.round(love / allcap / 5 * 100)
        sex = f.round(sex / allcap / 2 * 100)  # 100 to make it a percent
        drama = f.round(drama / allcap / 4 * 100)  # 100 to make it a percent

    if type=="synastry": #further adjust
        luck = f.round(luck/allcap/9 * 100)
        love = f.round(love/allcap/9 * 100)
        sex = f.round(sex/allcap/9 * 100)  # 100 to make it a percent
        drama = f.round(drama/allcap/12 * 100)  # 100 to make it a percent

    #----------------------------
    # UNCOMMENT THESE 2 LINES:
    if showLines == True:
        print("Luck %, Sex %, Love %, Drama %") #titles
        print(f"{luck}%, {sex}%, {love}%, {drama}%, ") #values

    var = {'Luck': luck, 'Sex': sex, 'Love': love, 'Drama': drama}
    return var



#--------------------------------------


# import ASTROLOGYfunctions as aa
# aa.csvSelfMagiAspects264_2()
def csvSelfMagiAspects264_2(): #in order
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    aspects = m.AspectsDictSelf
    #print(f"aspects: ({len(aspects)})")
    me = aa.me()
    #today = aa.today()
    gender = me['info']['gender']
    myPlanets = me['planets']['360']
    planets = aa.p360planetsToDict(myPlanets)
    totals4powers = {'Luck':0,'Love':0,'Sex':0,'Drama':0,} # totals4powers['Luck']
    #print titles of columns
    # ----------------------------
    # UNCOMMENT THIS 1 LINE:
    #print("'num', 'word3', 'cat', 'match', 'planet1', 'angle', 'planet2', 'degrees1', 'degrees2', 'diffDegrees', 'angleDegree', 'diffDiffAndAngle', 'angleOrb', 'angleOrbPercentUsed1', 'powerPoints', '-IF A Match-', 'anglePower', 'planetOrb1', 'planetPower1', 'planetOrb2', 'planetPower2', 'Rx1', 'Rx2', 'bidirectional', 'gender1', 'gender2', 'powerLuck', 'powerLove', 'powerSex', 'powerDrama'")

    for i in range(len(aspects)):
        a = aspects[i]
        if len(aspects[i])>0: #if I still keep consolidating copies - this fixes if it's empty
            word3 = a['word3']
            cat = "/".join(a['cat']) #so all the categories will be in one field, for csv
            match = ''
            p = word3.split("-")
            planet1 = p[0]
            degrees1 = planets[planet1]
            #planet 1 - Rx
            if "Rx" in degrees1:
                Rx1 = "Rx"
                degrees1 = degrees1.strip(" Rx")
            else:
                Rx1 = ""
            angle = p[1]
            planet2 = p[2]
            degrees2 = planets[planet2]
            #planet 2 - Rx
            if "Rx" in degrees2:
                Rx2 = "Rx"
                degrees2 = degrees2.strip(" Rx")
            else:
                Rx2 = ""

            if Rx1!=Rx2:
                bidirectional = "bidirectional"
            else:
                bidirectional = ""

            aso = m.aspects_organized # degrees, meaningful_orb, power
            angleDegree = aso[angle]['degrees']
            d1 = degrees1
            d2 = degrees2

            diffDegrees = 0
            diffDegrees = aa.diffDegrees1(d1, d2, aso[angle]['degrees'])  # finds the larger, minus the smaller
            diffDegrees2 = aa.diffDegrees2(d1,d2,aso[angle]['degrees']) # finds the diffDegCloser to the angle #near diff, and far diff

            plo = m.planets_organized #planet_orb, power
            planetOrb1 = plo[planet1]['planet_orb']
            planetPower1 = plo[planet1]['power']
            planetOrb2 = plo[planet2]['planet_orb']
            planetPower2 = plo[planet2]['power']
            #aso = m.aspects_organized # degrees, meaningful_orb, power
            #angleDegree = aso[angle]['degrees']
            angleOrb = aso[angle]['meaningful_orb']
            anglePower = aso[angle]['power']

            angleOrbPercentUsed = angleOrb #diffDegrees will always be less - or more
            #if diffDegreesPlanets-angleAspectDegree==positive number ... that/angleOrb
            num = 1
            if diffDegrees>angleDegree:
                num = diffDegrees - angleDegree #less than angleOrb now
            if diffDegrees<=angleDegree:
                num = angleDegree - diffDegrees #less than angleOrb now
            #make even barely connected planets - get some - leave it at 1
            #if num < 1:
                #num= num + .1
            angleOrbPercentUsed = f.round_down2(num / angleOrb)


            gender1 = gender # "Male"
            gender2 = gender1

            match = "NO"
            if diffDegrees>=angleDegree-angleOrb and diffDegrees<=angleDegree+angleOrb:
                match = "YES"

            powerPoints=0
            if match == "YES":
                # closer they are to a perfect orb of 0 - they get 100% points
                powerPoints = (anglePower * angleOrbPercentUsed) * (planetPower1 + planetPower2)
                #powerPoints - reduce to orbClosePercent
                if powerPoints<0: #if negative power
                    if bidirectional=="bidirectional":
                        powerPoints = powerPoints * -1.6
                elif powerPoints>0: #if positive power
                    powerPoints = powerPoints * 1.6
                # angleOrb

                #diffDiffAndAngle between these 2: 'diffDegrees'	 'angleDegree'
                diffDiffAndAngle=0
                if diffDegrees>=angleDegree:
                    diffDiffAndAngle = diffDegrees - angleDegree
                elif angleDegree>diffDegrees:
                    diffDiffAndAngle = angleDegree - diffDegrees

                # calculate the power points for Luck, Love, Sex, Drama
                powerLuck = 0
                powerLove = 0
                powerSex = 0
                powerDrama = 0

                #keep it positive - when putting points into the category
                powerPoints2 = powerPoints
                if powerPoints<0:
                    powerPoints2 = powerPoints * -1

                #parse the cat var
                #go thru all 4, if it has those words in the cat
                # prepare for these SELF use cases: ... 'Sex|b/Sex|m', 'Sex/Love|f'
                if "Luck|b" == cat:
                    if bidirectional == "bidirectional":
                        powerLuck = powerPoints2
                        totals4powers['Luck'] += f.round_down2(powerLuck)
                    else:
                        powerPoints_P1 = 0
                elif "Luck" in cat:
                    powerLuck = powerPoints2 # powerLuck, powerLove, powerSex, powerDrama
                    totals4powers['Luck'] += f.round_down2(powerLuck)
                if "Sex/Love|f"== cat: #Love is on the right - Sex will be added later normally
                    if gender1 == "Female":
                        powerLove = powerPoints2
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love|f" == cat:
                    if gender1 == "Female":
                        powerLove = powerPoints2
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love|m" == cat:
                    if gender1 == "Male":
                        powerLove = powerPoints2
                        totals4powers['Love'] += f.round_down2(powerLove)
                    else:
                        powerPoints = 0
                elif "Love" in cat:
                    powerLove = powerPoints2
                    totals4powers['Love'] += f.round_down2(powerLove)
                if "Sex|m" == cat:
                    #only option
                    if gender1=="Male":
                        powerSex = powerPoints2
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    else:
                        powerPoints = 0
                elif "Sex|b/Sex|m"== cat:
                    #check both, add power once
                    if gender1 == "Male":
                        powerSex = powerPoints2
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    elif bidirectional == "bidirectional":
                        powerLuck = powerPoints2
                        totals4powers['Sex'] += f.round_down2(powerSex)
                    else:
                        powerPoints = 0
                elif "Sex" in cat:
                    powerSex = powerPoints2
                    totals4powers['Sex'] += f.round_down2(powerSex)
                if "Drama" in cat:
                    powerDrama = powerPoints2
                    totals4powers['Drama'] += f.round_down2(powerDrama)
                # that's the simple version ... if there is

            # ----------------------------
            # UNCOMMENT THESE 4 LINES:
            #if match=="YES": # if abs(powerPoints)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, {match}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees2}, {diffDegrees}, {angleDegree}, {diffDiffAndAngle}, {angleOrb}, {angleOrbPercentUsed}, {powerPoints}, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}, {powerLuck}, {powerLove}, {powerSex}, {powerDrama}") # 	pl1 Rx	pl2 Rx
            #if match=="NO": # if abs(powerPoints)>0 and match=="YES":
                #print(f"{i}, {word3}, {cat}, {match}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees2}, {diffDegrees}, {angleDegree}, -, {angleOrb}, -, -, '-IF A Match-', {anglePower}, {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}, -, -, -, -") # 	pl1 Rx	pl2 Rx

    #post processing
    # this is setting up the multipliers - and turn it into percents
    t = totals4powers
    luck = t['Luck']
    luck = f.round_down2(luck/700*100)
    love = t['Love']
    love = f.round_down2(love/400*100)
    sex = t['Sex']
    sex = f.round_down2(sex/400*100) # 100 to make it a percent
    drama = t['Drama']
    drama = f.round_down2(drama/600*100) # 100 to make it a percent
    #----------------------------
    # UNCOMMENT THESE 2 LINES:
    #print("Luck %, Love %, Sex %, Drama %") #titles
    #print(f"{luck}%, {love}%, {sex}%, {drama}%, ") #values

    var = {'Luck': luck, 'Love': love, 'Sex': sex, 'Drama': drama}
    return var

#---------------------------------

# import ASTROLOGYfunctions as aa
# aa.csvSelfMagiAspects264_1()
def csvSelfMagiAspects264_1(): #in order
    import ASTROLOGYfunctions as aa
    import ASTROLOGYmagi as m
    aspects = m.AspectsDictSelf
    print(f"aspects: ({len(aspects)})")
    me = aa.me()
    myPlanets = me['planets']['360']
    planets = aa.p360planetsToDict(myPlanets)
    for i in range(len(aspects)):
        a = aspects[i]
        word3 = a['word3']
        cat = "/".join(a['cat']) #so all the categories will be in one field, for csv
        p = word3.split("-")
        planet1 = p[0]
        degrees1 = planets[planet1]
        #planet 1 - Rx
        if "Rx" in degrees1:
            Rx1 = "Rx"
            degrees1 = degrees1.strip(" Rx")
        else:
            Rx1 = ""
        angle = p[1]
        planet2 = p[2]
        degrees2 = planets[planet2]
        #planet 2 - Rx
        if "Rx" in degrees2:
            Rx2 = "Rx"
            degrees2 = degrees2.strip(" Rx")
        else:
            Rx2 = ""

        if Rx1!=Rx2:
            bidirectional = "bidirectional"
        else:
            bidirectional = ""

        aso = m.aspects_organized # degrees, meaningful_orb, power
        angleDegrees = aso[angle]['degrees']
        d1 = degrees1
        d2 = degrees2

        diffDegrees = 0
        diffDegrees = aa.diffDegrees1(d1, d2, aso[angle]['degrees'])  # finds the larger, minus the smaller
        diffDegrees2 = aa.diffDegrees2(d1, d2, aso[angle]['degrees'])  # finds the diffDegCloser to the angle #near diff, and far diff

        plo = m.planets_organized #planet_orb, power
        planetOrb1 = plo[planet1]['planet_orb']
        planetPower1 = plo[planet1]['power']
        planetOrb2 = plo[planet2]['planet_orb']
        planetPower2 = plo[planet2]['power']
        #aso = m.aspects_organized # degrees, meaningful_orb, power
        #angleDegrees = aso[angle]['degrees']
        angleOrb = aso[angle]['meaningful_orb']
        anglePower = aso[angle]['power']

        gender1 = "Male"
        gender2 = gender1

        match = ""

        print(f"{i}, {word3}, {cat}, {match}, {planet1}, {angle}, {planet2}, {degrees1}, {degrees2}, {diffDegrees}, {angleOrb}, {anglePower}, '-IF A Match-', {planetOrb1}, {planetPower1}, {planetOrb2}, {planetPower2}, {Rx1}, {Rx2}, {bidirectional}, {gender1}, {gender2}") # 	pl1 Rx	pl2 Rx



# import ASTROLOGYfunctions as aa
# aa.selfMagiAspects264()
def selfMagiAspects264(): #in order
    import ASTROLOGYmagi as m
    aspects = m.AspectsDictSelf
    print(f"aspects: ({len(aspects)})")
    for i in range(len(aspects)):
        aspectInOrder = aspects[i]
        print(f"Aspect {i} of 264) aspectInOrder: {aspectInOrder}")


#-------------------------------
# Re-Number - the array lists
# import ASTROLOGYfunctions as aa
# aa.parse3wordsReNumber(start_with_num=224)

# Re-Number - the array lists
def parse3wordsReNumber(start_with_num=224):
    import FUNCTIONS as f
    lines = f.readFile("!parse3words.txt")
    # start with 224
    c=start_with_num
    for line in lines: # '0: {'word3': 'Venus-Opposed-Neptune', 'cat': ['Drama'] },'
        l = line.strip("\n").split(": {")
        newline = str(c)+": {"+str(l[1]) #remake the line - with the new number
        print(newline)
        c += 1
#-------------------------------

# import ASTROLOGYfunctions as aa

def isAngleMatch(planet1Degrees,planet2Degrees,angleName,angleInfo):
    # ---------------------------
    p1 = planet1Degrees.split(": ") #degrees could have ' Rx' after
    pl1 = p1[0]
    dg1 = p1[1]
    if " Rx" in dg1:
        Rx1 = "retrograde"
        dg1 = dg1.replace(" Rx","")
    else:
        Rx1 = "direct"
    #---------------------------
    dg1 = float(dg1)

    p2 = planet2Degrees.split(": ")  # degrees could have ' Rx' after
    pl2 = p2[0]
    dg2 = p2[1]
    if " Rx" in dg2:
        Rx2 = "retrograde"
        dg2 = dg2.replace(" Rx", "")
    else:
        Rx2 = "direct"
    # ---------------------------
    dg2 = float(dg2)
    # angleName
    #
    # angleInfo:
    # {'class': 'Major', 'degrees': 120, 'meaningful_orb': 6.5, 'power': 10, 'definition': 'Harmonious: Easy flow - passive - Cosmic Gift - Supportive and Helpful'}

    # need the following to determine a match
    orb = angleInfo['meaningful_orb']
    angleDegrees = angleInfo['degrees']
    planet1deg360 = dg1
    planet2deg360 = dg2
    # a function to determine the difference in degrees from those 2
    DegreesDiff = dg1-dg2
    if DegreesDiff<0:
        DegreesDiff = dg2-dg1
    if DegreesDiff>angleDegrees-orb and DegreesDiff<angleDegrees+orb:
        # it's a match
        return True
    else:
        # it's not a match
        return False



# import ASTROLOGYfunctions as aa
# titles = aa.magiTitles(word3) #for only 1 angle3word
# the 2 indexes available: ['word3'] ['magiTitleString']
#
# a group of these: {"word3":word3, "magiTitleString":magiTitleString}
def magiTitles(word3): # Sun-Conjunct-Jupiter
    #print(f"going to look up & LIST all - magi aspects - connected to: {word3}")
    import FUNCTIONS as f

    # looping thru the linkages
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    entries = []
    var = {}
    c = 0
    # ---------------------------------------------------------
    # ONLY LOOKING AT 'SELF' ASPECTS - NOT RELATIONSHIP-SYNASTRY
    # ---------------------------------------------------------
    # SELF, SYNASTRY ...
    for thing in m.specialAspects["self"]:
        #print(f"thing: {thing}") #titles, in a string
        info = m.specialAspects["self"][thing]
        #print(f"info: {info}") # a *LIST* of 3words
        #here is the entire list of 3 words
        info1str = ' ... '.join(info)
        #print(f"info1str: {info1str}")  # a string of 3words
        #print(f"looking for: {word3}")
        #timesItsFound = info1str.count(word3)
        #-----------------------------------------------------------------
        numTimesFound = f.isStringFound(content=info1str, findMe=word3)
        # -----------------------------------------------------------------
        if numTimesFound>0:
            print(f"\ninfo1str: {info1str}")  # a string of 3words
            print(f"looking for: {word3}")
            print(f"numTimesFound: {numTimesFound} - is how many times it's in the info1str string")
            print(f"thing: {thing}")
            var[word3] = {}
            var[word3] = {thing}
            print(f"var: {var}")
            entries.append(var)
            #exit()

    return entries

# magiTitles(word3): # Sun-Conjunct-Jupiter





# just returns true or false, if it's a magi 1+
#
# going to look up - magi aspect - if this is one {word3}
# IS a 3word ALSO A MAGI Aspect - TRUE OR FALSE (Sun-Conjunct-Jupiter)

# import ASTROLOGYfunctions as aa
# TrueFalse = isThis1Magi(word3) #Sun-Conjunct-Jupiter

# go thru all & append - just looking for: 1 3word, need: all title matches
def isThis1Magi(word3): # IT ALREADY WORKS ...
    #print(f"going to look up - magi aspect - if this is one {word3}")

    #looping thru the linkages
    import ASTROLOGYmagi as m
    entries = []
    c = 0
    for aspectTitle in m.specialAspects:
        #---------------------------------------------------------
        # ONLY LOOKING AT 'SELF' ASPECTS - NOT RELATIONSHIP-SYNASTRY
        #---------------------------------------------------------
        # SELF, SYNASTRY ...
        if aspectTitle == "self":  # synastry, self - the 2 parts of the array
            #print(f"\n{c}) aspect title (self or synastry): {aspectTitle}")
            # 0) aspect title: self ... 44 planetToPlanet aspects
            # 1) aspect title: synastry ... 71 planetToPlanet aspects
            planetToPlanets = m.specialAspects[aspectTitle]

            # print(f" ... planetToPlanet {len(planetToPlanets)} aspects: {planetToPlanets}")
            # f.print2(planetToPlanets)
            # "Chiron-Opposed-Amor"
            c2 = 0
            for planetAspect in planetToPlanets:
                linkages = planetToPlanets[planetAspect]
                # print(f"linkages: {linkages}")
                # print(f"planetAspect: {planetAspect}")
                # f.print2(planetAspect)
                c3 = 0
                for linkage in linkages:
                    # print(f"single linkage ... {linkage}")
                    p = linkage.split("-")
                    planetName1 = p[0]
                    angle = p[1]  # you take this as a template and compare those from both birthcharts
                    planetName2 = p[2]

                    if len(m.aspects_organized[angle]) >= 1:  # gets rid of last row error
                        word3_this = f"{planetName1}-{angle}-{planetName2}"
                        #----------------------------------------------------
                        # ONLY RETURNS TRUE - IF THE 3name's ARE THE SAME:
                        # ----------------------------------------------------
                        #print(f"word3 ({word3}) ==? word3_this ({word3_this})")
                        if word3 == word3_this:
                            return True
                        # ----------------------------------------------------
                    c3 += 1
                c2 += 1
        # loop through these - I had it before:
        # 'Jupiter-Conjunct-Vesta'
        c += 1

    return False

#------------------------------
# import ASTROLOGYfunctions as aa
# magiTitleGroups = aa.whatMagi(matched)
# magiTitleGroups: [[], [], [{'word3': 'Sun-Conjunct-Jupiter', 'magiTitleString': 'Super Aspect (A Winner-Powerful, Unique, Creative) (Sun-Jupiter,Uranus,Neptune,Pluto Venus-Jupiter,Uranus,Neptune,Pluto,Chiron Jupiter-Pluto,Uranus,Neptune Uranus-Pluto Pluto-Chiron) (Luck)'}], [], [], [{'word3': 'Sun-Conjunct-Pluto', 'magiTitleString': 'Iron Will (Cannot be pushed around) (Sun-Conjunct-Pluto) (Luck)'}, {'word3': 'Sun-Conjunct-Pluto', 'magiTitleString': 'Super Aspect (A Winner-Powerful, Unique, Creative) (Sun-Jupiter,Uranus,Neptune,Pluto Venus-Jupiter,Uranus,Neptune,Pluto,Chiron Jupiter-Pluto,Uranus,Neptune Uranus-Pluto Pluto-Chiron) (Luck)'}, {'word3': 'Sun-Conjunct-Pluto', 'magiTitleString': 'Sports Champion Aspect (Luck)'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'word3': 'Venus-Conjunct-Uranus', 'magiTitleString': 'Financial MAGIC - SILVER (Success-Business-Partnership-Earnings) (Venus,Jupiter,Uranus,Neptune) (Luck)'}, {'word3': 'Venus-Conjunct-Uranus', 'magiTitleString': 'Super Aspect (A Winner-Powerful, Unique, Creative) (Sun-Jupiter,Uranus,Neptune,Pluto Venus-Jupiter,Uranus,Neptune,Pluto,Chiron Jupiter-Pluto,Uranus,Neptune Uranus-Pluto Pluto-Chiron) (Luck)'}, {'word3': 'Venus-Conjunct-Uranus', 'magiTitleString': 'Male - Ladies Man -OR- Female - Who Just Wants to Have Fun (No Strings Attached) (Venus-Uranus) (Sex)'}], [], [], [], [], [], [], [], [], [], [], [], [{'word3': 'Mars-Square-Uranus', 'magiTitleString': 'Wanderer - Wants a Satisfying Relationship (Venus,Mars,Pluto,Juno-Uranus) (Drama)'}], [{'word3': 'Mars-Trine-Neptune', 'magiTitleString': 'Sports Champion Aspect (Luck)'}], [{'word3': 'Mars-Sextile-Pluto', 'magiTitleString': 'Sexual Aspect II-B (good - Other Aspects) (Venus-Mars,Venus-Pluto,Mars-Pluto) (Sex)'}], [], [], [], [], [], [], [], [], [], [], [], [{'word3': 'Jupiter-Conjunct-Pluto', 'magiTitleString': 'SUPER SUCCESS (Jupiter-Pluto) (Luck)'}, {'word3': 'Jupiter-Conjunct-Pluto', 'magiTitleString': 'Financial MAGIC - GOLD (Success-Business-Partnership-Earnings) (Chiron,Venus,Jupiter,Pluto) (Luck)'}, {'word3': 'Jupiter-Conjunct-Pluto', 'magiTitleString': 'Super Aspect (A Winner-Powerful, Unique, Creative) (Sun-Jupiter,Uranus,Neptune,Pluto Venus-Jupiter,Uranus,Neptune,Pluto,Chiron Jupiter-Pluto,Uranus,Neptune Uranus-Pluto Pluto-Chiron) (Luck)'}, {'word3': 'Jupiter-Conjunct-Pluto', 'magiTitleString': 'Sports Champion Aspect (Luck)'}], [{'word3': 'Jupiter-Quincunx-Chiron', 'magiTitleString': 'Super Aspect - Cinderella MAGIC-LUCKY (Sun,Jupiter,Neptune,Uranus,Pluto,with-CHIRON) (Luck)'}, {'word3': 'Jupiter-Quincunx-Chiron', 'magiTitleString': 'Financial MAGIC - GOLD (Success-Business-Partnership-Earnings) (Chiron,Venus,Jupiter,Pluto) (Luck)'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [{'word3': 'Uranus-Opposed-Chiron', 'magiTitleString': 'Infidelity Problem-Causer - Ability and Desire To Cause Problems for Someone you Have an Affair with and Really Mess Up their Current Relationship (if they have one) (Uranus-Chiron) (Drama)'}], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
#
# among the matches, list the magi title strings? - simple - easy - that's all
# TAKES A LIST, RETURNS A LIST, or an empty list
def whatMagi(whatAspectsMatched):
    matched = whatAspectsMatched # matched as an aspect ... now is it a magi aspect?

    magiTitleGroups = entries = []

    import ASTROLOGYfunctions as aa
    # f.print4(matched,"matched")
    for match in whatAspectsMatched:
        # {'linkage-YES-MATCH': 'Sun-Conjunct-Jupiter', 'planet1': 'Sun', 'planetDegrees1': 'Sun: 198', 'planet2': 'Jupiter', 'planet2degrees': 'Jupiter: 200', 'angleName': 'Conjunct', 'angleInfo': {'class': 'Major', 'degrees': 0, 'meaningful_orb': 10, 'power': 15, 'definition': 'Harmonious-Dynamic: Usually Imparts Power - Close Bond and Merging of Energies - Continually Influence Eachother - Same Energy {Moon/Venus or Sun/Mars} Increased Potential - Otherwise its Inhibited'}}
        # --- UNCOMMENT - TO SEE THE MATCH ---
        #print(f"match1 ({len(match)}): {match}")
        #everything used to make the decision on a match
        #IS IT A MAGI ANGLE?
        # and IF SO, LOG IT - NOTE THAT YOU FOUND ONE
        #all you need is the 3name:

        word3 = match['linkage-YES-MATCH'] # that contains the 3word linkage title

        #print(f"is this a magi?: {word3}")
        #Sun-Conjunct-Jupiter

        #---------------------------------------------------
        # is this 1, single '3word' found in the magi array, under a title? (for self)
        #---------------------------------------------------
        TrueFalse = aa.isThis1Magi(word3) #go thru all & append - just looking for all title matches
        if TrueFalse==True:
            #-------------------------------------------------------
            #
            # trying to find out what magi info I have on that 3word
            #
            # -------------------------------------------------------

            #print(f"\nis it a match?  ANSWER: * {TrueFalse} *")
            #next is how many times does it occur
            # -----------------------------------------
            #
            titlesGroup = magiTitles(word3)  # ... in all the magi titles, get the word3's title's
            #
            #-----------------------------------------
            if titlesGroup is None: #skip bad lines - I think
                pass
            else:
                if len(titlesGroup)>1:
                    magiTitleGroups.append(titlesGroup)

    return magiTitleGroups


#----------------------------

# angleInfo:
# Trine ... {'class': 'Major', 'degrees': 120, 'meaningful_orb': 6.5, 'power': 10, 'definition': 'Harmonious: Easy flow - passive - Cosmic Gift - Supportive and Helpful, This Energy Comes Naturally and FREE - Planets are usually in Same Element but different Quality - But if Too many Trines, Laziness might Develop since things are too easy'}


# uses the angles, and checks sun to every other planet, and then moon to all, etc...
# it only iterates over all of the angles to check if there is a match - just in the angles
# I want to see this data
# import ASTROLOGYfunctions as aa
# matched, notMatched = aa.whatAspects(me)
def whatAspects(me):
    import FUNCTIONS as f
    import ASTROLOGYmagi as m
    import ASTROLOGYfunctions as aa

    matched = []
    notMatched = []

    planets = planetsP2 = me['planets']['360']
    #print(f"planets ({len(planets)})")
    #f.print2(planets)
    #print(f"planets ({len(planets)})")
    #print("exiting")
    #exit()
    for planetDegrees1 in planets: # this gets planet 1
        #print(f"planetDegrees1: {planetDegrees1}")
        #print("exiting")
        #exit()
        #check each angle for this planet - to all other planets
        for planetDegrees2 in planetsP2: # this gets planet 2
            if planetDegrees1 != planetDegrees2:  # ... if it's the same planet - skip it
                plName1 = aa.getPlanetName(planetDegrees1)
                plName2 = aa.getPlanetName(planetDegrees2)
                #print(f"planetDegrees1: {planetDegrees1} ... planetDegrees2: {planetDegrees2}")
                for angle in m.magiAngles:
                    words3 = f"{plName1}-{angle}-{plName2}"
                    #print(f"angle: {angle} ... is it a match?")
                    #print(f"m.magiAngles[angle]: {m.magiAngles[angle]}")
                    #planet values are 360 - PlanetName: Degrees ... angle is angle name
                    #print(f"planet1: {planet1} ... planet2: {planet2} ... angle: {angle} ... {m.magiAngles[angle]}")
                    match = isAngleMatch(planetDegrees1,planetDegrees2,angle,m.magiAngles[angle])
                    if match==True:
                        # print("saving match")
                        # string = f" ** YES A MATCH ** ... {words3} ... planet1: {planetDegrees1} ... planetDegrees2: {planetDegrees2} ... angle: {angle} ... {m.magiAngles[angle]}"
                        # print(string)
                        dict = {'linkage-YES-MATCH':words3, "planet1":plName1, "planetDegrees1":planetDegrees1, "planet2":plName2, "planet2degrees":planetDegrees2,"angleName":angle,"angleInfo":m.magiAngles[angle]}
                        matched.append(dict)
                    elif match==False:
                        # string = f"NOT A MATCH ... planet1: {planetDegrees1} ... planetDegrees2: {planetDegrees2} ... angle: {angle} ... {m.magiAngles[angle]}"
                        # print(string)
                        dict = {'linkage-NO-MATCH': words3, "planet1": plName1, "planetDegrees1": planetDegrees1, "planet2": plName2, "planet2degrees": planetDegrees2, "angleName": angle, "angleInfo": m.magiAngles[angle]}
                        notMatched.append(dict)

    return matched, notMatched




# import ASTROLOGYfunctions as aa
# aa.
def magiAspects(me): #returns a list of 3names
    import FUNCTIONS as f
    import ASTROLOGYmagi as m
    magiArray = m.specialAspects
    #print(f"magiArray: ({len(magiArray)}):")
    #f.print2(magiArray)
    #print(f"magiArray: ({len(magiArray)}):")
    for one in magiArray['synastry']:
        #print(f"one: ({len(one)}): {one}")
        magiAspectGroup = magiArray['synastry'][one]
        #print(f"magiAspectGroup: ({len(magiAspectGroup)}): {magiAspectGroup}")
        for magiLinkage in magiAspectGroup:
            print(f"magiLinkage: {magiLinkage}")

    #magiAngles = m.aspects_organized

    # returns a list of 3names




#the numbers of rows are a little off - check the helper functions
# import ASTROLOGYfunctions as aa
# aa.linkagesOfAllPlanetsBy12PlanetsLoop() ... why are the rows less than the total linkages?
def linkagesOfAllPlanetsBy12PlanetsLoop():
    import ASTROLOGYmagi as m
    planetsAll = m.planets12

    for planet in planetsAll:

        import FUNCTIONS as f
        import ASTROLOGYfunctions as aa
        planetName=planet
        totalLinkagesForPlanet, rows = aa.linkagesByPlanet(planet=planetName)
        print(f"TOTAL LINKAGES: {totalLinkagesForPlanet} # linkages for {planetName}")
        print(f"rows: ({len(rows)})")
        print(f"TOTAL LINKAGES: {totalLinkagesForPlanet} # linkages for {planetName}")
        #f.print2(rows)
        print("\n\n----------------------------------\n\n")


#-------------------------------


def todayPlanets(personInfo):
    print(f"personInfo: {personInfo}")
    print("exiting")
    exit()
    import ASTROLOGYfunctions as aa
    city = personInfo["city"]
    timezone = personInfo["timezone"]
    dt = personInfo["datetime"].split(" ")  # '1981-10-12 03:06:00'
    date = dt[0]
    d1 = date.split("-")
    y = int(d1[0])
    m = int(d1[1])
    d = int(d1[2])
    time = dt[1]
    t = time.split(":")
    h = int(t[0])
    m1 = int(t[1])

    # -- load in the birthchart - from the user info above --

    # aa.cache1Birthchart() adds retrograde
    planets360 = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, timezone=timezone, city=city)
    # print(f"planets360: {planets360}") #should have Rx on some
    planets30 = aa.degrees30convert(planets360)
    # print(f"planets30: {planets30}")

    return planets360, planets30




def personPlanets(personInfo={}):
    if len(personInfo)>1:
        #print(f"personInfo: {personInfo}")
        import ASTROLOGYfunctions as aa
        city = str(personInfo["city"])
        #print(f"city: {city}")
        #print('exiting')
        #exit()
        timezone = personInfo["timezone"]
        dt = personInfo["datetime"].split(" ")  # '1981-10-12 03:06:00'
        date = dt[0]
        d1 = date.split("-")
        y = int(d1[0])
        m = int(d1[1])
        d = int(d1[2])
        time = dt[1]
        t = time.split(":")
        h = int(t[0])
        m1 = int(t[1])

        # -- load in the birthchart - from the user info above --

        # aa.cache1Birthchart() adds retrograde
        planets360 = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, timezone=timezone, city=city)
        # print(f"planets360: {planets360}") #should have Rx on some
        planets30 = aa.degrees30convert(planets360)
        # print(f"planets30: {planets30}")

        return planets360, planets30
    return False, False

# import ASTROLOGYfunctions as aa
# person = aa.person()

#remember:
# the midpoints do not have a direction - when calculating quincunxes, I think, it's a new point


#save the state with 'around' it
# import ASTROLOGYfunctions as aa
# planets = aa.cache1Birthchart(y=1981, m=10, d=12, h=3, m1=6, timezone=-5, city="Kansas City, MO")
def cache1Birthchart(y=1981, m=10, d=12, h=9, m1=6, timezone=-6, city="Kansas City, MO"):
    #print(2)
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    # save the string - cache it
    lat, long = aa.cacheTheCity(city) # get this info from the city
    foldernameCSV = "birthchart-cache/csv/"
    lat, long = aa.cacheTheCity(city)
    # 2022-2-27--12-0--33N26-112W4.csv ... get the format
    filenameCSV = f"{y}-{m}-{d}--{h}-{m1}--{lat}-{long}.csv"  # db_pdnabank2.txt[4] = "timezone" "-5" ...
    #print(f"filenameCSV: {filenameCSV}")

    filenameCSV = foldernameCSV + filenameCSV
    status = f.fileExists(filenameCSV)
    if status == True: # print("file exists")
        # load a cached birthchart
        planets360 = aa.load1Birthchart(filenameCSV=filenameCSV)
        # print(f"planets360 {len(planets360)}: {planets360}")
        return planets360
    elif status == False:  # print("file doesn't exist")
        # cache a birthchart
        date = f"{d}.{m}.{y}"
        time = f"{h}:{m1}:00"
        # for an accurate chart - adjust the time - with -timezone or +timezone (hours different)
        dateNew, timeNew = aa.applyTimezoneOffset(tzOffset=timezone, date=date, time=time)
        # print(f"dateNew: {dateNew} ... timeNew: {timeNew}")
        # --get the swetest generated birthchart--
        planets360 = aa.birthchartSWETEST(city=city, dateDMY=dateNew, timeWithOffset=timeNew)
        # print(f"planets360 {len(planets360)}: {planets360}")
        # write the planets we've collected above - to csv cache
        CSVstring = ""
        for planet in planets360:
            CSVstring += planet + ", "
        #print(f"CSVstring: {CSVstring}")
        CSVstring = CSVstring[:len(CSVstring) - 2] #remove the last 2 chars ... ', '

        # write the planets we've collected above - to csv cache
        aa.birthchartCSVsave(filenameCSV, CSVstring) #SAVES THE CSV FILE HERE

        #print(f"planets360 {len(planets360)}: {planets360}")
        return planets360





#save the state with 'around' it
# import ASTROLOGYfunctions as aa
# planets = aa.load1Birthchart(y=1981, m=10, d=12, h=3, m1=6, timezone=-5, city="Kansas City, MO")
def load1Birthchart(filenameCSV="file.csv"): # format: birthchart-cache/csv/1981-10-12--9-6--39N6-94W34.csv
    #it already exists ... just load it now
    import FUNCTIONS as f

    line1 = f.readFile(filenameCSV)
    planets = line1[0].split(", ")
    #print(f"planets-5 ({len(planets)}): {planets}")
    #read file
    #return planets
    return planets #52 - geo and helio




#-------------------------------

#---------------
# NOTE: WHENEVER I ADD NEW ASTROIDS - I HAVE TO RERUN THIS FUNCTION - TO ADD THE NEW ONES IN
#----------------
#runs through everyone in my pdnabank and caches their birthchart as csv - using swetest
# import ASTROLOGYfunctions as aa
# aa.cacheAllBirthcharts()
def cacheAllBirthcharts():
    import ASTROLOGYfunctions as aa
    people = aa.pdnaBankGetMyPeopleCSV_BirthchartStuff()
    # people - has ... name, datetime, city, timezone, id, pic - for each entry
    #print(f"people ({len(people)}) {people}")
    c=0
    for person in people:
        #print(f"{c}) person ({len(person)}): {person}")
        name = person[0]
        datetime = person[1]
        d2 = datetime.strip('"').split(" ")
        date = d2[0]
        d3 = date.split("-")
        y = d3[0]
        m = d3[1]
        d = d3[2]
        time = d2[1]
        t2 = time.split(":")
        h = t2[0]
        m1 = t2[1]
        city = person[2].strip('"')
        timezone = person[3]
        print(f"{c}) ... y={y}, m={m}, d={d}, h={h}, m1={m1}, timezone={timezone}, city={city}")
        # import ASTROLOGYfunctions as aa
        planets = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, timezone=timezone, city=city)
        c += 1




#-------------------------------

# import ASTROLOGYfunctions as aa
# decLat, decLong = aa.decimalLatLong(city="Kansas City, MO")
def decimalLatLong(city="Kansas City, MO"):
    import ASTROLOGYfunctions as aa
    import FUNCTIONS as f
    decLat, decLong = aa.mapQuestLatLong(city)
    return decLat, decLong



# import ASTROLOGYfunctions as aa
# dateDMY = aa.fixDateDMY(dateDMY="12.10.1981")
#if any values are less than 10, pad them as a string, with a leading zero
def fixDateDMY(dateDMY="12.10.1981"):
    d1 = dateDMY.split(".")
    d = int(d1[0])
    m = int(d1[1])
    y = int(d1[2])
    if d<10:
        d = f"0{d}"
    if m < 10:
        m = f"0{m}"
    string = f"{d}.{m}.{y}"
    return str(string)


# import ASTROLOGYfunctions as aa
# timeWithOffset = aa.fixTimeHM(timeWithOffset="9:15:00")
#if any values are less than 10, pad them as a string, with a leading zero
def fixTimeHM(timeWithOffset="9:15:00"):

    t = timeWithOffset.split(":")
    h = int(float(t[0].strip("'")))
    m1 = int(t[1])
    if h < 10:
        h = f"0{h}"
    if m1<10:
        m1 = f"0{m1}"
    #rebuild the string
    string = str(f"{h}:{m1}:00")
    return string


# import ASTROLOGYfunctions as aa
# decimalSpeed = aa.getSpeedNumFromSwetest(speed="-0- 2'26.5772") # 0-27'17.5785, 1- 7'17.5587, 14-32'42.0875
def getSpeedNumFromSwetest(speed="-0- 2'26.5772"):
    # split on the minute symbol "-"
    s = speed.split("-")
    if s[0]=="": #it was negative
        return -1

    decimalSpeed = 1
    return decimalSpeed
    #... if a dash is on the left side of the number, it's negative #-0- 2'26.5772
    # return a decimal, pos or neg


# import ASTROLOGYfunctions as aa
# Rx = aa.makeRxString(speedSwetest)
def makeRxString(speedSwetest="-0- 2'26.5772"):
    import ASTROLOGYfunctions as aa
    decimalSpeed = aa.getSpeedNumFromSwetest(speedSwetest)
    direction = "direct"  # default - direct - if speed is positive - it's moving in it's normal direction
    if decimalSpeed < 0:  # if it's less than zero - it's moving backwards - from it's normal direction
        direction = "retrograde"
    # --------------------------
    RxString = "" #direct is blank
    if direction == "retrograde":
        RxString = " Rx"  # the space that speperates it from the degrees is here
    else:
        RxString = ""
    return RxString

# import ASTROLOGYfunctions as aa
# aa.areSignsReversed(num1,num2)
def areSignsReversed(num1,num2):
    num1 = float(num1)
    num2 = float(num2)
    reversed = False

    # ----------CONTRAPARALLEL-----------
    #if num 1 is pos, if num 2 is negative:
    if num1>=0 and num2<0:
        reversed=True
    #if num 2 is pos, if num 1 is negative:
    elif num2>=0 and num1<0:
        reversed=True
    #----------PARALLEL-----------
    #if both numbers are positive or 0
    elif num1>=0 and num2>=0:
        reversed=False
    #if both numbers are negative
    elif num1<0 and num2<0:
        reversed=False

    return reversed


# import ASTROLOGYfunctions as aa
# aa.parseDegreesSweToDecimal(l[1].strip())
def parseDegreesSweToDecimal(degreesString="-2/28'19.1097"): #in degrees # declination: '-16/53' 2.9113'
    import FUNCTIONS as f
    s = degreesString.split("/")
    degree = int(s[0].strip()) # the only one that can be negative
    #if it finds a negative - minus - before the number - keep it negative at the end
    negative = s[0].strip().count("-")
    makeNeg = False #default ... it's a positive number
    if negative>0: #it found a negative sign - to the left of the number
        makeNeg=True
        degree = abs(degree) #take off the negative - until the end
    minSec = s[1]
    m = minSec.split("'")
    min = float(m[0].strip())/60
    sec = float(m[1].strip().strip('"'))/3600 #float

    totalDecimal = 0
    if degree<0:
        totalDecimal = f.round_down4(degree - min - sec)
    if degree==0:
        totalDecimal = f.round_down4(min + sec)
    if degree>0:
        totalDecimal = f.round_down4(degree + min + sec)

    if makeNeg==True:
        totalDecimal = totalDecimal * -1

    return totalDecimal



# import ASTROLOGYfunctions as aa
# aa.makePlanetStringSwe2(line)
def makePlanetStringSwe2(line="Moon   19/10' 4.4701   -0/ 0'40.3936   1.000116403   1/ 1'20.1435", type="h"): #g, h ... return long planet string with / seperating everything
    import ASTROLOGYfunctions as aa
    import FUNCTIONS as f
    l = line.strip('b"').split("  ")

    # clean whitespace for each
    planetName = l[0].strip() + "_" + type
    degrees = aa.parseDegreesSweToDecimal(l[1].strip())  # in degrees # '-2/28'19.1097'
    declination = aa.parseDegreesSweToDecimal(l[2].strip())  # in degrees
    distance = f.round_down4(float(l[3].strip()))  # in Decimal - round down
    speed = aa.parseDegreesSweToDecimal(l[4].strip())  # in parseDegreesSweToDecimal()
    if speed < 0:  # it's negative
        Rx = "Rx"
    else:
        Rx = "Rx0"
    # Rx = pos or neg - from speed
    # print(f"{c}) planetName: '{planetName}', degrees: '{degrees}', declination: '{declination}', distance: '{distance}', speed: '{speed}', Rx: {Rx}")
    string = f'{planetName}: {degrees}/{Rx}/{declination}/{distance}/{speed}'
    return string



# import ASTROLOGYfunctions as aa
# aa.makePlanetStringSwe(line)
def makePlanetStringSwe(line="swetest line with degs/and/decs", type="g"): #g, h ... return long planet string with / seperating everything
    TrueFalse = isinstance(line, str)
    if TrueFalse == "False":
        print("error - not a string - in makePlanetStringSwe()")
    if TrueFalse == "True":

        print(f"line ({len(line)}): {line}")
        print("exiting")
        exit()
        import ASTROLOGYfunctions as aa
        import FUNCTIONS as f
        #print(f"line: {line}")

        l = line.strip('b"').split("  ")
        #print(f"l: {l}")

        #clean whitespace for each
        planetName = l[0].strip()+"_"+type
        degrees = aa.parseDegreesSweToDecimal(l[1].strip()) #in degrees # '-2/28'19.1097'
        declination = aa.parseDegreesSweToDecimal(l[2].strip()) #in degrees
        distance = f.round_down4(float(l[3].strip())) #in Decimal - round down
        speed = aa.parseDegreesSweToDecimal(l[4].strip()) # in parseDegreesSweToDecimal()
        if speed<0: #it's negative
            Rx = "Rx"
        else:
            Rx = "Rx0"
        #Rx = pos or neg - from speed
        #print(f"{c}) planetName: '{planetName}', degrees: '{degrees}', declination: '{declination}', distance: '{distance}', speed: '{speed}', Rx: {Rx}")
        string = f'{planetName}: {degrees}/{Rx}/{declination}/{distance}/{speed}'
        return string


# import ASTROLOGYfunctions as aa
# planets = aa.birthchartSWETEST(city="Kansas City, MO", datetime="10.12.1981 3:15:00")
# -5:00, some countries use 30, or 45m, so I need to add that in
#add retrograde
def birthchartSWETEST(city="Kansas City, MO", dateDMY="12.10.1981", timeWithOffset="9:15:00"):

    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa

    #FIX - (pad with leading zero) - when num is less than 10
    timeWithOffset = aa.fixTimeHM(timeWithOffset)
    dateDMY = aa.fixDateDMY(dateDMY)

    decLat, decLong = aa.decimalLatLong(city) #accuracy - in swetest

    #print(f"decLat: {decLat} ... decLong: {decLong} ... should be -94")
    # need lat long in decimal form - for the houses - 10th house
    commandString = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -b{dateDMY} -ut{timeWithOffset} -p0123456789mDFGHI -geopos{decLong},{decLat} -head"
    commandString2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -b{dateDMY} -ut{timeWithOffset} -p0123456789mCDFGHI -geopos{decLong},{decLat} -hel -head"
    #astroid AMOR 1221:
    commandStringAmor = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1221 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringAmor2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1221 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringEros = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs433 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringEros2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs433 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringSappho = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs80 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringSappho2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs80 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringLilith = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1181 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringLilith2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1181 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringHousesMidheaven = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -p -eswe -house{decLong},{decLat} -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    # print(f"cmd is it the same?: {commandStringHousesMidheaven}")
    commandStringNorthNode = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -pm -eswe -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringCeres = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringCeres2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringSedna = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs90377 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringSedna2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs90377 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringOdin = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs3989 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringOdin2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs3989 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringMidas = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1981 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringMidas2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs1981 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringQuaoar = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs50000 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringQuaoar2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs50000 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"
    commandStringErisUB313 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs136199 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -head"
    commandStringErisUB313_2 = f"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -ps -xs136199 -b{dateDMY} -ut{timeWithOffset} -geopos{decLong},{decLat} -hel -head"

    from subprocess import run

    outputString = run(commandString, capture_output=True).stdout # check the output from the terminal
    outputString2 = run(commandString2, capture_output=True).stdout # check the output from the terminal
    outputStringAmor = run(commandStringAmor, capture_output=True).stdout # check the output from the terminal
    outputStringAmor2 = run(commandStringAmor2, capture_output=True).stdout # check the output from the terminal
    outputStringEros = run(commandStringEros, capture_output=True).stdout # check the output from the terminal
    outputStringEros2 = run(commandStringEros2, capture_output=True).stdout # check the output from the terminal
    outputStringSappho = run(commandStringSappho, capture_output=True).stdout # check the output from the terminal
    outputStringSappho2 = run(commandStringSappho2, capture_output=True).stdout # check the output from the terminal
    outputStringLilith = run(commandStringLilith, capture_output=True).stdout # check the output from the terminal
    outputStringLilith2 = run(commandStringLilith2, capture_output=True).stdout # check the output from the terminal
    outputStringCeres = run(commandStringCeres, capture_output=True).stdout # check the output from the terminal
    outputStringCeres2 = run(commandStringCeres2, capture_output=True).stdout # check the output from the terminal
    outputStringSedna = run(commandStringSedna, capture_output=True).stdout # check the output from the terminal
    outputStringSedna2 = run(commandStringSedna2, capture_output=True).stdout # check the output from the terminal
    outputStringOdin = run(commandStringOdin, capture_output=True).stdout # check the output from the terminal
    outputStringOdin2 = run(commandStringOdin2, capture_output=True).stdout # check the output from the terminal
    outputStringMidas = run(commandStringMidas, capture_output=True).stdout # check the output from the terminal
    outputStringMidas2 = run(commandStringMidas2, capture_output=True).stdout # check the output from the terminal
    outputStringQuaoar = run(commandStringQuaoar, capture_output=True).stdout # check the output from the terminal
    outputStringQuaoar2 = run(commandStringQuaoar2, capture_output=True).stdout # check the output from the terminal
    outputStringErisUB313 = run(commandStringErisUB313, capture_output=True).stdout # check the output from the terminal
    outputStringErisUB313_2 = run(commandStringErisUB313_2, capture_output=True).stdout # check the output from the terminal
    outputStringHousesMidheaven = run(commandStringHousesMidheaven, capture_output=True).stdout # check the output from the terminal
    outputStringHousesNorthNode = run(commandStringNorthNode, capture_output=True).stdout # check the output from the terminal

    outputString = str(outputString)
    outputString2 = str(outputString2)
    outputStringAmor = str(outputStringAmor)
    outputStringAmor2 = str(outputStringAmor2)
    outputStringEros = str(outputStringEros)
    outputStringEros2 = str(outputStringEros2)
    outputStringSappho = str(outputStringSappho)
    outputStringSappho2 = str(outputStringSappho2)
    outputStringLilith = str(outputStringLilith)
    outputStringLilith2 = str(outputStringLilith2)
    outputStringHousesMidheaven = str(outputStringHousesMidheaven)
    outputStringNorthNode = str(outputStringHousesNorthNode)
    outputStringCeres = str(outputStringCeres)
    outputStringCeres2 = str(outputStringCeres2)
    outputStringSedna = str(outputStringSedna)
    outputStringSedna2 = str(outputStringSedna2)
    outputStringOdin = str(outputStringOdin)
    outputStringOdin2 = str(outputStringOdin2)
    outputStringMidas = str(outputStringMidas)
    outputStringMidas2 = str(outputStringMidas2)
    outputStringQuaoar = str(outputStringQuaoar)
    outputStringQuaoar2 = str(outputStringQuaoar2)
    outputStringErisUB313 = str(outputStringErisUB313)
    outputStringErisUB313_2 = str(outputStringErisUB313_2)

    #print(f"outputString: {outputString}")
    # OUTPUT
    """
    output: b"swetest -edirC:/Users/myvor/CLionProjects/C/sweph/ephe -b12.10.1981 -ut03:15:00 -p0123456789DH \r\ndate (dmy) 12.10.1981 greg.   3:15:00 UT\r\nUT: 2444889.635417     delta t: 51.996696 sec\r\nET: 2444889.636018\r\nEpsilon (true)    23\xf826'26.2881\r\nNutation          -0\xf8 0'16.4352   -0\xf8 0' 3.6521\r\nSun              198\xf842'35.1705   -0\xf8 0' 0.5604    0.997879537    0\xf859'21.2200\r\nMoon             359\xf832'20.9797   -4\xf824'11.1086    0.002457284   14\xf827' 2.0896\r\nMercury          211\xf843'24.6100   -3\xf8 0'48.6214    0.690352846   -0\xf845'32.8984\r\nVenus            243\xf831'36.0328   -2\xf827' 0.5427    0.893457292    1\xf8 7'19.6810\r\nMars             144\xf843' 0.6793    1\xf822'12.0920    1.997036242    0\xf835'44.9328\r\nJupiter          200\xf818'14.7195    1\xf8 5' 9.5108    6.449366556    0\xf813' 1.2536\r\nSaturn           193\xf833'52.2356    2\xf812'56.6926   10.608263792    0\xf8 7'20.9364\r\nUranus           237\xf857'37.7456    0\xf810'51.1594   19.601584560    0\xf8 3' 4.2854\r\nNeptune          262\xf829'26.2062    1\xf817' 9.7365   30.702518823    0\xf8 1'13.5387\r\nPluto            204\xf8 2'45.9135   16\xf833'12.3151   30.969089383    0\xf8 2'23.6461\r\nChiron            51\xf853' 8.2355   -2\xf836'22.3492   15.490018255   -0\xf8 2'26.0047\r\nJuno             226\xf840'20.8158    9\xf824'17.9336    4.188035096    0\xf819'24.0954\r\n"
    """
    # array
    lines = outputString.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").split("\\r\\n")
    lines2 = outputString2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").split("\\r\\n")
    #-----------
    # string
    lineAmor = outputStringAmor.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineAmor2 = outputStringAmor2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineEros = outputStringEros.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineEros2 = outputStringEros2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineSappho = outputStringSappho.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineSappho2 = outputStringSappho2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineLilith = outputStringLilith.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineLilith2 = outputStringLilith2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    # ---Financial Astroids---
    lineCeres = outputStringCeres.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineCeres2 = outputStringCeres2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineSedna = outputStringSedna.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineSedna2 = outputStringSedna2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineOdin = outputStringOdin.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineOdin2 = outputStringOdin2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineMidas = outputStringMidas.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineMidas2 = outputStringMidas2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineQuaoar = outputStringQuaoar.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineQuaoar2 = outputStringQuaoar2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineErisUB313 = outputStringErisUB313.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    lineErisUB313_2 = outputStringErisUB313_2.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    #--------------------------
    lineNorthNode = outputStringNorthNode.replace("\'","'").replace("         ","   ").replace("      ","   ").replace("     ","   ").replace("    ","   ").replace("\\xf8","/").replace("\\r\\n","")
    #----------------
    # --------------------------------------------
    # print(f"lines ({len(lines)}):\n")
    linesHousesMidheaven = outputStringHousesMidheaven.replace("\'", "'").replace("         ", "   ").replace("      ", "   ").replace("     ", "   ").replace("    ", "   ").replace("\\xf8", "/").split("\\r\\n")
    # print(f"linesHousesMidheaven ({len(linesHousesMidheaven)}):\n") # got it right now
    # f.print2(linesHousesMidheaven)
    h2 = linesHousesMidheaven[9]  # "house 10   153-57'18.8832"
    h3 = h2.split("   ")
    deg360 = h3[1].split("-")[0]
    lineMidheaven = f"Midheaven: {deg360}" # it's added later
    # f.print2(lineMidheaven)
    #----------------------------

    #--------------------
    # import FUNCTIONS as f
    # f.print2(lines)
    # --------------------------------------------

    planets = []
    c = 0
    if len(lines) > 1:  # last line is nothing
        for line in lines:
            if len(line) > 1:  # last line is nothing
                # print(f"{c}) line: {len(line)}: {line}")
                l = line.split("  ")
                # clean whitespace for each
                planetName = l[0].strip().strip('b"') + "_g"
                degrees = aa.parseDegreesSweToDecimal(l[1].strip())  # in degrees # '-2/28'19.1097'
                declination = aa.parseDegreesSweToDecimal(l[2].strip())  # in degrees
                distance = f.round_down4(float(l[3].strip()))  # in Decimal - round down
                speed = aa.parseDegreesSweToDecimal(l[4].strip())  # in parseDegreesSweToDecimal()
                if speed < 0:  # it's negative
                    Rx = "Rx"
                else:
                    Rx = "Rx0"
                # Rx = pos or neg - from speed
                #print(f"{c}) planetName: '{planetName}', degrees: '{degrees}', declination: '{declination}', distance: '{distance}', speed: '{speed}', Rx: {Rx}")
                string = f'{planetName}: {degrees}/{Rx}/{declination}/{distance}/{speed}'
                #print(f"     {string}")
                planets.append(string)

                c += 1

                #-------------------------
                # NORTHNODE - set up here ... SOUTHNODE - setup below
                #------------------------
                #degreesNorthNode = 0
                #if planetName=="mean Node":
                    #planets.append(f"NorthNode: {degrees}{Rx}")
                    #degreesNorthNode = degrees
                # -------------------------
                # ALL OTHERS - set up here
                # ------------------------
                #else:
                    #planets.append(string)

    #print(f"planets ({len(planets)}):\n")
    #f.print2(planets)
    #WORKING ON Getting the Helio Chart - as appended '2's to the names, except Earth
    #print(f"lines2 ({len(lines2)}):")
    #f.print2(lines2)
    #print(f"lines2 ({len(lines2)})")

    #print("exiting")
    #exit()
    c = 0
    if len(lines2)>10:
        for line in lines2:
            if len(line)>2: #last line is nothing
                #print(f"{c}) line: {len(line)}: {line}")
                # ------------------
                l = str(line)

                string = ""
                string = aa.makePlanetStringSwe2(l,"h") #h for helio, g for geo

                #------------------
                #print(f"string: {string}")
                if f.isString(string): #if it's a string
                    #print(string)
                    #print("exiting 5")
                    #exit()
                    if "Moon" not in string: # in helio: Moon is too close to Earth - never save it
                        planets.append(string)
                c += 1



    #---------------------------------
    #GET Rx FOR ALL OF THESE AS WELL:
    # ---------------------------------

    #----------------------
    #finish adding AMOR:
    string = aa.makePlanetStringSwe2(lineAmor,"g") #h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineAmor2,"h") #h for helio, g for geo
    planets.append(string)

    # ----------------------
    # finish adding EROS:
    string = aa.makePlanetStringSwe2(lineEros, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineEros2,"h") #h for helio, g for geo
    planets.append(string)
    # ----------------------
    # finish adding SAPPHO:
    string = aa.makePlanetStringSwe2(lineSappho, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineSappho2,"h") #h for helio, g for geo
    planets.append(string)

    # ----------------------
    # finish adding LILITH:
    string = aa.makePlanetStringSwe2(lineLilith, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineLilith2,"h") #h for helio, g for geo
    planets.append(string)
    # ----------------------
    # finish adding CERES: # 2 degrees different!! FIX IT
    #string = aa.makePlanetStringSwe2(lineCeres, "g")  # h for helio, g for geo
    #planets.append(string)
    string = aa.makePlanetStringSwe2(lineCeres2,"h") #h for helio, g for geo
    planets.append(string)


    # ----------------------
    # finish adding SEDNA:
    string = aa.makePlanetStringSwe2(lineSedna, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineSedna2,"h") #h for helio, g for geo
    planets.append(string)

    # Odin (3989), Midas (1981), Quaoar (50000), Eris/UB313 (136199)

    # ----------------------
    # finish adding ODIN:
    string = aa.makePlanetStringSwe2(lineOdin, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineOdin2,"h") #h for helio, g for geo
    planets.append(string)

    # ----------------------
    # finish adding MIDAS:
    string = aa.makePlanetStringSwe2(lineMidas, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineMidas2,"h") #h for helio, g for geo
    planets.append(string)

    # ----------------------
    # finish adding QUAOAR:
    string = aa.makePlanetStringSwe2(lineQuaoar, "g")  # h for helio, g for geo
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineQuaoar2,"h") #h for helio, g for geo
    planets.append(string)

    # ---------------------- #Eris/UB313
    # finish adding ERISUB313:ErisUB313
    string = aa.makePlanetStringSwe2(lineErisUB313, "g")  # h for helio, g for geo
    string = string.replace("Eris","ErisUB313")
    planets.append(string)
    string = aa.makePlanetStringSwe2(lineErisUB313_2,"h") #h for helio, g for geo
    string = string.replace("Eris","ErisUB313")
    planets.append(string)

    # Finish adding MIDHEAVEN
    #print(f"lineMidheaven: {lineMidheaven}")

    decimal = aa.parseDegreesSweToDecimal(lineMidheaven.split(": ")[1].strip())
    string_lineMidheaven = f"Midheaven_g: {decimal}"
    planets.append(string_lineMidheaven) #"Midheaven: 340/ 4'15.6831" - convert to - working here

    # -------- Add SaturnChironMidpoint ----------
    chiron = ""
    saturn = ""
    meanNode = ""
    #print(f"planets ({len(planets)})")
    #print("exiting 2.1")
    #exit()
    #print("Not NoneType")
    if len(planets)>1:
        #print("exiting 1")
        #exit()
        for planetSignDeg in planets: #been appending to planets this whole time
            if "Saturn" in str(planetSignDeg):
                saturn = planetSignDeg
            if "Chiron" in str(planetSignDeg):
                chiron = planetSignDeg
            if "mean Node" in str(planetSignDeg):
                meanNode = planetSignDeg

    # print(f"{saturn} ... {chiron} ... midpoint?")
    #print(f"saturn (get full decimal): {saturn}")
    #print(f"chiron (get full decimal): {chiron}")
    degS = float(saturn.split(": ")[1].split("/")[0])
    degC = float(chiron.split(": ")[1].split("/")[0])
    #print(f"saturn: {degS} / chiron {degC}")
    # -------------
    midNum = aa.midpointFrom2_360s(degS, degC)
    saturnchironmidpoint = f"SaturnChironMidpoint_g: {midNum}"
    # print(f"planetSignDegree: {planetSignDegree}")
    planets.append(saturnchironmidpoint)
    # -------- Add SaturnChironMidpoint ----------
    # do the same thing with Saturn, and chiron, for the mean Node,to NorthNode, and calc South Node
    nn1 = meanNode.split(": ")
    n1 = nn1[1].split("/")
    deg = n1[0]
    northNode = float(deg)
    southNode = northNode + 180
    if southNode>360:
        southNode = southNode - 360
    #planets.append(f"mean Node: {northNode}/{n1[1]}/{n1[2]}/{n1[3]}/{n1[4]}")
    planets.append(f"NorthNode_g: {northNode}/{n1[1]}/{n1[2]}/{n1[3]}/{n1[4]}")
    planets.append(f"SouthNode_g: {southNode}")

    #print("looking for NorthNode_g in here:")
    #print(f"planets: {len(planets)}")
    #f.print2(planets)
    #print("looking for NorthNode_g in here:")

    return planets



#-------------------------------

# dict[planets]=>[degrees]
# import ASTROLOGYfunctions as aa
# planetsDict = aa.p360planetsToDict(planets360_P1)
def p360planetsToDict(planets360_P1):
    #print("the problem is in this function ... p360planetsToDict(planets360_P1)")
    #print("p360planetsToDict(planets360_P1) ...")
    planets_dict = {}
    import FUNCTIONS as f
    dict = {}
    c=0
    for planetSignDegreeString in planets360_P1:
        p = planetSignDegreeString.split(":")
        if len(p)>1:
            #print(f"{c}) p: {p}")
            planetName = str(f.strip1(p[0]))
            degreesRx = f.strip1(p[1])
            dict[planetName] = degreesRx

            c += 1
    #print(f"dict: {dict}")
    #print(f"dict['Sun']: {dict['Sun']}")
    return dict
    #exit() #focus on this function - so stop everything else


#new_dic = {}
#new_dic[1] = {}
#new_dic[1][2] = 5

#need dict from planetName to the 360deg - just that in the array

"""
TEST LINKAGES
take out 2 from that function

only process 1 person - planets left - 1person planets right - per that function
"""
# import ASTROLOGYfunctions as aa
# linkageStatus = aa.testLinkage(planetName1,deg1,angle,planetName2, deg2)
def testLinkage(planetName1="Saturn", deg1=243, angle="Trine", planetName2="Chiron", deg2=60):
    #print("Testing For a Linkage - Person1-left--Person2-right:")
    import FUNCTIONS as f
    import ASTROLOGYmagi as m
    Rx1 = ""
    if " Rx" in str(deg1):
        deg1 = float(str(deg1).strip(" Rx"))
        Rx1 = " Rx"
    Rx2 = ""
    if " Rx" in str(deg2):
        deg2 = float(str(deg2).strip(" Rx"))
        Rx2 = " Rx"

    #if linkage is found - times power values by - planet power/orb
    # times the power by the power of the planet's power and orb
    # m.set_savedPowerValues['initial_chemistry']['power']['Luck'] += float(power)
    # planets_organized["Sun"]["planet_orb"], planets_organized["Sun"]["power"]
    #
    orbPlanetDegrees1 = m.planets_organized[planetName1]["planet_orb"]
    powerPlanet1 = m.planets_organized[planetName1]["power"]
    orbPlanetDegrees2 = m.planets_organized[planetName2]["planet_orb"]
    powerPlanet2 = m.planets_organized[planetName2]["power"]

    angleDegrees = int(m.aspects_organized[angle]['degrees'])
    orbDegrees = int(m.aspects_organized[angle]['meaningful_orb'])
    power = int(m.aspects_organized[angle]['power'])
    #print(f"{planetName1}: {deg1} - angle: {angle} - degrees: {angleDegrees}, orb: {orbDegrees}, power: {power} ... {planetName2}: {deg2}")
    angleDiff = 0
    # --------------------------------------
    # this is to decide which number is larger - so I can subtract one from the other
    # to get the angle difference (angleDiff)
    if float(deg1)>float(deg2):
        angleDiff = float(deg1)-float(deg2)
        #print(f"angleDiff ({angleDiff}) = deg1({deg1})-deg2({deg2})")
    elif float(deg1)==float(deg2):
        angleDiff = 0
    elif float(deg2)>float(deg1):
        angleDiff = float(deg2)-float(deg1)
        #print(f"deg2({deg2})-deg1({deg1}) = angleDiff ({angleDiff})")
    #--------------------------------------
    #print(f"angleDiff: {angleDiff} ... {angle}: {angleDegrees}")
    #print(f"is angleDiff ({angleDiff}) less than the orb ({orbDegrees}) - within the orb ??")
    power1 = 0
    if angleDiff<orbDegrees: #if it's within the orb
        power1 = orbDegrees - angleDiff / orbDegrees * power
        power2 = orbPlanetDegrees1 - angleDiff / orbPlanetDegrees1 * powerPlanet1
        power3 = orbPlanetDegrees2 - angleDiff / orbPlanetDegrees2 * powerPlanet2
        powerTotal = float(f.round_down2(power1 * power2 * power3))
        return powerTotal

        #the closer to the match - the smallest orb - gets a higher slice of power
        #total power - is max points to give
        #how close to an exact match - 0 degrees
        # and then - if it is exactly at the max of the orb - it still barely counts
        #angleDiff=5, orb=10, power=15 ... 5/10*15 - 50% of 15
        #angleDiff=9, orb=10, power=15 ... 1/10*15 - only gets 10% of the power - it's down to the last degree of the orb
        #angleDiff=2, orb=10, power=15 ... o10-2d|(8)/10*15 - almost exact 0 angleDiff
        #angleDiff=2, orb=6.5, power=15 ... o6.5-2d|(4.5)/6.5o*15 (10.4 out of 15 power)
        # ... it's only costs about 1/3 of the orb - so it gets a comission of 2/3 of the power
    if angleDiff==orbDegrees: #if it's within the orb
        power1 = 1 / orbDegrees * power #it's still there, but it's the last bit of power
        power2 = orbPlanetDegrees1 - angleDiff / orbPlanetDegrees1 * powerPlanet1
        power3 = orbPlanetDegrees2 - angleDiff / orbPlanetDegrees2 * powerPlanet2
        powerTotal = float(f.round_down2(power1 * power2 * power3))
        return powerTotal
    if angleDiff>orbDegrees:
        power1 = 0
        #it's outside of the orb - not a match
        #calculate power, and return it
        return power1 # = 0
    #exit()


#--------------------------------------


#import ASTROLOGYfunctions as aa
#justThePlanet = aa.keepBeforeLineChar(string="Pluto|genders:manwoman")
#print(f"justThePlanet: {justThePlanet}")
def keepBeforeLineChar(string):
    print(f"deleteAfterLine (|): {string}")
    s = string.split("|")
    print(f"s: {s}")
    justThePlanet = s[0]
    return justThePlanet



# import ASTROLOGYfunctions as aa
# savePower(categoryTitle="Long title (Luck)", power=5)
def savePower(categoryTitle="Long title (Luck)", power=5, infoPack={}):
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    # times the power by the power of the planet's power and orb
    # m.set_savedPowerValues['initial_chemistry']['power']['Luck'] += float(power)

    P1name = infoPack["P1name"]
    P1gender = infoPack["P1gender"]
    justThePlanet1 = infoPack["justThePlanet1"]
    Planet1degrees = infoPack["Planet1degrees"]
    P2name = infoPack["P2name"]
    P2gender = infoPack["P2gender"]
    justThePlanet2 = infoPack["justThePlanet2"]
    Planet2degrees = infoPack["Planet2degrees"]
    angleName = infoPack["angleName"]
    angleDifference = infoPack["angleDifference"]

    #print(f"infoPack-sv ({len(infoPack)}): {infoPack}")

    orbPlanetDegrees1 = m.planets_organized[justThePlanet1]["planet_orb"]
    powerPlanet1 = m.planets_organized[justThePlanet1]["power"]
    orbPlanetDegrees2 = m.planets_organized[justThePlanet2]["planet_orb"]
    powerPlanet2 = m.planets_organized[justThePlanet2]["power"]

    power2 = f.round_down2((orbPlanetDegrees1 - angleDifference) / orbPlanetDegrees1 * powerPlanet1)
    power3 = f.round_down2((orbPlanetDegrees2 - angleDifference) / orbPlanetDegrees2 * powerPlanet2)
    print(f"power {power} ... power2: {power2} ... power3: {power3}")

    saveLinkage(categoryTitle=categoryTitle, power=power, infoPack=infoPack)
    import ASTROLOGYmagi as m
    if "Luck" in categoryTitle:
        m.set_savedPowerValues['initial_chemistry']['power']['Luck'] += float(power*power2*power3)
    if "Love" in categoryTitle:
        m.set_savedPowerValues['initial_chemistry']['power']['Love'] += float(power)
    if "Sex" in categoryTitle:
        m.set_savedPowerValues['initial_chemistry']['power']['Sex'] += float(power)
    if "Drama" in categoryTitle:
        m.set_savedPowerValues['initial_chemistry']['power']['Drama'] += float(power)


# import ASTROLOGYfunctions as aa
# saveLinkage(categoryTitle="Long title (Luck)", power=5)
#returns the total power it found
def saveLinkage(categoryTitle="Long title (Luck)", power=5, infoPack={}):

    print(f"infoPack-sl ({len(infoPack)}): {infoPack}")

    P1name = infoPack["P1name"]
    P1gender = infoPack["P1gender"]
    justThePlanet1 = infoPack["justThePlanet1"]
    Planet1degrees = infoPack["Planet1degrees"]
    P2name = infoPack["P2name"]
    P2gender = infoPack["P2gender"]
    justThePlanet2 = infoPack["justThePlanet2"]
    Planet2degrees = infoPack["Planet2degrees"]
    angleName = infoPack["angleName"]
    angleDifference = infoPack["angleDifference"]

    # P1name = "Michael"
    # P1planet = "Chiron"
    # P1gender = "man"
    # P2name = "Miriam"
    # P2planet = "Venus"
    # P2gender = "woman"
    #THIS FORMAT: ... ' - Uranus (Miriam) - Chiron (Michael)' #at the end
    officialAngleName = f"{justThePlanet1}-{angleName}-{justThePlanet2}"
    whosePlanets = str(f"{justThePlanet1}: {Planet1degrees} ({P1name}) - {justThePlanet2}: {Planet2degrees} ({P2name}) ... angleDifference: ({angleDifference}) ... officialAngleName: ({officialAngleName})")
    #---
    #adding authorship - who gets credit for the linkage - whose planet to whose planet - with names
    #-----------------
    #put these as text
    import ASTROLOGYmagi as m
    if "Luck" in categoryTitle: #string
        append1 = {categoryTitle: {"power": power, "whosePlanets": whosePlanets} }
        dict = m.set_savedLinkages['initial_chemistry']['linkages']['Luck']
        dict.update(append1) # update is append for dicts
        m.set_savedLinkages['initial_chemistry']['linkages']['Luck'] = dict
    if "Love" in categoryTitle:
        append1 = {categoryTitle: {"power": power, "whosePlanets": whosePlanets} }
        dict = m.set_savedLinkages['initial_chemistry']['linkages']['Love']
        dict.update(append1)
        m.set_savedLinkages['initial_chemistry']['linkages']['Love'] = dict
    if "Sex" in categoryTitle:
        append1 = {categoryTitle: {"power": power, "whosePlanets": whosePlanets} }
        dict = m.set_savedLinkages['initial_chemistry']['linkages']['Sex']
        dict.update(append1)
        m.set_savedLinkages['initial_chemistry']['linkages']['Sex'] = dict
    if "Drama" in categoryTitle:
        append1 = {categoryTitle: {"power": power, "whosePlanets": whosePlanets} }
        dict = m.set_savedLinkages['initial_chemistry']['linkages']['Drama']
        dict.update(append1)
        m.set_savedLinkages['initial_chemistry']['linkages']['Drama'] = dict




#need: angleDifference here # 2 360's - find out which is bigger 1st
def angleDifference2_360s(n1=100.123,n2=200.123):
    n1 = float(n1)
    n2 = float(n2)

    if n1>n2:
        return n1-n2
    if n1 == n2:
        return 0
    if n2>n1:
        return n2-n1




# import ASTROLOGYfunctions as aa
# aa.loopingThruTheLinkages4()

# it lists all of the Aspects that have to do with a planet name
def loopingThruTheLinkages4(planet="Pluto"):
    import ASTROLOGYmagi as m
    import ASTROLOGYfunctions as aa
    # loop through these - I had it before:
    # 'Jupiter-Conjunct-Vesta'
    #----------------------------------------
    #
    # PERSON 1:
    P1name = "Michael"
    P1planet = ""
    P1gender = "man"
    planets360_P1 = aa.cache1Birthchart(y=1981, m=10, d=12, h=3, m1=6, timezone=-5, city="Kansas City, MO")

    # need dict from planetName to the 360deg - just that in the array
    P1_planets = p360planetsToDict(planets360_P1) #Dict
    #print(f"planets360_P1 ({len(planets360_P1)}): {planets360_P1}")

    #----------------------------------------
    specialAspects = m.specialAspects
    aspects_organized = m.aspects_organized
    c = 0
    planet = "Sun" #Venus
    for linkageTitleString in specialAspects["self"]: # self, synastry
        #print("")
        linkageGroups = specialAspects["self"][linkageTitleString]
        #print(f"linkageGroups: {linkageGroups}")
        for linkage3name in linkageGroups:
            # if it has the planet at the beginning or end of the linkage3name,
            if f"{planet}-" in linkage3name or f"-{planet}" in linkage3name:
                print(f"\n{c}) [title]: {linkageTitleString}")
                # the linkage - with 3 parts to it: like: Venus-Conjunct-Mars
                print(f"linkage3name: {linkage3name}")
                c += 1
        #print(f"{c})")

    print("")
    print("That's all")



# import ASTROLOGYfunctions as aa
# totalLinkagesForPlanet, rows = aa.linkagesByPlanet(planet="Sun")

# it lists all of the Aspects that have to do with a planet name
def linkagesByPlanet(planet="Sun"):
    import ASTROLOGYmagi as m
    import ASTROLOGYfunctions as aa
    # loop through these - I had it before:
    # 'Jupiter-Conjunct-Vesta'
    #----------------------------------------

    # P1name,P1planet,P1gender,P2name,P2planet,P2gender - set the planet
    #
    # PERSON 1:
    P1name = "Michael"
    P1planet = ""
    P1gender = "man"
    planets360_P1 = aa.cache1Birthchart(y=1981, m=10, d=12, h=3, m1=6, timezone=-5, city="Kansas City, MO")

    # need dict from planetName to the 360deg - just that in the array
    P1_planets = p360planetsToDict(planets360_P1) #Dict
    #print(f"planets360_P1 ({len(planets360_P1)}): {planets360_P1}")

    #----------------------------------------
    import FUNCTIONS as f
    specialAspects = m.specialAspects
    #print("specialAspects: ")
    #f.print2(specialAspects)

    aspects_organized = m.aspects_organized
    # print("aspects_organized: ")
    # f.print2(aspects_organized)

    # planets_organized = m.planets_organized
    # print("planets_organized: ")
    # f.print2(planets_organized)

    # print(f"specialAspects: {specialAspects}") #long list 44 sets of linkages
    # print("")

    # loop through them one by one
    # see if it matches the 2 comparing birthcharts we are using
    # first person is 1stPlanet To the planet of 2nd person
    # 'Sun-Trine-Neptune' <-- Sun is 1st perons's Sun <-- Neptune is 2nd person's Neptune
    # and it makes a Trine angle - with the plus or minus - I think orb where it counts
    c = 0
    rows = {}
    planet = planet # "Venus" #Sun
    for linkageTitleString in specialAspects["self"]: # self, synastry
        #print("")
        linkageGroups = specialAspects["self"][linkageTitleString]
        #print(f"linkageGroups: {linkageGroups}")
        for linkage3name in linkageGroups:
            # if it has the planet at the beginning or end of the linkage3name,
            if f"{planet}-" in linkage3name or f"-{planet}" in linkage3name:
                # the linkage - with 3 parts to it: like: Venus-Conjunct-Mars
                print(f"\n{c}) linkage3name: {linkage3name}")
                print(f"[title]: {linkageTitleString}")
                rows[linkage3name] = linkageTitleString
                c += 1
        #print(f"{c})")

    #print("")
    #print("That's all")
    totalLinkagesForPlanet = c
    return totalLinkagesForPlanet, rows #how many linkages it found for that planet




# import ASTROLOGYfunctions as aa
# aa.loopingThruTheLinkages2()
# required to be run 2 times - to catch the other person's planets as person 1
def loopingThruTheLinkages2():
    import ASTROLOGYmagi as m
    import ASTROLOGYfunctions as aa
    # loop through these - I had it before:
    # 'Jupiter-Conjunct-Vesta'
    #----------------------------------------

    # P1name,P1planet,P1gender,P2name,P2planet,P2gender - set the planet
    #
    # PERSON 1:
    P1name = "Michael"
    P1planet = ""
    P1gender = "man"
    planets360_P1 = aa.cache1Birthchart(y=1981, m=10, d=12, h=3, m1=6, timezone=-5, city="Kansas City, MO")

    # need dict from planetName to the 360deg - just that in the array
    P1_planets = p360planetsToDict(planets360_P1) #Dict
    #print(f"planets360_P1 ({len(planets360_P1)}): {planets360_P1}")
    #
    # PERSON 2:
    P2name = "Miriam"
    P2planet = ""
    P2gender = "woman"
    planets360_P2 = aa.cache1Birthchart(y=1984, m=4, d=18, h=12, m1=0, timezone=-5, city="Mexico City, Mexico")
    # need dict
    P2_planets = aa.p360planetsToDict(planets360_P2) #Dict
    #print(f"planets360_P2 ({len(planets360_P2)}): {planets360_P2}")

    #----------------------------------------
    import FUNCTIONS as f
    specialAspects = m.magiAspects()
    #print("specialAspects: ")
    #f.print2(specialAspects)

    aspects_organized = m.magiAspects2()
    # print("aspects_organized: ")
    # f.print2(aspects_organized)

    # planets_organized = a.magiAspects3()
    # print("planets_organized: ")
    # f.print2(planets_organized)

    # print(f"specialAspects: {specialAspects}") #long list 44 sets of linkages
    # print("")

    # loop through them one by one
    # see if it matches the 2 comparing birthcharts we are using
    # first person is 1stPlanet To the planet of 2nd person
    # 'Sun-Trine-Neptune' <-- Sun is 1st perons's Sun <-- Neptune is 2nd person's Neptune
    # and it makes a Trine angle - with the plus or minus - I think orb where it counts
    c = 0
    for aspectTitle in specialAspects:
        if aspectTitle == "synastry":  # synastry, self - the 2 parts of the array
            print(f"\n{c}) aspect title: {aspectTitle}")
            # 0) aspect title: self ... 44 planetToPlanet aspects
            # 1) aspect title: synastry ... 71 planetToPlanet aspects
            planetToPlanets = specialAspects[aspectTitle]

            #print(f" ... planetToPlanet {len(planetToPlanets)} aspects: {planetToPlanets}")
            #f.print2(planetToPlanets)
            # "Chiron-Opposed-Amor"
            c2 = 0
            for planetAspect in planetToPlanets:
                categoryTitle = planetAspect # has 1+ of the 4: Luck, Love, Sex, Drama
                print(f"planetAspect: {planetAspect}")
                linkages = planetToPlanets[planetAspect]
                #print(f"linkages: {linkages}")
                #f.print2(planetAspect)
                c3 = 0
                for linkage in linkages:
                    nameOfLinkage = linkage
                    #print(f"single linkage 1 ... {linkage}") # Saturn-Quincunx-Neptune
                    p = linkage.split("-")
                    #1st Planet in the linkage check
                    planetName1 = p[0]
                    angle = p[1]  # you take this as a template and compare those from both birthcharts
                    # 2nd Planet in the linkage check
                    planetName2 = p[2]
                    if len(aspects_organized[angle]) >= 1:  # gets rid of last row error

                        justThePlanet1 = aa.keepBeforeLineChar(planetName1)
                        justThePlanet2 = aa.keepBeforeLineChar(planetName2)

                        #make sure planetName1 & 2 - don't have |genders on it
                        # deg1_2 = P1_planets['Pluto|genders:manwoman']
                        #deg1 is the 1st degree for person 1, for Planet1
                        deg1 = P1_planets[justThePlanet1] # need dict from planetName to the 360deg - just that in the array
                        #deg1_2 is the 2nd degree for person 1, for Planet2
                        deg1_2 = P1_planets[justThePlanet2] # 111 # planets360_P1[planetName1] # need dict from planetName to the 360deg - just that in the array
                        #if it has more qualifications, like this has gender:manwoman ,on Pluto
                        #IF IT HAS A QUALFIER - ON THE MATCH - a '|'
                        #do this for now

                        #deg2 is the 1st degree for person 2, for Planet2
                        deg2 = P2_planets[justThePlanet2]
                        deg2_2 = P2_planets[justThePlanet1]
                        #print(f"deg1, deg1_2, deg2, deg2_2: {deg1}, {deg1_2}, {deg2}, {deg2_2}")
                        print( f"{c}:{c2}:{c3}) single linkage: ... {planetName1} {deg1} (of person 1) ... angle: {angle} - degrees: {aspects_organized[angle]['degrees']}, orb: {aspects_organized[angle]['meaningful_orb']}, power: {aspects_organized[angle]['power']} ... {planetName2} ({deg2}) (of person 2)")

                        # test the linkage to see if we have a match
                        print("looking up person 1 first - person 2 second")
                        linkageStatus = testLinkage(justThePlanet1,deg1,angle,justThePlanet2, deg2)#good

                        # 0 power - not a match
                        if linkageStatus!=0:
                            print(f"categoryTitle = {categoryTitle}")  # has 1+ of the 4: Luck, Love, Sex, Drama"
                            angleDifference = angleDifference2_360s(deg1,deg2)
                            infoPack = {"P1name": P1name, "P1gender": P1gender, "justThePlanet1": justThePlanet1,
                                        'Planet1degrees': deg1, "P2name":P2name, "P2gender": P2gender,
                                        "justThePlanet2": justThePlanet2, 'Planet2degrees': deg2,
                                        'angleName': angle, 'angleDifference': angleDifference}
                            aa.savePower(categoryTitle, linkageStatus, infoPack) #linkageStatus is power
                            #------------------------------

                        #exit()
                    c3 += 1
                c2 += 1
        # loop through these - I had it before:
        # 'Jupiter-Conjunct-Vesta'
        c += 1
    view = m.set_savedPowerValues['initial_chemistry']
    viewMore = m.set_savedLinkages['initial_chemistry']
    print(f"view ('initial_chemistry'):")
    # multipliers used in PHP? - for the 4 categories- to compensate for not having as many aspects - for the 3 good categories
    # multiply before viewing:
    f.print2(view)
    f.print2(viewMore)




#------------------------------


# import ASTROLOGYfunctions as aa
# aa.loopingThruTheLinkages1()
def loopingThruTheLinkages1():
    # loop through these - I had it before:
    # 'Jupiter-Conjunct-Vesta'

    import ASTROLOGYmagi as a

    import FUNCTIONS as f
    specialAspects = a.magiAspects()
    #print("specialAspects: ")
    #f.print2(specialAspects)

    aspects_organized = a.magiAspects2()
    # print("aspects_organized: ")
    # f.print2(aspects_organized)

    # planets_organized = a.magiAspects3()
    # print("planets_organized: ")
    # f.print2(planets_organized)

    # print(f"specialAspects: {specialAspects}") #long list 44 sets of linkages
    # print("")

    # loop through them one by one
    # see if it matches the 2 comparing birthcharts we are using
    # first person is 1stPlanet To the planet of 2nd person
    # 'Sun-Trine-Neptune' <-- Sun is 1st perons's Sun <-- Neptune is 2nd person's Neptune
    # and it makes a Trine angle - with the plus or minus - I think orb where it counts
    c = 0
    for aspectTitle in specialAspects:
        if aspectTitle == "synastry":  # synastry, self - the 2 parts of the array
            print(f"\n{c}) aspect title: {aspectTitle}")
            # 0) aspect title: self ... 44 planetToPlanet aspects
            # 1) aspect title: synastry ... 71 planetToPlanet aspects
            planetToPlanets = specialAspects[aspectTitle]

            #print(f" ... planetToPlanet {len(planetToPlanets)} aspects: {planetToPlanets}")
            #f.print2(planetToPlanets)
            # "Chiron-Opposed-Amor"
            c2 = 0
            for planetAspect in planetToPlanets:
                linkages = planetToPlanets[planetAspect]
                #print(f"linkages: {linkages}")
                #print(f"planetAspect: {planetAspect}")
                #f.print2(planetAspect)
                c3 = 0
                for linkage in linkages:
                    # print(f"single linkage ... {linkage}")
                    p = linkage.split("-")
                    planetName1 = p[0]
                    angle = p[1]  # you take this as a template and compare those from both birthcharts
                    planetName2 = p[2]

                    if len(aspects_organized[angle]) >= 1:  # gets rid of last row error
                        print(f"{c}:{c2}:{c3}) single linkage ({planetName1}-{angle}-{planetName2}): ... {planetName1} (of person 1) ... angle: {angle} - degrees: {aspects_organized[angle]['degrees']}, orb: {aspects_organized[angle]['meaningful_orb']}, power: {aspects_organized[angle]['power']} ... {planetName2}  (of person 2)")
                    c3 += 1
                c2 += 1
        # loop through these - I had it before:
        # 'Jupiter-Conjunct-Vesta'
        c += 1

    # spit out - this seperated on a line - Chiron-Opposed-Amor...
    # now I need to add in both people's birthcharts - and use this on p1-guy to p2-girl




#------------------------------



# import ASTROLOGYfunctions as aa
# aa.PowerNumberFinalGrade(): # not done # savingSettingPowerNumber
def PowerNumberFinalGrade(): #practice
    #SET OF POWER - for each chart
    #set of charts?
    #set of variables - for this set of charts/midpoints
    # ONE BIG SET - 6 times we do MagiAspect Scans - for matches--saving power values
    # set_savedPowerValues['initial_chemistry']['power']
    import ASTROLOGYmagi as m
    powers = m.set_savedPowerValues
    print(f"powers: {powers}")

    #access the current power value of Luck
    luck1 = m.set_savedPowerValues['initial_chemistry']['power']["Luck"]
    print(f"luck1: {luck1}")
    #test saving a power value of 10 to Luck
    m.set_savedPowerValues['initial_chemistry']['power']["Luck"]+=11
    m.set_savedPowerValues['initial_chemistry']['power']["Luck"]-=1
    luck1 = m.set_savedPowerValues['initial_chemistry']['power']["Luck"]
    print(f"luck1: {luck1}")
    #test setting the final grade
    m.set_savedPowerValues['initial_chemistry']["finalGrade"] += 5
    m.set_savedPowerValues['initial_chemistry']["finalGrade"] -= 1
    #test getting the final grade value
    finalGrade = m.set_savedPowerValues['initial_chemistry']["finalGrade"]
    print(f"finalGrade: {finalGrade}")
    m.set_savedPowerValues['combinedFinalGrade'] +=3
    combinedFinalGrade = m.set_savedPowerValues['combinedFinalGrade']
    print(f"combinedFinalGrade: {combinedFinalGrade}")


#------------------------


# import ASTROLOGYfunctions as aa
# aa.oneSETofData_2people()
def oneSETofData_2people():
    import ASTROLOGYfunctions as aa

    me = aa.me()
    person = aa.person2()

    # ------------------------
    info1 = me['info']
    info2 = person['info']
    #------------------------
    # person 1
    name1 = info1['name']
    datetime1 = info1['datetime']
    city1 = info1['city']
    timezone1 = info1['timezone']
    timeknown1 = info1['timeknown'] # time_given, time_not_given
    planets360_P1 = me['planets']['360']
    # person 2
    name2 = info2['name']
    datetime2 = info2['datetime']
    city2 = info2['city']
    timezone2 = info2['timezone']
    timeknown2 = info2['timeknown'] # time_given, time_not_given
    planets360_P2 = person['planets']['360']
    # add in 2 people birthcharts - for it to check if it matches any
    #
    # PERSON 1:# planets = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, city=city)
    print(f"info1 ({len(info1)}): {info1}")
    print(f"planets360_P1 ({len(planets360_P1)}): {planets360_P1}")
    #
    # PERSON 2:
    print(f"info2 ({len(info2)}): {info2}")
    print(f"planets360_P2 ({len(planets360_P2)}): {planets360_P2}")

    # LAYER 1
    # the initial chemistry ... the way you feel when you first see or meet them
    # 1st P - left side ... 2nd P - right side ... genders, retrograde

    # LAYER 2
    # "COUPLE MIDS"
    # The Relationship As A Person - It's Chart
    # the potiential relationship - the combination of the 2 people - as if the relationship is a person - called the potiential relationship
    potientialRelationshipMids = aa.midpointsFrom2Planets360(planets360_P1, planets360_P2)  # <--
    print(f"potientialRelationshipMids: {potientialRelationshipMids}")

    # LAYER 3
    # the way you feel about the potiential relationship - mids
    feelAboutPotiential_P1 = aa.midpointsFrom2Planets360(planets360_P1, potientialRelationshipMids)  # <--
    print(f"feelAboutPotiential_P1: {feelAboutPotiential_P1}")

    # how you/THEY feel about the potiential relationship -mids-like it's a person
    feelAboutPotiential_P2 = aa.midpointsFrom2Planets360(planets360_P2, potientialRelationshipMids)  # <--
    print(f"feelAboutPotiential_P2: {feelAboutPotiential_P2}")

    # LAYER 4
    # the feelings About - The Potiential - Relationship
    # how your side of the potiential relationshp (as a person) * Affects * -YOU-/them
    howPotientialRelatinoshipAffects_P1 = aa.midpointsFrom2Planets360(planets360_P1, feelAboutPotiential_P1)  # <--
    print(f"howPotientialRelatinoshipAffects_P1: {howPotientialRelatinoshipAffects_P1}")

    # how their side of the potiential relationshp (as a person) * Affects * you/-THEM-
    howPotientialRelatinoshipAffects_P2 = aa.midpointsFrom2Planets360(planets360_P2, feelAboutPotiential_P2)  # <--
    print(f"howPotientialRelatinoshipAffects_P2: {howPotientialRelatinoshipAffects_P2}")



#------------------------------

# import ASTROLOGYfunctions as aa
# aa.oneSETofData()
def oneSETofData():
    import ASTROLOGYfunctions as aa

    # add in 2 people birthcharts - for it to check if it matches any
    #
    # PERSON 1:# planets = aa.cache1Birthchart(y=y, m=m, d=d, h=h, m1=m1, city=city)
    planets360_P1 = aa.cache1Birthchart(y=1981, m=10, d=12, h=3, m1=6, city="Kansas City, MO")
    print(f"planets360_P1 ({len(planets360_P1)}): {planets360_P1}")
    #
    # PERSON 2:
    planets360_P2 = aa.cache1Birthchart(y=1984, m=4, d=18, h=12, m1=0, city="Mexico City, Mexico")  # <--
    print(f"planets360_P2 ({len(planets360_P2)}): {planets360_P2}")

    # LAYER 1
    # the initial chemistry ... the way you feel when you first see or meet them
    # 1st P - left side ... 2nd P - right side ... genders, retrograde

    # LAYER 2
    # "COUPLE MIDS"
    # The Relationship As A Person - It's Chart
    # the potiential relationship - the combination of the 2 people - as if the relationship is a person - called the potiential relationship
    potientialRelationshipMids = aa.midpointsFrom2Planets360(planets360_P1, planets360_P2)  # <--
    print(f"potientialRelationshipMids: {potientialRelationshipMids}")

    # LAYER 3
    # the way you feel about the potiential relationship - mids
    feelAboutPotiential_P1 = aa.midpointsFrom2Planets360(planets360_P1, potientialRelationshipMids)  # <--
    print(f"feelAboutPotiential_P1: {feelAboutPotiential_P1}")

    # how you/THEY feel about the potiential relationship -mids-like it's a person
    feelAboutPotiential_P2 = aa.midpointsFrom2Planets360(planets360_P2, potientialRelationshipMids)  # <--
    print(f"feelAboutPotiential_P2: {feelAboutPotiential_P2}")

    # LAYER 4
    # the feelings About - The Potiential - Relationship
    # how your side of the potiential relationshp (as a person) * Affects * -YOU-/them
    howPotientialRelatinoshipAffects_P1 = aa.midpointsFrom2Planets360(planets360_P1, feelAboutPotiential_P1)  # <--
    print(f"howPotientialRelatinoshipAffects_P1: {howPotientialRelatinoshipAffects_P1}")

    # how their side of the potiential relationshp (as a person) * Affects * you/-THEM-
    howPotientialRelatinoshipAffects_P2 = aa.midpointsFrom2Planets360(planets360_P2, feelAboutPotiential_P2)  # <--
    print(f"howPotientialRelatinoshipAffects_P2: {howPotientialRelatinoshipAffects_P2}")



#------------------------------


# import ASTROLOGYfunctions as aa
# aa.getMidPointsFrom2Birthcharts()
def getMidPointsFrom2Birthcharts():
    import ASTROLOGYfunctions as aa
    planets30_P1 = aa.openSaveBirthchartCSVcache(y=1981, m=10, d=12, h=3, m1=6, lat="39n05", long="94w34")
    planets360_P1 = aa.degrees360convert(planets30_P1)
    # print(f"planets360_P1: {planets360_P1}")

    planets60_P2 = aa.openSaveBirthchartCSVcache(y=1984, m=4, d=18, h=12, m1=0, lat="19N25", long="99W7")
    planets360_P2 = aa.degrees360convert(planets60_P2)  # <--
    # print(f"planets360_P2: {planets360_P2}")

    mids = aa.midpointsFrom2Planets360(planets360_P1, planets360_P2)  # <--
    print(f"mids: {mids}")
    return mids


#------------------


# import ASTROLOGYfunctions as aa
# planets360 = aa.degrees360convert(planets60) # <--
# print(f"planets360: {planets360}")

# use this - on 2 birthcharts - then get the middle of both charts
def degrees360convert(planets):
    #print(f"planets ({len(planets)}): {planets}")
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    # string = f.strip1(string)
    c=0
    planetSignDegree360 = []
    for planetSignDegree in planets:
        if ":" in planetSignDegree: #if it's something - not blank
            #print(f"planetSignDegree: {planetSignDegree}")
            p = planetSignDegree.split(":")
            #print(f"{c}) p: {p}")

            planetName = p[0]
            signDegrees = f.strip1(p[1])
            s = signDegrees.split(" (")
            sign = s[0]
            degrees = s[1].strip(")").strip("(")
            degrees360 = aa.sign30to360(sign=sign,sign30=degrees)
            #print(f"{c}) {planetName} - {sign} - {degrees} ... deg360: {degrees360}")
            p360 = f"{planetName}: {sign} ({degrees360})"
            planetSignDegree360.append(p360)
            c += 1
    planets360 = planetSignDegree360

    return planets360



# import ASTROLOGYfunctions as aa
# planets30 = aa.degrees30convert(planets360)
# print(f"planets30: {planets30}")

# use this - on 2 birthcharts - then get the middle of both charts
def degrees30convert(planets):
    #print(f"planets ({len(planets)}): {planets}")
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    # string = f.strip1(string)
    c=0
    planetSignDegree30 = []
    for planetDegree in planets:
        #LIST ALL PLANETS - UNCOMMENT THIS LINE
        # print(f"planetDegree: {planetDegree}")
        if ":" in planetDegree: #if it's something - not blank
            #print(f"planetSignDegree: {planetSignDegree}")
            p = planetDegree.split(": ")
            #print(f"{c}) p: {p}")
            planetName = p[0]
            d = degreesRxDecDisSpeed = p[1].split("/") # sometimes has " Rx" on the end
            #print(f"degreesRxDecDisSpeed: {degreesRxDecDisSpeed}")
            degrees = d[0]
            if len(d)==1: #midpoints - only have degrees - 1 spot
                sign, deg30 = aa.sign360to30(degrees)
                deg30 = f.round_down2(deg30)
                p30 = f"{planetName}: {sign} ({deg30})"
                planetSignDegree30.append(p30)
            else: # 'Sun_g: 198.9509/Rx0/-0.0001/0.9978/0.9893'
                one = d[1] #Midpoints - only have degrees - nothing else -
                two = d[2]
                three = d[3]
                four = d[4]
                sign,deg30 = aa.sign360to30(degrees)
                deg30 = f.round_down2(deg30)
                #print(f"{c}) {planetName} - {sign} - {degrees} ... deg360: {degrees360}")
                p30 = f"{planetName}: {sign} ({deg30})/{one}/{two}/{three}/{four}"
                planetSignDegree30.append(p30)
                c += 1
    planets30 = planetSignDegree30

    return planets30


"""
#libra 18 = 198 (in deg360)
#sign="Libra"
#sign30=18
sign360 = 36 #aa.sign30to360(sign=sign,sign30=sign30) # sign360: 198
print (f"sign360: {sign360}\n")
sign,sign30 = aa.sign360to30(deg360=sign360)
print (f"sign,sign30: {sign,sign30}")
sign360 = aa.sign30to360(sign=sign,sign30=sign30)
print (f"sign360: {sign360}")
sign,sign30 = aa.sign360to30(deg360=sign360)
print (f"sign,sign30: {sign,sign30}")

GOES WITH BELOW 2 FUNCTIONS - test drive - back and forth conversion
"""


# import ASTROLOGYfunctions as aa
# degrees360 = aa.sign30to360(sign="Libra",sign30=18)
def sign30to360(sign="Libra",sign30=18):
    signs12 = "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    #degrees around the wheel - starting with 30 degrees for Aries
    degrees = {"Aries":0, "Taurus":30, "Gemini":60, "Cancer":90, "Leo":120, "Virgo":150, "Libra":180, "Scorpio":210, "Sagittarius":240, "Capricorn":270, "Aquarius":300, "Pisces":330, } # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    #print(f"degrees[sign]+sign30 ... {degrees[sign]}+{sign30} = {int(degrees[sign])+int(sign30)}")
    num360 = int(degrees[sign])+int(sign30)
    return num360


#libra 18 = 198 (in deg360)
#sign360 = sign30to360(sign="Libra",sign30=18)
#print (f"sign360: {sign360}")


#---------------------------
# import ASTROLOGYfunctions as aa
# degrees360 = aa.sign30to360(sign="Libra",sign30=18)
# import ASTROLOGYfunctions as aa
# sign,sign30 = aa.sign360to30(deg360=198)
#---------------------------

# import ASTROLOGYfunctions as aa
# sign,degrees30 = aa.sign360to30(deg360=198)
def sign360to30(deg360=198):
    import FUNCTIONS as f
    deg360 = float(deg360)

    signs12 = {1:"Aries", 2:"Taurus", 3:"Gemini", 4:"Cancer", 5:"Leo", 6:"Virgo", 7:"Libra", 8:"Scorpio", 9:"Sagittarius", 10:"Capricorn", 11:"Aquarius", 12:"Pisces"}
    #degrees around the wheel - starting with 30 degrees for Aries
    degrees = {"Aries":0, "Taurus":30, "Gemini":60, "Cancer":90, "Leo":120, "Virgo":150, "Libra":180, "Scorpio":210, "Sagittarius":240, "Capricorn":270, "Aquarius":300, "Pisces":330, } # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

    num = int(f.round_down(deg360/30))+1 # gives which sign - as a number in a list - organize a new variable
    sign = signs12[num]
    lessDegrees = degrees[sign] #less 30 * the number of sign
    sign30 = deg360 - lessDegrees
    return sign,sign30




#---------------------------



# import ASTROLOGYfunctions as aa
# aa.getSignNameOn30format(string) #Sun: Libra (18) ... it pulls it from this string
def getSignNameOn30format(string): # Sun: Libra (18)
    import FUNCTIONS as f
    signDegrees = f.strip1(string.split(": ")[1])  # Libra (18)
    signName = f.strip1(signDegrees.split(" ")[0])
    return signName

# import ASTROLOGYfunctions as aa
# aa.getPlanetName(string) #Sun: Libra (18) ... it pulls it from this string
def getPlanetName(string):
    import FUNCTIONS as f
    s = string.split(":")
    planetName = f.strip1(s[0])
    return planetName

# import ASTROLOGYfunctions as aa
# aa.getNumberInString(string) #Sun: Libra (18)
def getNumberInString(string): #Sun: 198 ... NOW IT'S THIS FORMAT
    #print(f"string: {string}")
    import FUNCTIONS as f
    s = string.split(": ")
    numRx = f.strip1(s[1])
    #remove Rx
    Rx = ""
    if "Rx" in numRx:
        Rx = "Rx"
        numRx = numRx.strip(" Rx")
    degrees = float(numRx)
    return degrees


# import ASTROLOGYfunctions as aa
# midNum = aa.midpointFrom2_360s(n1, n2) #2 numbers that are 360's
def midpointFrom2_360s(n1, n2):
    import FUNCTIONS as f
    mid = 0
    if n1>n2:
        mid = ( (n1-n2) / 2) + n2 #halfway in between the 2 numbers
    elif n1==n2:
        mid = ( (n1-n2) / 2) + n2
    elif n2>n1:
        mid = ((n2 - n1) / 2) + n1  # halfway in between the 2 numbers
    mid = f.round_down4(mid)
    return mid


"""
#import OPENsomething as o
#import ASTROLOGYfunctions as aa
#planets30_P1 = o.openSaveBirthchartCSVcache(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")
#planets360_P1 = aa.degrees360convert(planets30_P1)
# print(f"planets360_P1: {planets360_P1}")

#planets60_P2 = o.openSaveBirthchartCSVcache(y=1984,m=4,d=18,h=12,m1=0,lat="19N25",long="99W7")
#planets360_P2 = aa.degrees360convert(planets60_P2) # <--
# print(f"planets360_P2: {planets360_P2}")

#mids = aa.midpointsFrom2Planets360(planets360_P1, planets360_P2) # <--
#print(f"mids: {mids}")
"""
#find the midpoints
# import ASTROLOGYfunctions as aa
# aa.midpointsFrom2Planets360(planets360_P1, planets360_P2)
def midpointsFrom2Planets360(planets360_P1, planets360_P2):
    mids = []
    #print(f"{len(planets360_P1)}")
    for i in range(len(planets360_P1)):
        planetName = getPlanetName(planets360_P1[i])
        d360_1 = getNumberInString(planets360_P1[i]) # 198
        d360_2 = getNumberInString(planets360_P2[i]) # 28
        mid_360 = midpointFrom2_360s(d360_1, d360_2) # 113
        #sign, degrees30 = f.sign360to30(mid_360) #sign and degrees within 30
        #print(f"Both People: {planets360_P1[i]} ... {planets360_P2[i]} ... midpoint ({mid_360}): {planetName}: {sign} ({degrees30})")
        #print(f"{planetName} - p1 - {d360_1} ... p2 - {d360_2} ... the midpoint: {mid_360} / {sign} ({degrees30}) ")
        mids.append(f"{planetName}: {mid_360}") # - ({sign} ({degrees30}))
    return mids


#-----------------------------



# import ASTROLOGYfunctions as aa
# planets = aa.makeSaturnChironMidpointForPlanets()
def makeSaturnChironMidpointForPlanets(planets):  # for SaturnChironMidpoint
    # 'SaturnChironMidpoint' is not there - make it
    # at the end of when the functions give me the csv data - add this to the end of that

    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    #planets = aa.openSaveBirthchartCSVcache(y=y, m=m, d=d, h=h, m1=m1, lat=lat, long=long)
    #print("--it must have the SaturnChironMidpoint at the end--")
    #print(f"planets ({len(planets)}):")
    #f.print2(planets)

    chiron = ""
    saturn = ""
    for planetSignDeg in planets:
        if "Saturn" in planetSignDeg:
            saturn = planetSignDeg
        if "Chiron" in planetSignDeg:
            chiron = planetSignDeg
    #print(f"{saturn} ... {chiron} ... midpoint?")

    degS = int(saturn.split(": ")[1].strip(" Rx"))
    degC = int(chiron.split(": ")[1].strip(" Rx"))

    # -------------
    midNum = aa.midpointFrom2_360s(degS, degC)  # 2 numbers that are 360's
    #print(f"SaturnChironMidpoint: midNum: {midNum}")
    # -------------

    # degrees360 = aa.sign30to360(sign="Libra",sign60=18)

    #sign, deg30 = aa.sign360to30(deg360=midNum)
    #print(sign, deg30)

    planetSignDegree = f"SaturnChironMidpoint: {midNum}"
    #print(f"planetSignDegree: {planetSignDegree}")

    # Add in the SaturnChironMidpoint:
    planets.append(planetSignDegree)

    return planets


#-----------------------------


# goes through each state and caches the lat long
# it doesn't let me past 62 - gotta find out why
# import ASTROLOGYfunctions as aa
# aa.cacheALLlatLong() #ALL at once
def cacheALLlatLong():
    import time
    import ASTROLOGYfunctions as aa
    import listAllFILES as lf
    states = lf.returnStates()
    # print(states[1])
    # exit()

    c = 62
    for i in range(len(states) - 1):
        if i > c:  # only after starting number
            state = states[i]
            print(f"{c}) state: {state}")
            c += 1
            # if c==3:
            # exit()
            aa.cacheTheCity(state)
            time.sleep(.25)
        else:
            # do nothing - we are trying to start at a later number
            pass


# import ASTROLOGYfunctions as aa
# aa.cacheLatLong(city="San Jose, CA")

#not working yet
def cacheLatLong(city="San Jose, CA"):
    cacheFilename = "lat-long-cache.csv"
    import OPENsomething as o
    import ASTROLOGYfunctions as aa
    writeString = ""
    #city = "San Jose, CA"
    #this is below in the code: fixing it
    try:  # it's not getting the lat and long - so go to that function #"San Jose, CA" - it failed on this
        letterLat, letterLong = aa.mapQuestLatLong(city)
        decLat = letterLatToDecimalLat(letterLat)
        decLong = letterLongToDecimalLong(letterLong)
        writeString = f"{city}, {letterLat}, {letterLong}, {decLat}, {decLong}"
        print(writeString)
    except:
        print("couldn't get long and lat conversion - error")
        exit()
    #cache it, check if it's there already, append it to a file
    # SAVES the 4 lat-longs
    #don't write doubles - function to check if it's already there
    try:
        print(f"csv cached?: {city} ?")
        o.appendFile(cacheFilename,writeString)
        print(f"csv cached: {city}")
    except:
        print("error - couldn't append file - to cache it")

#cacheLatLong(city="San Jose, CA")




# import ASTROLOGYfunctions as aa
# aa.cacheAllCitiesLatLong()

def cacheAllCitiesLatLong():
    import listAllFILES as lf
    import ASTROLOGYfunctions as aa
    cityStates = lf.returnStates()

    for cityState in cityStates:
        # cache it here
        aa.cacheTheCity(cityState)


#-----------------------------

# import ASTROLOGYfunctions as aa
# lat, long = aa.cacheTheCity(city="Phoenix, AZ")

def cacheTheCity(city="Phoenix, AZ"):
    import ASTROLOGYfunctions as aa
    import OPENsomething as o
    import FUNCTIONS as f

    cached = aa.findTheCityInCache(city)
    #the city is not in the cache yet
    if cached == False:
        #print(f"Going to Cache: {city}")
        # cacheTheCity(city="Phoenix, AZ")

        # this is below in the code: fixing it
        try:  # it's not getting the lat and long - so go to that function #"San Jose, CA" - it failed on this
            letterLat, letterLong = aa.mapQuestLatLong(city)
            decLat = letterLatToDecimalLat(letterLat)
            decLong = letterLongToDecimalLong(letterLong)
            writeString = f"{city}, {letterLat}, {letterLong}, {decLat}, {decLong}"
            #print(writeString)
            f.appendFile("cache-lat-long.csv", writeString)
            print(f"Successfully Cached the lat/long for {city}")
            return letterLat, letterLong
        except:
            try:
                letterLat, letterLong = aa.bingMapsLatLong(city)
                return letterLat, letterLong
            except:
                print("error - there was an exception - for - f.cityStateToLatLong(city=city)")
                print("--change this line: user_agent='Astrology_Horoscope'? - I think it helps")
                #opens default browser - to wikipedia search for city
                import webbrowser
                search_query = "wikipedia " + city + " lat long"
                google_search = f"https://www.google.com/search?q={search_query}"
                o.openURLinBrowser(url=google_search)
                exit()
    # the city is in the cache, return lat, long
    elif cached == True:
        #return lat, long
        #print(f"{city} is Already Cached")
        letterLat, letterLong = aa.mapQuestLatLong(city)
        return letterLat, letterLong


# import ASTROLOGYfunctions as aa
# decLat, decLong = aa.cacheTheCity2(city="Phoenix, AZ")

def cacheTheCity2(city="Phoenix, AZ"):
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    import OPENsomething as o

    cached = aa.findTheCityInCache(city)
    #the city is not in the cache yet
    if cached == False:
        #print(f"Going to Cache: {city}")
        # cacheTheCity(city="Phoenix, AZ")

        # this is below in the code: fixing it
        try:  # it's not getting the lat and long - so go to that function #"San Jose, CA" - it failed on this
            letterLat, letterLong = aa.mapQuestLatLong(city)
            decLat = letterLatToDecimalLat(letterLat)
            decLong = letterLongToDecimalLong(letterLong)
            decLong = f.round_down2(decLong)
            decLat = f.round_down2(decLat)
            return decLat, decLong
        except:
            try:
                letterLat, letterLong = aa.bingMapsLatLong(city)
                decLat = letterLatToDecimalLat(letterLat)
                decLong = letterLongToDecimalLong(letterLong)
                decLong = f.round_down2(decLong)
                decLat = f.round_down2(decLat)
                return decLat, decLong
            except:
                print("error - there was an exception - for - f.cityStateToLatLong(city=city)")
                print("--change this line: user_agent='Astrology_Horoscope'? - I think it helps")
                #opens default browser - to wikipedia search for city
                import webbrowser
                search_query = "wikipedia " + city + " lat long"
                google_search = f"https://www.google.com/search?q={search_query}"
                o.openURLinBrowser(url=google_search)
                exit()
    # the city is in the cache, return lat, long
    elif cached == True:
        #return lat, long
        #print(f"{city} is Already Cached")
        letterLat, letterLong = aa.mapQuestLatLong(city)
        decLat = letterLatToDecimalLat(letterLat)
        decLong = letterLongToDecimalLong(letterLong)
        decLong = f.round_down2(decLong)
        decLat = f.round_down2(decLat)

        return decLat, decLong



# import ASTROLOGYfunctions as aa
# cached = aa.findTheCityInCache(city = "Phoenix, AZ")
# if cached==False:
#   aa.cacheTheCity(city="Phoenix, AZ")

def findTheCityInCache(city = "Phoenix, AZ"):
    import FUNCTIONS as f
    #city = "Phoenix, AZ"
    found_the_city = False
    lines = f.readFile("cache-lat-long.csv")
    for line in lines:
        l=line.split(", ")
        #print(f"l: {l}")
        city2 = l[0]+", "+l[1]
        # if it's a 3 word seperated by comma - city name:
        if ("N" in l[3] or "S" in l[3]) and ("E" in l[4] or "W" in l[4]):
            city2 = l[0]+", "+l[1]+", "+l[2]
        if city==city2: #does the city match the line?
            #print(f"Found City in Cache: {city2}")
            # exit()
            found_the_city = True
    return found_the_city



# import ASTROLOGYfunctions as aa
# lat, long = aa.findTheLatLongOfCityInCache(city = "Phoenix, AZ")

def findTheLatLongOfCityInCache(city = "Phoenix, AZ"):
    import FUNCTIONS as f
    #city = "Phoenix, AZ"
    found_the_city = False
    lines = f.readFile("cache-lat-long.csv")
    for line in lines:
        l=line.split(", ")
        #print(f"l: {l}")
        city2 = l[0]+", "+l[1]
        if ("N" in l[3] or "S" in l[3]) and ("E" in l[4] or "W" in l[4]):
            city2 = l[0]+", "+l[1]+", "+l[2]
        if city==city2: #does the city match the line?
            #print("Found City in Cache")
            found_the_city = True
            lat = l[2]
            long = l[3]
            #print(f"lat/long: {lat} / {long}")
            return lat, long
    #if it didn't find a match, return this
    return 0.001,0.001





# import ASTROLOGYfunctions as aa
# decimalLat = aa.letterLatToDecimalLat(string="39N6")
def letterLatToDecimalLat(string="39N6"):
    #print(f"letterLatToDecimalLat ... string: {string}")
    s2 = string
    if 'N' in s2:
        s = s2.split("N")
        #the number is positive
    elif 'S' in s2:
        s = s2.split("S")
        #also the number is now negative
    try:
        decimal = int(s[0]) + int(s[1])/60
    except:
        print("lat long cache - city has 3 words, not 2 - so it doesn't work")
        print("put all of the cities - in single quotes, in the csv")
    if 'S' in s2:
        decimal = decimal * -1
    return decimal


# import ASTROLOGYfunctions as aa
# decimalLong = aa.letterLongToDecimalLong(string="94W34")
def letterLongToDecimalLong(string="94W34"):
    s2 = string
    if 'E' in s2:
        s = s2.split("E")
        # the number is positive
    elif 'W' in s2:
        s = s2.split("W")
        # also the number is now negative
    decimal = int(s[0]) + int(s[1]) / 60
    if 'W' in s2:
        decimal = decimal * -1
    return decimal



# import ASTROLOGYfunctions as aa
# letterLat = aa.decimalLatToLetterLat(d=39.10)
def decimalLatToLetterLat(d=39.10): #for serannu
    import FUNCTIONS as f
    if d < 0:  # negative
        letter = "S"
        d = -1*d
    else:
        letter = "N"
    lat = d
    latDegree = int(f.round_down(lat))
    fraction = lat - latDegree  # the fraction is left
    # print(f"result_long: {result_long}")
    resultLatMinute = int( f.round_down(fraction * 60) ) # //100

    string = f"{latDegree}{letter}{resultLatMinute}"
    return string



# import ASTROLOGYfunctions as aa
# letterLong = aa.decimalLongToLetterLong(d=-94.57)
def decimalLongToLetterLong(d=-94.57): #for serannu
    import FUNCTIONS as f
    if d<0: #negative
        letter="W"
        d = -1*d
    else:
        letter="E"
    long = d
    longDegree = int(f.round_down(long))
    fraction = long - longDegree  # the fraction is left
    # print(f"result_long: {result_long}")
    resultLongMinute = int(f.round_down(fraction * 60))  # //100

    string = f"{longDegree}{letter}{resultLongMinute}"
    return string


#-------------------------------


# import ASTROLOGYfunctions as aa
# timeZoneOffset = aa.getTimezoneOffsetBing(city="Kansas City, MO", datetime="12.10.1981 3:15:00")
def getTimezoneOffsetBing(city="Kansas City, MO", datetime="12.10.1981 3:15:00"):
    #city = "Kansas City, MO"
    BingMapsKeyAPI = "Alp-h4VbPTew-RBbcOOj89hst9vIjFRhr44-jiWV2onZsdiA24QtDiBxAkLsTIqb"
    url1 = f"https://dev.virtualearth.net/REST/v1/TimeZone/?query={city}&datetime={datetime}&key={BingMapsKeyAPI}"
    #url2 = "https://dev.virtualearth.net/REST/v1/TimeZone/39.1,-94.5?key="+BingMapsKeyAPI+""
    #print(f"city: {city} ... url: {url1}")

    #GET:
    # 'utcOffsetWithDst': '-5:00'
    #that's what it is in mycosmicdna

    import requests
    response = requests.get(url1) # "http://api.open-notify.org/astros.json"
    content1 = t = str(response.json())
    print(f"content1: {content1}")
    c2 = t.split("utcOffsetWithDst")[1]
    c2 = c2.split("0'")[0]+"0"
    #print(f"c2: {c2}")
    c3 = c2.split("'")[2] #-5:00
    #print(f"c3: {c3}")
    c4 = c3.split(":")
    c5 = int(c4[0]) #-5
    print(f"c5: {c5}")
    return c5
#'utcOffsetWithDst': '-5:00'


# import ASTROLOGYfunctions as aa
# dateNew, timeNew = aa.applyTimezoneOffset(tzOffset=-5, date="12.10.1981", time="3:15:00")
def applyTimezoneOffset(tzOffset=-5, date="12.10.1981", time="3:15:00"):
    tzOffset = float(tzOffset)
    #print(f"tzOffset ({tzOffset}) ... date ({date}) ... time ({time}) ... ")
    d2 = date.split(".")
    m = int(d2[0])
    d = int(d2[1])
    y = int(d2[2])
    t2 = time.split(":")
    h = int(t2[0])
    m1 = int(t2[1])
    #print(f"h ({h}) ... m1 ({m1})")

    if tzOffset > 0:
        # subtract hours
        h -= tzOffset
    elif tzOffset < 0:
        # add hours
        h += -1 * tzOffset

    if h > 23:
        # increment the day for the date
        d += 1
        # subtract the day from the hours
        h -= 24

    # handle if it was at 11pm and timezone was negative
    # - the day could go past the end of the month

    dateNew = f"{m}.{d}.{y}"
    timeNew = f"{h}:{m1}:00"

    return dateNew, timeNew




#at the end, if decimals, reduce it to 2 decimal places
#
# import ASTROLOGYfunctions as aa
# city = "San Francisco, CA"
# lat, long = aa.mapQuestLatLong(city)
# print(f"lat, long: {lat, long}")
def mapQuestLatLong(city = "San Francisco, CA"):
    #check if it's cached first
    import ASTROLOGYfunctions as aa
    cached = aa.findTheCityInCache(city)
    if cached == True:
        return aa.findTheLatLongOfCityInCache(city)
    if cached == False:
        import FUNCTIONS as f
        import geocoder #pip install geocoder
        mapquest_apikey = "VnGw3KlAwIjNMmALFUuZcsFPAsZF1Bk3"
        g = geocoder.mapquest(''+city+'', key=mapquest_apikey)
        #print(f"g.json: {g.json}")
        #print(f"g.json['lat']: {g.json['lat']}")
        latDecimal = g.json['lat']
        longDecimal = g.json['lng']

        #reduce to 2 decimal places
        latDecimal = f.round_down4(latDecimal)
        longDecimal = f.round_down4(longDecimal)

        return latDecimal, longDecimal


# import ASTROLOGYfunctions as aa
# city = "San Francisco, CA"
# lat, long = aa.bingMapsLatLong(city)
# print(f"lat, long: {lat, long}")
def bingMapsLatLong(city = "San Francisco, CA"):
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    cached = aa.findTheCityInCache(city)
    if cached == True:
        return findTheLatLongOfCityInCache(city)
    if cached == False:
        import geocoder #pip install geocoder
        bing_maps_apikey = "AvWQMcU8xf2s_cQ9toOcavGSmChheyvLEhr1jfUz4bHZ6VG53OZ_4pWy_mQ6wwAR"
        g = geocoder.bing(''+city+'', key=bing_maps_apikey)
        #print(f"g.json: {g.json}")
        #print(f"g.json['lat']: {g.json['lat']}")
        latDecimal = g.json['lat']
        longDecimal = g.json['lng']

        latDecimal = f.round_down4(latDecimal)
        longDecimal = f.round_down4(longDecimal)

        return latDecimal, longDecimal







#-------------------------------






#-------------------------------------------





# import ASTROLOGYfunctions as aa
# filenameCSV = "writeFile.csv"
# CSVstring = "1,2,3"
# aa.birthchartCSVsave(filenameCSV, CSVstring) #helper function

def birthchartCSVsave(filenameCSV, CSVstring):
    import FUNCTIONS as f
    f.writeFile(filenameCSV, CSVstring)
    print(f'Cached Mini-Birthchart csv file successfully: {filenameCSV}')


#-----------------------


# import ASTROLOGYfunctions as aa
# peopleCSV = aa.pdnaBankGetMyPeopleCSV()

def pdnaBankGetMyPeopleCSV():
    import FUNCTIONS as f
    #saved - had to change the file encoding
    #now it opens
    import OPENsomething as o
    filename = "db_pdnabank.txt" # C:/Users/myvor/PycharmProjects/pythonProject/
    lines = f.readFile(filename) # array of lines
    people = []
    #print(f"filename: {filename}")
    #print(f"lines: {len(lines)}: ")
    #print(lines)

    for line in lines:
        if len(line) > 1: #avoid errors
            print(f"line ({len(line)}): {line}")
            l = line.split("	")
            id = l[0]
            if "1000000001-pdna-" in id:
                try:
                    name = l[1]
                    pic = l[9]
                    # print(f"id: {id}")
                    # print(f"name: {name}")
                    # print(f"pic: {pic}")
                    # print("one of my pdna bank people")
                    var = name, pic, id
                    people.append(var)
                except:
                    pass

    #print("\n--My PdnaBank--:")
    #print(f"people ({len(people)}): {people}")
    if len(people)>1:
        return people


# import ASTROLOGYfunctions as aa
# personInfo = aa.pdnaBank1person(nameAsk="Test")
# print(f"personInfo ({len(personInfo)}):")
# f.print2(personInfo)
# print(f"personInfo ({len(personInfo)}):")

def pdnaBank1person(nameAsk="Test"):
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa
    people = aa.pdnaBankGetAllPeople_AllStuff()
    #print(f"people: ({len(people)})")
    #f.print2(people)
    #exit()

    info = {}
    for person in people:
        #print(f"person: {person}")
        #print("is name [2]?")
        name = person['name']
        #print(f"name: {name}")
        #exit()
        if nameAsk in person['name']: #return first result of a name match
            return person
    return ""


# import ASTROLOGYfunctions as aa
# people = aa.pdnaBankGetAllPeople_AllStuff()

def pdnaBankGetAllPeople_AllStuff():
    import FUNCTIONS as f
    #saved - had to change the file encoding
    #now it opens
    import OPENsomething as o
    filename = "db_pdnabank.txt" # C:/Users/myvor/PycharmProjects/pythonProject/
    lines = f.readFile(filename) # array of lines
    #print(f"filename: {filename}")
    #print(f"lines: {len(lines)}: ")
    #print(lines)
    #exit()
    people = []
    for line in lines:
        l = line.split('", "')

        id = l[0]

        if "1000000001-pdna-" in id:

            #exit()
            id = l[0]
            #print(f"id1: {id}")
            #print(l)
            name = l[1].strip('"').strip("'")
            datetime = l[2].strip('"').strip("'")  # 1981-02-22 03:30:00
            city = l[3].strip('"').strip("'")
            timezone = l[4].strip('"').strip("'")
            timeknown = l[5].strip('"').strip("'")  # time_given, time_not_given
            category = l[6].strip('"').strip("'")  # Friends, Dating, All
            dateAdded = l[7].strip('"').strip("'")
            dateUpdated = l[8].strip('"').strip("'")
            imgFilename = l[9].strip('"').strip("'")
            notes = l[10].strip('"').strip("'")
            #gender = "Female" # default
            gender = l[11].strip("\n").strip('"').strip("'")

            #print(f"id: {id} ... name: {name} ... datetime: {datetime} ... city: {city}")
            #print(f"timezone: {timezone} ... timeknown: {timeknown} ... category: {category}... gender: {gender}")
            #print(f"dateAdded: {dateAdded} ... dateUpdated: {dateUpdated} ... imgFilename: {imgFilename}")
            #print(f"... notes: {notes}")
            #print("")

            #exit()
            #print(f"id: {id}")
            #print(f"name: {name}")
            #print(f"pic: {pic}")
            #print("one of my pdna bank people")
            pic = imgFilename
            var = {"name":name, "datetime": datetime, "city": city, "timezone":timezone, "timeknown":timeknown, "category":category, "dateAdded":dateAdded, "dateUpdated":dateUpdated, "imgFilename":imgFilename, "notes":notes, "gender":gender}
            #print(f"var: {var}")
            people.append(var)

    #print("\n--My PdnaBank--:")
    #print(f"people ({len(people)}): {people}")
    #print("exiting")
    #exit()
    return people



#-----------------------

# import ASTROLOGYfunctions as aa
# people = aa.pdnaBankGetMyPeopleCSV_BirthchartStuff()
# people - has ... name, datetime, cityState, timezone, id, pic - for each entry

#get more fields, the ones you need for a birthchart
def pdnaBankGetMyPeopleCSV_BirthchartStuff(): #give them the timezone - cache
    import FUNCTIONS as f
    #saved - had to change the file encoding
    #now it opens
    import OPENsomething as o
    filename = "db_pdnabank.txt" # C:/Users/myvor/PycharmProjects/pythonProject/
    #print(f"filename: {filename}")
    lines = f.readFile(filename) # array of lines
    people = []
    #print(f"filename: {filename}")
    #print(f"lines: {len(lines)}: ")
    #print(lines)
    for line in lines:
        l = line.split("	")
        id = l[0]
        if "1000000001-pdna-" in id:
            #print(f"Split Line: {l}")
            name = l[1]
            datetime = l[2]
            city = l[3]
            timezone = l[4]
            pic = l[9]
            #print(f"id: {id}")
            #print(f"name: {name}")
            #print(f"pic: {pic}")
            #print("one of my pdna bank people")
            var = name, datetime, city, timezone, id, pic
            people.append(var)
    #print("\n--My PdnaBank--:")
    print(f"people ({len(people)}): {people}")
    return people


#-------------------------------------------








# import ASTROLOGYfunctions as aa
# csv = aa.loadCachedCSVbirthchart(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34")

#now do loading the cached csv birthcharts
def loadCachedCSVbirthchart(y=1981,m=10,d=12,h=3,m1=6,lat="39n05",long="94w34"):
    pass
















#-------------------------------

# import ASTROLOGYfunctions as aa
# html = aa.openSaveBirthchartAsFile()
# planets = aa.parseBirthchartHTML(html)
# print(f"planets: {planets}")
def parseBirthchartHTML(html="<html>"): # birthchart html from serennu # "https://serennu.com/astrology/ephemeris.php?inday=12&inmonth=10&inyear=1981&inhours=03&inmins=06&insecs=00&insort=pname&z=t&gh=g&addobj=&inla=39n05&inlo=94w34&h=P"
  import time
  from bs4 import BeautifulSoup

  # parse it with Beautiful Soup
  # print(f"html: {html}")

  soup = BeautifulSoup(html, 'lxml')
  planetsTable = soup.find("table", {
    "id": "results"})  # img.YVj9w ...chooses the images - that have sizes on them - in the long 'srcset' attribute
  # print(f"planets ({len(planets)}): {planets}")
  htmlParts = str(planetsTable).split("<tr>")
  # print(f"htmlParts ({len(htmlParts)}): {htmlParts}")

  # got the rows
  # now get the tds
  rows = []
  for htmlPart in htmlParts:
    t = str(htmlPart).split("<td>")
    rows.append(t)
  rows.pop(0)  # like php unset(r[0])
  time.sleep(0.001)
  planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Chiron",
             "Juno"]
  # ------------------------------
  rows2 = []
  for row in rows:
    row2 = str(row).replace("</td>", "").replace("\\n", "").replace("</tr>", "").replace("\\", "")
    rows2.append(row2)
  # ------------------------------
  # print(f"rows2 ({len(rows2)}): {rows2}")
  # print(rows2[0])
  # print(rows2[10])
  # r = rows2[10].split(", ")
  # print(f"{r[2]}, {r[3]}")

  # print(f"planets ({len(rows2)}): ")
  # ------------------------------
  myPlanets = []
  otherAstroids = []

  c = 0
  for row in rows2:
    # print(f"{c}) row: {row}")
    c += 1
    r = row.split(", ")
    planetName = r[2].strip("'")
    planetDegrees = r[3].strip("'")
    p1 = planetDegrees.replace(" cp", " Capricorn").replace(" ge", " Gemini").replace(" vi", " Virgo").replace(" sa", " Sagittarius").replace(" pi", " Pisces").replace(" le", " Leo").replace(" li", " Libra").replace(" ta", " Taurus").replace(" sc", " Scorpio").replace(" cn", " Cancer").replace(" ar", " Aries").replace(" aq", " Aquarius")
    p = p1.split(" ")
    #degrees = str(p[1])+", "+str(p[0])

    pl = planetName, planetDegrees

    if planetName in planets:
      myPlanets.append(pl)
      # print(f"---{c}) row: {planetName} ... {planetDegrees}---")
    else:
      otherAstroids.append(pl)
      # print(f"{c}) row: {planetName} ... {planetDegrees}")

  #print(f"myPlanets: {myPlanets}")
  # print(f"allPlanets: {otherAstroids}")

  myPlanetsInOrder = []
  for planet in planets:
    # print(f"planet: {planet}")
    for myPlanet in myPlanets:
      # print(f"myPlanet: {myPlanet}")
      if planet == myPlanet[0]:
        myPlanetsInOrder.append(myPlanet)

  #print(f"myPlanetsInOrder: {myPlanetsInOrder}")

  outputBirthchartInfo = []
  for planet in myPlanetsInOrder:
    planetName = planet[0]
    #split and fix the degrees sign
    p1 = planet[1].replace(" cp", " Capricorn").replace(" ge", " Gemini").replace(" vi", " Virgo").replace(" sa"," Sagittarius").replace(" pi", " Pisces")
    p1 = p1.replace(" le", " Leo").replace(" li", " Libra").replace(" ta", " Taurus").replace(" sc"," Scorpio").replace(" cn", " Cancer").replace(" ar", " Aries").replace(" aq", " Aquarius")
    p = p1.split(" ")
    if p[0]=="": #resolving some weird data glitch - a blank [0]
      p.pop(0) #removing the blank [0]... it is resolved
    #print(p)
    sign = str(p[1]) #gets the sign
    degrees = str(p[0])
    planetInBirthchart = planetName+": "+sign+" ("+degrees+")"
    outputBirthchartInfo.append(planetInBirthchart)
    #print(f"degrees: {degrees}")

  return outputBirthchartInfo


def csvTheAngles():
    import ASTROLOGYmagi as m
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa

    me = aa.me()
    # f.print2(me['planets']['360'])

    for a1 in m.aspects_organized:
        a = m.aspects_organized[a1]
        # print(f"angleInfo ({len(a)}): {a}")
        name = a1
        class1 = a['class']  #: 'Major',
        degs = a['degrees']  #: 0,
        orb = a['meaningful_orb']  #: 10,
        power = a['power']  #: 15,
        definition = a['definition']
        print(f"{name}, {class1}, {degs}, {orb}, {power}, {definition}")


def csvMyPlanets():
    import FUNCTIONS as f
    import ASTROLOGYfunctions as aa

    me = aa.me()
    # f.print2(me['planets']['360'])

    for planetDegRx in me['planets']['360']:
        planet = aa.getPlanetName(planetDegRx)
        degrees = planetDegRx.split(": ")[1].strip(" Rx")
        Rx = ""
        if "Rx" in planetDegRx:
            Rx = "Rx"
        print(f"{planet}, {degrees}, {Rx}")


def scrapeEPHE_htmlFiles():  # got all the html files - to find rare astroid files
    import FUNCTIONS as f
    from bs4 import BeautifulSoup

    import requests
    url = "http://www.astro.com/ftp/swisseph/ephe/"
    link_start = url
    r = requests.get(url)
    html = r.text
    # print(f"html: {html}")

    savePath = "ephe/"
    filename = f"{savePath}!ephe.html"
    f.saveHTMLfile(html, filename=filename)

    soup = BeautifulSoup(html, 'lxml')

    links = []
    for link in soup.find_all('a'):
        url1 = link.get('href')
        name = link.get('name')
        if "/" in url1 and "archive" not in url1:
            links.append(url1)  # just the pages with lists of files show up here

    links.pop(0)  # gets rid of the root path for the swiss ephemeris

    # starting with 'ast0/' , 'ast1/'

    linksString = f.collapseArray(links, "' , '")

    print(f"linksString: {linksString}")

    for link in links:
        link1 = link.strip("/")
        savePath = "ephe/"
        saveFilename = savePath + link1 + ".html"
        link_start = "http://www.astro.com/ftp/swisseph/ephe/"
        htmlUrl = link_start + link
        r = requests.get(htmlUrl)
        html = r.text
        f.saveHTMLfile(html, saveFilename)





