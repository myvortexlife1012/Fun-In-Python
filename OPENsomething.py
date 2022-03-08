



# import OPENsomething as o
# o.openURLinBrowser(url="http://wikipedia.org")
def openURLinBrowser(url="http://wikipedia.org"):
    import sys, os, subprocess
    if sys.platform=='win32':
        os.startfile(url)
    elif sys.platform=='darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            subprocess.Popen(['xdg-open', url])
        except OSError:
            print ('Please open a browser on: '+url)








#---------------------------------



# Save the page as the keys that make it unique - filename
# Parse this with BeautifulSoup

# https://serennu.com/astrology/ephemeris.php?inday=12&inmonth=10&inyear=1981&inhours=03&inmins=06&insecs=00&insort=pname&z=t&gh=g&addobj=3%2C+2060&inla=39n05&inlo=94w34&h=P
def demoReadingWritingAndReading():
    import requests

    # Define a variable to contain a web page URL.
    web_page_url = "https://serennu.com/astrology/ephemeris.php?inday=12&inmonth=10&inyear=1981&inhours=03&inmins=06&insecs=00&insort=pname&z=t&gh=g&addobj=&inla=39n05&inlo=94w34&h=P"
    filename = "1981-10-12--03-06--39n05-94w34.html"

    # Add a User-Agent header to simulate a real web browser to send the requests. The User-Agent header should be saved in a dictionary object.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    # Make an HTTP get requests to the webserver by the requests module get method, and the get method returns a response object.
    response = requests.get(url=web_page_url, headers=headers)
    # Get the request web page text content by the response.text attribute.
    page_content = response.text
    # Print out the text to verify it is correct.
    print(page_content)
    # Write the web page content to a local file to save it.
    with open(filename, 'w', encoding='utf8') as fp:
        fp.write(page_content)

    print('Save web page content successfully: ' + web_page_url)
    # Save web page content http://www.google.com successfully.
    # Read the local file content to verify it is the web page content.
    # Open the local file with read permission.
    with open(filename, 'r', encoding='utf8') as fp:
        line = fp.readline()  # read one line text.

        # Only when the read-out text's length is 0 then quit the loop.
        while len(line) > 0:
            print(line)

            # read the next line.
            line = fp.readline()




# import OPENaFileOrFolder as opn
# filepath = r"C:\Users\myvor\Pictures\0.animals\beautiful tiger wallpapers\!image18.jpg"
# folderpath = r"C:\Users\myvor\Pictures\0.animals\beautiful tiger wallpapers" #it opens folders in windows explorer
# -- OPENS A PROGRAM and a FILE - the default assigned to the file type
# opn.openFileWithDefaultProgram(filepath)
# -- OPENS AN EXPLORER WINDOW - to show you the folder
# opn.openFileWithDefaultProgram(folderpath)

# Note: this would open the brave browser - to open the html for the images - after it completes generating it
# Note: it would double click the html file

def openFileWithDefaultProgram(filepath=""):
    #this opens a file - like Double-Clicking on it
    #it opens with the default program
    if filepath=="":
        filepath = r"C:\Users\myvor\Pictures\0.animals\beautiful tiger wallpapers\!image18.jpg"
    print(filepath)
    import subprocess, os, platform
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))





"""
working with python and paths:
----------
you can use always:

'C:/mydir'
this works both in linux and windows. Other posibility is

'C:\\mydir'
if you have problems with some names you can also try raw string literals:

r'C:\mydir'
however best practice is to use the os.path module functions that always select the correct configuration for your OS:

os.path.join(mydir, myfile)
From python 3.4 you can also use the pathlib module. This is equivelent to the above:

pathlib.Path(mydir, myfile)

https://stackoverflow.com/questions/2953834/windows-path-in-python

"""

