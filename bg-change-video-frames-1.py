# pyinstaller --onefile bg-change-video-frames-1.py # makes the exe file (in dist folder)

# --------------------------------------------
# DESKTOP WALLPAPER - VIDEO WALLPAPER (simulates)
#
import listAllFILES as lfs
folder_path="z-Frames/beach_with_rocks"
array = lfs.listAllFILES(folder_path)
pics = array[1]
print(str(len(pics))+" pics")

import BackgroundCHOOSE as bkng
while True: #keep playing it on the screen
    bkng.BackgroundSequenceChange(array,speed=.25)# speed is time to sleep between

# --------------------------------------------
