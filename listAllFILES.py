



# import listAllFILES as f
# states = f.returnStates()
def returnStates():
    import FUNCTIONS as f
    import OPENsomething as o
    import ASTROLOGYfunctions as aa
    peopleCSV = aa.pdnaBankGetMyPeopleCSV_BirthchartStuff()

    #print(f"peopleCSV: {peopleCSV}")
    #exit()
    #print("change the filename to a thumbnail filename - save the name too for captions")
    c=0
    states = []
    for person in peopleCSV:
        #print(f"person {c}): {person}")
        c += 1
        state = person[2].strip('"')
        #print(f"state {c}): {state}")

        states.append(state)
    #print(f"nameImgs ({len(nameImgs)}): {nameImgs}")
    return states



# import listAllFILES as f
# nameImgs = f.returnNameImgs()
def returnNameImgs(): # a [] list of ... name, thumbImgPath
    import FUNCTIONS as f
    import OPENsomething as o
    import ASTROLOGYfunctions as aa

    peopleCSV = aa.pdnaBankGetMyPeopleCSV()

    #print(f"peopleCSV: {peopleCSV}")
    #print("change the filename to a thumbnail filename - save the name too for captions")
    c=0
    nameImgs = []
    for person in peopleCSV:
        name = person[0].replace('"',"")
        #print(f"person {c}) : {name} - {person}")
        c += 1
        imgPath = person[1]
        i = imgPath.replace("1000000001/",""). split("/")
        filename = i[len(i)-1]
        filename = filename.replace('"',"") # th  s was stopping it, there was a " at the end of the file
        filename2 = filename[:-4]  # re  oves the file extension
        fileExt = filename[-4:]  # gi  es only the extension with the '.' dot
        # imgPath = imgPath.replace(filename,"") #no filename on it - just the path
        thumbImgPath = "mycosmicdna/pics/thumbnails" + "/" +filename2+fileExt
        #print(f"thumbImgPath: {thumbImgPath}")
        nameImg = name, thumbImgPath
        nameImgs.append(nameImg)
    #print(f"nameImgs ({len(nameImgs)}): {nameImgs}")
    return nameImgs



# import listAllFILES as f
# f.getAfewImagesPdnaBank()

def getAfewImagesPdnaBank():
    import listAllFILES as f
    folder_path = "mycosmicdna/pics/thumbnails" #slashes need to be to the right
    filenamesThumbs = f.listAllThumbnails(folder_path)
    print(f"filenamesThumbs: {len(filenamesThumbs)}")
    count=1
    for thumb in filenamesThumbs:
        print(f"thumb: {thumb}")
        if count==10:
            break
        count += 1




# import listAllFILES as filelist
# folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
# files = filelist.listAllImages(folder_path)

#does not get thumbnails
def listAllImages(dir):
    # new list files - all photos - specific file extensions
    # def listAllFilesWithExtensions(dir,list=['.jpg','.png','gif']):
    import os
    #dir = "z-IMAGES_1"
    files = []
    for dirname, dirnames, filenames in os.walk(dir):  # "."
        # print(f"dirname ({dirname})")
        # print(f"dirnames ({len(dirnames)})")
        # print(f"filenames ({len(filenames)}):")
        for filename in filenames:
            file = os.path.join(dirname, filename)
            if ".jpg" in file or ".gif" in file or ".png" in file:
                if "__thumbnail" in file:
                    pass #do nothing
                else:
                    # print(f"file: {file}")
                    files.append(file.replace("/","\\").replace("\\","/"))

    #print(f"\n\nfiles ({len(files)})")
    return files


# import listAllFILES as f
# folder_path = "mycosmicdna\pics\thumbnails"
# folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
# filenamesThumbs = f.listAllThumbnails(folder_path)
#count=1
#for thumb in filenamesThumbs:
    #print(f"thumb: {thumb}")
    #if count==7:
        #break
#does not get thumbnails
def listAllThumbnails(dir):
    # new list files - all photos - specific file extensions
    # def listAllFilesWithExtensions(dir,list=['.jpg','.png','gif']):
    import os
    #dir = "z-IMAGES_1"
    files = []
    for dirname, dirnames, filenames in os.walk(dir):  # "."
        # print(f"dirname ({dirname})")
        # print(f"dirnames ({len(dirnames)})")
        # print(f"filenames ({len(filenames)}):")
        for filename in filenames:
            file = os.path.join(dirname, filename)
            if ".jpg" in file or ".gif" in file or ".png" in file:
                if "__thumbnail" in file:
                    file = file.replace("\\","/")
                    # print(f"file: {file}")
                    files.append(file)
                else:
                    pass

    #print(f"\n\nfiles ({len(files)})")
    return files


#the files - numbered come back funny
# - out of order, unless force a 3-4 digit 0 before the number
# - in case the number of frame images gets too large

# import listAllFILES as filelist
# folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
# filenamesOnly = filelist.listFilenameOnly(folder_path)

def listFilenameOnly(folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"):
    # get filenames only
    import listAllFILES as lfs
    folder_path = "z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
    array = lfs.listAllFILES(folder_path)
    length = array[0]
    pics = array[1]
    filenames = []
    for picPath in pics:
        print(f"remove path from: {picPath}")
        line = picPath.split("\\")
        filename = line[len(line) - 1]  # last entry - of path - is filename
        filenames.append(filename)
        print(f"filename-only: {filename}")
    return filenames



#new list files - all photos - specific file extensions





#v1
"""
lists all files
- relative to (from WITHIN) the python project folder
"""
"""
#Change the background automatically
import listAllFILES as filelist
folder_path="z-IMAGES_1/0.cool"
array = filelist.listAllFILES(folder_path)
length = array[0]
pics = array[1]

import BackgroundChooseRANDOM as files
files.BackgroundChooseRANDOM(array)
"""
def listAllFILES(folder_name):
    #print("Going to list all files!")

    import os, sys
    project_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    #print("Hello, here is the project_path: " + project_path)
    #print("Hello, here is the folder_path: " + folder_path)
    paths_joined = os.path.join(project_path, folder_name)
    #print("Hello, here is the paths_joined: " + paths_joined)
    #print("\n------------------------------\n")

    pics = [] #empty list
    for path, subdirs, files in os.walk(paths_joined):
        for name in files:
            pic = os.path.join(path, name)
            #print(pic)
            pics.append(pic)
    print("Files LIST:")
    print("Number of files in the list = ", len(pics))
    print(pics)
    return pics




# import listAllFILES as files
# folder_path = "z-Frames"
# dirnames, filenames = anotherWay1(folder_path)
"""
import listAllFILES as files
folder_path = "z-Frames"
dirnames, filenames = files.anotherWay1(folder_path)
filenames = sorted(filenames)
print(str(len(filenames))+" filenames:")
print(filenames)
"""


def anotherWay1(folder_name="folder_name"):
    import os
    import sys
    # it fills up dirnames, and filenames - with all the folders, and seperate files
    # from os import walk
    project_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    paths_joined = os.path.join(project_path, folder_name)
    f = []
    for (dirpath, dirnames, filenames) in os.walk(paths_joined):
        f.extend(filenames)
        break
    # print (dirnames)
    # print (filenames)
    both = dirnames, filenames
    return both