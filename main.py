import mymodule
mymodule.greeting("Mike")




import ASTROLOGYmagi as m
import FUNCTIONS as f
import ASTROLOGYfunctions as aa




# do today
#aa.theFinanceParallels("g","g") # do today











import GuiAPPs as g
#g.chartWheel()



# create a midpoint chart - with just planet Uranus - tech stock indicator
me = aa.me()
#planets = me['planets']['360']
#look for mean Node or North Node - South Node
#f.print2(planets)
#print("looking for NorthNode_g - SouthNode_g")


#-------------------

#during the calculations, it may use floats - that increase the value
#powerNum = aa.powerFor(me, aspect_string="Sun-Conjunct-Jupiter")
#print(f"powerNum: {powerNum}")

#powerNum = aa.powerFor(me, aspect_string="Sun-Conjunct-Pluto")
#print(f"\npowerNum: {powerNum}")

#powerNum = aa.powerFor(me, aspect_string="Sun-Quincunx-Chiron")
#print(f"\npowerNum: {powerNum}")

#powerNum = aa.powerFor(me, aspect_string="Venus-Conjunct-Uranus")
#print(f"\npowerNum: {powerNum}")


#----------------------


#orb, orbMax = aa.getOrb(me, aspect_string="Sun-Conjunct-Jupiter")
#print(f"orb: {orb}, orbMax: {orbMax}")

#orb, orbMax = aa.getOrb(me, aspect_string="Sun-Conjunct-Pluto")
#print(f"orb: {orb}, orbMax: {orbMax}")

#orb, orbMax = aa.getOrb(me, aspect_string="Sun-Quincunx-Chiron")
#print(f"orb: {orb}, orbMax: {orbMax}")


import requests








#I'm going to run this - and it could take a coule days - I'm not sure how long




# load the html for swetest - and download all of the asteroid files
# create a mirror of all of the files, in a folder
mirrorPath = "C:/Users/myvor/PycharmProjects/pythonProject/ephe"
url = "http://www.astro.com/ftp/swisseph/ephe/"
base_url = url

firstFile = "!index.html"
#then each folder - has an .html file downloaded
folder1Name = "ast0" # ast0.html
folderPathFull = mirrorPath +"/"+ folder1Name
html_file = folder1Name+".html"
html_fullpath_file = mirrorPath +"/!html/"+ html_file
save_fullpath = mirrorPath +"/"+ folder1Name
save_fullpath_first = mirrorPath
open_fullpath_first_file = mirrorPath +"/!html/"+ firstFile
save_fullpath_first_file = mirrorPath
add_to_url = folder1Name
full_url_path = url + add_to_url

#print(f"save_fullpath_first: {save_fullpath_first}") # C:/Users/myvor/PycharmProjects/pythonProject/ephe/ast0.html
print(f"open_fullpath_first_file: {open_fullpath_first_file}") # C:/Users/myvor/PycharmProjects/pythonProject/ephe/ast0.html
#print(f"html_fullpath_file: {html_fullpath_file}") # C:/Users/myvor/PycharmProjects/pythonProject/ephe/ast0.html
#print(f"save_fullpath: {save_fullpath}") # C:/Users/myvor/PycharmProjects/pythonProject/ephe/ast0
#print(f"full_url_path: {full_url_path}") # http://www.astro.com/ftp/swisseph/ephe/ast0



# strip out all of the folders - just process files

links = f.getLinks(open_fullpath_first_file) # save first files to mirrorPath
#print(f"\nlinks ({len(links)}):")
#f.print2(links)

fileLinks = []
folderLinks = []
for link in links:
    if "/" in link:
        link2 = link.replace("/","")
        folderLinks.append(link)
    elif "=" in link:
        pass
    else:
        fileLinks.append(link)


# there's a .html file for each folderLinks - of first file !index.html
print(f"\nfolderLinks ({len(folderLinks)}):")

print(f"\nfileLinks ({len(fileLinks)}):")
#f.print2(fileLinks)

#link = fileLinks[0]
#print(f"\nlink: {link}")


total = len(folderLinks)
c = 0
# there's a .html file for each folderLinks
for folderName in folderLinks:
    if "ftp" in folderName or "archive" in folderName or "=" in folderName:
        pass
    else:
        folderName0 = "http://www.astro.com/ftp/swisseph/ephe/"+folderName.replace("/","")
        folderName1 = "ephe/"+folderName.replace("/","")
        folderName2 = "ephe/!html/"+folderName.replace("/","")
        folderName3 = folderName2 + ".html"
        print (f"{c}/{total}) folderName3: {folderName3}")
        links = f.getLinks(folderName3)
        #remove the nonsense:  # '?C=N;O=D', '?C=M;O=A', '?C=S;O=A', '?C=D;O=A', '/ftp/swisseph/ephe/'
        links.pop(0) # '?C=N;O=D'
        links.pop(0) # '?C=M;O=A'
        links.pop(0) # '?C=S;O=A'
        links.pop(0) # '?C=D;O=A'
        links.pop(0) # '/ftp/swisseph/ephe/'
        # removed ... left with filenames, 'readme.txt', 'se44000s.se1', 'se44001s.se1'
        print(f"{c}/{total}) links ({len(links)}): {links}")
        l=0
        for link in links:
            url_base = folderName0
            folder_base = folderName1
            #---------------------------
            full_url_path_link = url_base +"/"+ link
            save_path_link = folder_base +"/"+ link
            f.folder(folder_path=folder_base) # makes a folder if not there yet
            #print(f"{c}/{total})/{l}/{len(links)} link: {link}")
            #print(f"{c}/{total})/{l}/{len(links)} full_url_path_link: {full_url_path_link}")
            #print(f"{c}/{total})/{l}/{len(links)} save_path_link: {save_path_link}")
            print(f" {c}/{total}) / {l}/{len(links)} ... {full_url_path_link} - saving to: {folder_base} )")
            #print(f"f.readAndSaveBinaryFileFromUrl( '{full_url_path_link}', save_to_path='{folder_base}' )")
            if f.fileExists(save_path_link)==False: #only download once 1x
                f.readAndSaveBinaryFileFromUrl(full_url_path_link, save_to_path=folder_base) # "ephe"

            l += 1
        c += 1


exit()



# --set up the synastry other function--
# aa.csvSelfMagiAspects264_3(me, type="self", showLines=True, showOnlyMatches=True) #True
#aa.csvSelfMagiAspects264_3(me, type="self", showLines=True, showOnlyMatches=True) #True
# -------------------------------------
# --- DO THIS --
# make sure the aspects are correctly processed - with cat/cat|m ... etc...
# --- DO THIS --
# -------------------------------------
# longer_diff, shorter_diff = aa.diffByAspectString(me, aspect_string)



#check that the double/cats - are registering power correctly




# import ASTROLOGYfunctions as aa

"""
# INDIVIDUAL ASPECT -- GETTING BOTH DIFF DEGREES, long and short difference
aspect_string = "Neptune-Quincunx-Chiron"
longer_diff, shorter_diff = aa.diffByAspectString(me, aspect_string)
print(f"aspect_string: {aspect_string}")
print(f"longer_diff: {longer_diff}, shorter_diff: {shorter_diff}")
"""




"""
planets30 = me['planets']['30']
#print(f"planets30 ({len(planets30)}):")
#f.print2(planets30)
planets30_g = []
for planet in planets30:
    if "_g" in planet:
        planets30_g.append(planet)
print(f"planets30_g ({len(planets30_g)}):")
f.print2(planets30_g)
"""



#create midpoints of all the planets in _g
# loop twice on the planets, but only use first loop as first person
# it will create
# use both the near and far midpoints _n, _f
# 2nd time - when it's done with the sun, the next time, skip the sun, so the moon goes first
# 3rd time - Mercury goes first - and it skips the last 2 # to avoid duplication
# - and in the 2nd planet loop -> then start at that place in the 2nd planet you add - so skip the Sun and Moon 1st
#-----------
# OUTPUT 1st: create the list so I can put Drama or Luck on it
# - create the dictionary that I need to fill in
#-----------



