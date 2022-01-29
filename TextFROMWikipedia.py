#v2

#import TextFROMWikipedia as ptxt
#text = ptxt.PlainTextFromWikipediaURL("https://en.wikipedia.org/wiki/Brewing",True,False)
#text = ptxt.PlainTextFromWikipediaURL("https://en.wikipedia.org/wiki/Brewing",False,False)
#print(text)

# Required:
# pip install requests, bs4, lxml

def PlainTextFromWikipediaURL(link="",return_summary=True,open_in_browser_too=True):
    # Hear a Wikipedia Article READ TO YOU by running a python script!
    print("\nRead a URL with python!\n")  # https://en.wikipedia.org/wiki/Brewing
    print("\nRead a Wikipedia URL with python!\n")  # https://en.wikipedia.org/wiki/Brewing

    import platform
    pl = platform.system()
    if pl == "Linux":
        print("The PlainTextFromURL is not set up for Linux yet")
    if pl=="Windows":
        #print("You're using Windows")
        if link=="":
            link = "https://en.wikipedia.org/wiki/Brewing"

        import requests
        #get that url loaded from the link as html
        f_html = requests.get(link)
        #print(f_html.text)

        from bs4 import BeautifulSoup
        f_html.encoding = 'utf-8' # Optional: requests infers this internally
        soup = BeautifulSoup(f_html.text, 'lxml')
        #
        #to get all links:
        #content = soup.find_all('a')
        # ------------------------------
        #just getting the content in <div id='content'></div>
        html_content_str = soup.find("div", {"id": "content"})
        #print("html_content_str")
        #print(html_content_str)

        #converting it to text - & stripping the html tags out
        soup = BeautifulSoup(html_content_str.text, 'lxml')
        #RESULT IS GOOD TEXT ONLY:
        text_only = soup.get_text()
        # BUT FIRST - let's remove repetitive things

        #remove from that string, certain phrases - I don't want to hear each time:
        #Jump to navigation
        #Jump to search
        text_only = text_only.replace("Jump to navigation", "").replace("Jump to search", "").replace("From Wikipedia, the free encyclopedia", "Reading from Wikipedia").replace("\n\n\n", "\n")

        plain_text_readable = text_only

        if return_summary!=True:
            #--Reads the WHOLE ARTICLE:--
            #print(plain_text_readable)
            return1 = plain_text_readable
        else:
            #--Reads the FIRST 500 CHARS:--
            summary500 = plain_text_readable[0:500]
            #print(summary500) #print only 1st chars of text from html - testing
            return1 = summary500
        #OPENS THE PAGE ALSO in a browser - while reading it to you

        #opens the browser - if desired
        if open_in_browser_too==True:
            import webbrowser
            webbrowser.open_new(link)

        #return the content
        return return1

