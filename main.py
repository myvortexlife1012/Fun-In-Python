
# make exe for the background change app
# pip install auto-py-to-exe # type 'auto-py-to-exe' in the console ... gui appears



# import OpenAFileOrFolder as opn
# filepath = r"C:\Users\myvor\Pictures\0.animals\beautiful tiger wallpapers\!image18.jpg"
# opn.openFileWithDefaultProgram(filepath)



"""
import AllWINDOWS as wins
wins.whereMouseClicks()
"""

"""
import ctypes
window = ctypes.windll.user32.GetForegroundWindow()
print("window:")
print(window)
"""

"""
import AllWINDOWS as wins
windows = wins.arrayOfWindowsVisible()
print(f"windows ({len(windows)}):")
print(windows)
"""


#import GuiAPPs as guiApps
#guiApps.guiBGchangeShow()

# import win32gui
# pip install win32gui



"""
import AllWINDOWS as wins
#needs win32gui - python 3.6 env
windows = wins.arrayOfWindows()
print("windows:")
print(windows)"""


#windows:
# [{'x': 1314, 'y': 120, 'w': 207, 'h': 42, 'name': 'FastStone Capture'},
# {'x': 338, 'y': 151, 'w': 1180, 'h': 656, 'name': 'pythonProject – AllWINDOWS.py'},
# {'x': 376, 'y': 51, 'w': 1103, 'h': 678, 'name': 'New Tab - Brave'},
# {'x': 34, 'y': 78, 'w': 334, 'h': 540, 'name': 'Calculator'},
# {'x': 179, 'y': 179, 'w': 895, 'h': 518, 'name': 'C:\\Windows\\system32\\cmd.exe'},
# {'x': 478, 'y': 73, 'w': 1038, 'h': 712, 'name': 'Settings'},
# {'x': 77, 'y': 77, 'w': 1152, 'h': 598, 'name': 'QTrayIconMessageWindow'},
# {'x': 505, 'y': 190, 'w': 526, 'h': 422, 'name': 'mbamtray'},
# {'x': 26, 'y': 26, 'w': 1152, 'h': 598, 'name': 'QTrayIconMessageWindow'},
# {'x': 128, 'y': 128, 'w': 1152, 'h': 598, 'name': 'MS_WebcheckMonitor'}]


#import GuiAPPs as guiApps
#guiApps.guiBGchangeShow()
# guiApps.GuiWindowLAYOUTSshow()
# guiApps.GuiWithImageBUTTONSshow()


#make an invisible right arrow that changes the background to a similar but different one
"""
import ctypes
from ctypes import wintypes
user32 = ctypes.windll.user32
h_wnd = user32.GetForegroundWindow()
print("h_wnd: ")
print(h_wnd)
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
print("pid.value: ")
print(pid.value)
"""
# python windows get window dimensions - of active window, of a draggable area - maybe menu area
# python windows mouse drag


#import AllWINDOWS as wins
#wins.moveMouseTO(500,50,"FAST")


"""

import GuiAPPs as guiApps
guiApps.guiBGchangeShow()
# guiApps.GuiWindowLAYOUTSshow()
# guiApps.GuiWithImageBUTTONSshow()
"""

#---------------
# a button that runs this code:
"""
#Change the background automatically
import listAllFILES as lfs
folder_path="z-IMAGES_1/0.cool/premium_wallpapers_rock_stacks" #folder_path="z-IMAGES_1/0.cool"
array = lfs.listAllFILES(folder_path)
length = array[0]
pics = array[1]

#keep it in the same folder of images - so it feels consistent
import BackgroundChooseRANDOM as bgcrand
bgcrand.BackgroundChooseRANDOM(array)
"""



"""
import KeyLOGGER as keyLogger
keyLogger.keyLogger2Start()
"""