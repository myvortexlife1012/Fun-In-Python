# uses listAllFILES - to get full paths of all pics available


#keeps playing the video now
"""
import listAllFILES as lfs
folder_path="z-Frames"
array = lfs.listAllFILES(folder_path)
length = array[0]
pics = array[1]
print(str(len(pics))+" pics")
print(pics)

import BackgroundCHOOSE as bkng
while True: #keep playing it on the screen
    bkng.BackgroundSequenceChange(array)
"""

def BackgroundSequenceChange(listALlFILES_array,speed=1):
    import BackgroundCHOOSE as b
    import time
    import ctypes
    import os
    import platform
    pl = platform.system()

    length = len(listALlFILES_array)
    print(f"length: {length}")
    prePath = "C:/Users/myvor/PycharmProjects/pythonProject/"
    for i in range (length):
        filename = prePath+"z-Frames/beach_with_rocks/frame-"+str(i)+".jpg"
        print(filename)

        #print("going to switch to it-in a sequence later")

        # import BackgroundCHOOSE as b
        b.setDesktopBackground(filename)

        time.sleep(speed)





# v1

#import BackgroundCHOOSE as bkng
# bkng.BackgroundChooseRANDOM(listALlFILES_array)

def BackgroundChooseRANDOM(listAllFILES_array):
    import BackgroundCHOOSE as b
    length = len(listAllFILES_array)
    filenames = listAllFILES_array

    import random
    rand_num = random.randint(0, length-1)
    print(f"Random number chosen - From Backgrounds - ({rand_num}) - from total ({length}) ", )
    filename = filenames[rand_num]
    filename = filename.replace("/","\\")
    print("\nfilename is: ", filename)

    # import BackgroundCHOOSE as b
    b.setDesktopBackground(filename)


# import BackgroundCHOOSE as bkng
# bkng.setDesktopBackground(filename)
# filename = "z-IMAGES_1\0.cool\!new1\whales_sunset\mountain_photography.jpg"

def setDesktopBackground(filename="file.jpg"):
    if "z-IMAGES_1" in filename:
        if "pythonProject" in filename:
            pass
        else:
            filename = "C:\\Users\\myvor\\PycharmProjects\\pythonProject\\" + filename

    import platform
    pl = platform.system()

    #for windows
    if pl == 'Windows':
        import ctypes
        SPI_SETDESKWALLPAPER = 0x14  # which command (20)

        SPIF_UPDATEINIFILE = 0x2  # forces instant update
        src = r""+filename+""  # full file location
        # in python 3.4 you have to add 'r' before "path\img.jpg"

        print(ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE))

    #for UBUNTU Linux
    #current_background1 = "gsettings get org.gnome.desktop.background picture-uri"
    #current_background = os.system("gsettings get org.gnome.desktop.background picture-uri")

    #change the background
    #filename = filename (spaces = '%20')

    #from urllib.parse import quote
    #filename = quote(filename)
    #image_filename = "premium wallpapers sunrises (1).jpg"
    if pl=='Linux':
        string = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+filename
        #print("\n\n"+string)
        import os
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+filename)

