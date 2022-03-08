#FUNCTIONS.py # other functions


# import FUNCTIONS as f
# docRoot = f.myDocumentsRoot()
# homeRoot = f.homeFolderRoot()


# import FUNCTIONS as f
# f.round_down(5.75)
# f.decimalLatToLetterLat(d=39.10)
# f.decimalLongToLetterLong(d=-94.57)
# f.letterLongToDecimalLong(string="94W34")
# f.letterLatToDecimalLat(string="39N6")

#-----------------------------
# import FUNCTIONS as f

def getLinks(html_filepath = "C:/Users/myvor/PycharmProjects/pythonProject/ephe/!index.html"):
    with open(html_filepath, 'r') as f:
        html_page = f.read()

    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    #print(links)
    return links

#-----------------------------

# import FUNCTIONS as f
# f.folder(folder_path="ephe/html")
def folder(folder_path="ephe/html"): #if folder doesn't exist, it makes the folder
    import os
    isExist = os.path.exists(folder_path)
    if isExist==True:
        pass
    else:
        #make folder
        os.makedirs(folder_path)
#-------------------


# import FUNCTIONS as f
# lines = f.readFile("cache-lat-long.csv")
def readFile(cacheFilename="cache-lat-long.csv"):
    rows = []
    with open(cacheFilename, "r") as f:
        for line in f:
            # look at line in loop
            #print(line, end='')
            rows.append(line)
    return rows

# import FUNCTIONS as f
# f.readAndSaveBinaryFileFromUrl(url="http://url.com/url.se1", save_to_path="ephe")
def readAndSaveBinaryFileFromUrl(url_of_item="http://url.com/url.se1",save_to_path="ephe"):
    import urllib.request, urllib.parse, urllib.error
    filename = url_of_item.split("/")[-1]
    save_path_filename = save_to_path + "/" + filename
    item1 = urllib.request.urlopen(url_of_item).read()
    fhand = open(save_path_filename, 'wb')
    fhand.write(item1)
    fhand.close()


# import FUCNTIONS as f
# filenameCSV = "writeFile.csv"
# CSVstring = "1,2,3"
# f.writeFile(filenameCSV, CSVstring)

def writeFile(filenameCSV="writeFile.csv", CSVstring="1,2,3"):
    with open(filenameCSV, 'w', encoding='utf8') as fp:
        fp.write(CSVstring)
    #print(f'file written successfully: {filenameCSV}')


# import FUCNTIONS as f
# f.writeFileBinary(url_item="http://url.com/url.txt",save_to_path="ephe")
def writeFileBinary(url_item="http://url.com/url.txt",save_to_path="ephe"):
    import requests
    response = requests.get(url_item)

    filename = url_item.split('/')[-1]
    local_filename = save_to_path+"/" + filename
    totalbits = 0
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    totalbits += 1024
                    #print("Downloaded", totalbits * 1025, "KB...")
                    f.write(chunk)


# import OPENsomething as o
# o.appendFile(cacheFilename="cache-lat-long.csv",writeString="1,2,3")
def appendFile(cacheFilename="cache-lat-long.csv",writeString="1,2,3"):
    file1 = open(cacheFilename, "a")  # append mode
    file1.write(f"{writeString}\n")
    file1.close()


#------------------------


# import FUNCTIONS as f
# string = f.stripWhitespace(string)
def stripWhitespace(string): # remove whitespace, newline, tab chars from beginning of a string - leading chars - trailing chars
    return str(string).lstrip().rstrip()


# import FUNCTIONS as f
# string = f.stripQuotes(string)
def stripQuotes(string):
    return str(string).strip('"').strip("'")


# import FUNCTIONS as f
# string = f.strip1(string)
def strip1(string):
    string = stripQuotes(stripWhitespace(string))
    return string


#------------------------

# import FUNCTIONS as f
# TrueFalse = isString(string)
def isString(string):
    if isinstance(string, str):
        return True
    else:
        return False

# import FUNCTIONS as f
# numTimesFound = f.isStringFound(content="1-2-3-4", findMe='4')
def isStringFound(content="1-2-3-4-5-6-7-8-9", findMe='find me'):
    #print(f"'{findMe}' in - {content}")
    #content = "1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-"
    timesItsFound = content.count(findMe)
    #print(f"timesItsFound: {timesItsFound}")
    return timesItsFound

# import FUNCTIONS as f
# f.someSpace(linesOfSpace=3)
def someSpace(linesOfSpace = 3):
    for i in range(linesOfSpace):
        print("")
#------------------------

# import FUNCTIONS as f
# f.saveHTMLfile(html, filename="ephe/save.html")
def saveHTMLfile(html, filename="ephe/save.html"):
    file = open(filename, "w")
    file.write(html)
    file.close()


# import FUNCTIONS as f
# f.round_down(5.75)
def round_down(n, decimals=0):
    import math
    multiplier = 10 ** decimals
    result = math.floor(n * multiplier) / multiplier
    return int(result)

# import FUNCTIONS as f
# f.collapseArray(array, "/")
def collapseArray(array, joinChar="/"):
    string = joinChar.join(array)
    return string

# import FUNCTIONS as f
# f.joinArray(array, "/")
def joinArray(array, joinChar="/"):
    string = joinChar.join(array)
    return string



# import FUNCTIONS as f
# f.round(5.75) # (1) 5.75 -> 6 / (2) 5.1 -> 5
def round(n):
    return roundUpOrDown(n)


# import FUNCTIONS as f
# f.roundUpOrDown(5.75) # (1) 5.75 -> 6 / (2) 5.1 -> 5
def roundUpOrDown(n):
    n0 = float(n) #might have decimal fraction
    n1 = int(n0) #rounded down to int number
    #decimal part
    d = n0 - n1 #0.? - the decimal - less than 1
    num_rounded_up_or_down = 0
    # -rounds it up-
    if d>=.5:
        num_rounded_up_or_down = n1+1
    # -rounds it down-
    else:
        num_rounded_up_or_down = n1

    return num_rounded_up_or_down


# import FUNCTIONS as f
# f.round_down2(5.75)
def round_down2(n, decimals=2):
    n = float(n)
    import math
    multiplier = 10 ** decimals
    result = math.floor(n * multiplier) / multiplier
    return float(result)

# import FUNCTIONS as f
# f.round_down1(5.75)
def round_down1(n, decimals=1):
    n = float(n)
    import math
    multiplier = 10 ** decimals
    result = math.floor(n * multiplier) / multiplier
    return float(result)


# import FUNCTIONS as f
# f.round_down4(5.7575)
def round_down4(n, decimals=4):
    n = float(n)
    import math
    multiplier = 10 ** decimals
    result = math.floor(n * multiplier) / multiplier
    return float(result)


#-----------------------------


# import FUNCTIONS as f
# f.print2(array)
def print2(array):  # PRETTY PRINT - Dicts that are complex
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(array)

# import FUNCTIONS as f
# f.print3(array,varName)
def print3(array,varName):  # PRETTY PRINT - Dicts that are complex
    print(f"{varName}: ({len(array)}):")


# import FUNCTIONS as f
# f.print4(array)
def print4(array,varName):  # PRETTY PRINT - Dicts that are complex
    import FUNCTIONS as f
    print(f"{varName}: ({len(array)}):")
    f.printRows(array,varName)
    print(f"{varName}: ({len(array)}):")
    print("")


# when you want to print a list - with separation between the rows - to make it readable

# import FUNCTIONS as f
# f.printRows(list)
def printRows(list,varName="var"):  # ... numbers the rows as well
    c = 0
    for one in list:
        print(f"\n{c})  {varName}: ({len(one)}):  {one}")
        c += 1

#-----------------------------


"""
function keep_only_certain_planets($array){
  look --> $planets_to_keep = array("Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","Chiron","Juno","Ceres","Pallas","Vesta","Eros","Amor","Lilith","Sappho","SaturnChironMidpoint");
  
  //print_r($planets_to_keep);die();
  foreach($array as $planet=> $value){
    if(in_array($planet, $planets_to_keep)){
      $array2[$planet] = $value;
    }
  }
  return $array2;
}
"""





#-------------------------------


# import FUNCTIONS as functions
# docRoot = functions.myDocumentsRoot()

def myDocumentsRoot():
  import os
  homePath = os.path.expanduser('~')  # 'C:\\Users\\yagisanatode'
  return homePath



#--------------------------

# import FUNCTIONS as functions
# homeRoot = functions.homeFolderRoot()

def homeFolderRoot():
  from pathlib import Path
  homeFolder = Path.home()
  print(homeFolder) # C:\Users\myvor
  return homeFolder




#import FUNCTIONS as f
#status = f.fileExists(thumbImgPath)
#
#if status == True:
  #print("file exists")
#elif status == False:
  #print("file doesn't exist")

def fileExists(file):
  from pathlib import Path
  myFile = Path(file)
  if myFile.is_file():
    # file exists
    return True
  else:
    return False






"""

DICTS

# original:

new_dict = {}
print(f"new_dict: {new_dict}")
#output: new_dict: {}
new_dict[1] = {}
print(f"new_dict: {new_dict}")
#output: new_dict: {1: {}}
new_dict[1][2] = 5
print(f"new_dict: {new_dict}")
#output: new_dict: {1: {2: 5}}
"""



