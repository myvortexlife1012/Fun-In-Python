
# import AllWINDOWS as wins
# wins.OpenProgramByStartMenu2()
# wins.mouseAndKeysListen1()
# wins.mouseAndKeysListen2() #outputs per pixel mouse movements
# wins.mouseInCircle() #circles the start menu button
# wins.moveMouseTO(500,50,"FAST")
# wins.mousePositionLOOP()
# point = wins.mousePosition()
# wins.screenSizeOS()
# wins.moveWindowsByName()
  # take where window is and move it around a bit
  # take where window is, and it's width and height, and click a button on it
#needs win32gui - python 3.6 env
# wins.allWindowsPIDsAndTitles() # ctypes
# windows = wins.arrayOfWindows() #returns array of the windows
# windows = wins.arrayOfWindowsVisible()





# import AllWINDOWS as wins
# wins.mouseInCircle()

#circles the windows start button - right now
def mouseInCircle():
    # circles the start menu button
    def mouseInCircle():
        # mouse goes in a circle:
        import pyautogui
        import math

        # Radius
        R = 30  #
        # measuring screen size
        (x, y) = pyautogui.size()
        print("pyautogui.size()")
        print(pyautogui.size())
        # locating center of the screen
        # pyautogui.position(x/2,y/2)
        # locating the start menu button in Windows 10
        (X, Y) = 40, y - 35
        # offsetting by radius
        pyautogui.moveTo(X + R, Y)

        # drawing the circle
        for i in range(410):  # 360=full circle, more-it keeps going
            # setting pace with a modulus
            # smaller radius - make this larger - to seem more natural
            if i % 12 == 0:  # skips some pixels in the mouse moves
                pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
        pyautogui.moveTo(X, Y)






# import AllWINDOWS as wins
# wins.OpenProgramByStartMenu2()
def OpenProgramByStartMenu2(program="Firefox"):
    import pyautogui
    import time
    #check it's windows
    import platform
    pl = platform.system()
    #for windows Only - START MENU
    if pl == 'Windows':
        print(f"Going to open: {program} ...")
        #click on start menu
        print("click on start menu")
        #get the screen height - 50 less than height
        #import AllWINDOWS as wins
        OSwidth, OSheight = screenSizeOS() # OS Window Size: # Size(width=1920, height=1080) - pyautogui
        x, y = 20, OSheight-20
        #pyautogui - clicks
        pyautogui.click(x, y)
        #sleep for 1/2 sec
        print("sleep for 1/2 sec")
        time.sleep(0.5)
        #type 'firefox' type '\n' #presses enter
        print("type the program and press enter")
        pyautogui.typewrite(program)
        time.sleep(1)
        pyautogui.typewrite('\n')


# import AllWINDOWS as wins
# wins.OpenProgramByStartMenu()
def OpenProgramByStartMenu(program="Firefox"):
    import pyautogui
    import time

    def msg(n, phrase):
        print(phrase)

    # Printing basic message
    msg(1, f'Opening {program}...')

    # Location the start button
    _start_button_ = pyautogui.locateOnScreen('images/start_button.png')
    _location_ = pyautogui.center(_start_button_)

    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Opened start menu successfully!')
    else:
        msg(3, 'Failed to open start menu!')
        exit()

    time.sleep(0.5)

    # Search for Firefox in the menu search
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')

    # Print message
    msg(1, 'Firefox is now open and running.')





# import AllWINDOWS as wins
# wins.mouseAndKeysListen1()
def mouseAndKeysListen1():
    from pynput.keyboard import Listener as KeyboardListener
    from pynput.mouse import Listener as MouseListener
    from pynput.keyboard import Key
    import logging
    logging.basicConfig(filename=("keylog.mouse.keys.log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def end_rec(key):
        print(key)
        logging.info(str(key))

    def on_press(key):
        print(key)
        logging.info(str(key))

    def on_move(x, y):
        print("Mouse moved to ({0}, {1})".format(x, y))
        logging.info("Mouse moved to ({0}, {1})".format(x, y))

    def on_click(x, y, button, pressed):
        if pressed:
            print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

    def on_scroll(x, y, dx, dy):
        print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
        logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

    with MouseListener(on_click=on_click, on_scroll=on_scroll) as listener:
        with KeyboardListener(on_press=on_press) as listener:
            listener.join()



# import AllWINDOWS as wins
# wins.mouseAndKeysListen2() #outputs per pixel mouse movements

#outputs per pixel mouse movements
def mouseAndKeysListen2():
    from pynput.keyboard import Listener as KeyboardListener
    from pynput.mouse import Listener as MouseListener
    from pynput.keyboard import Key
    import logging
    logging.basicConfig(filename=("keylog.mouse.keys.log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def end_rec(key):
        print(key)
        logging.info(str(key))

    def on_press(key):
        print(key)
        logging.info(str(key))

    def on_move(x, y):
        print("Mouse moved to ({0}, {1})".format(x, y))
        logging.info("Mouse moved to ({0}, {1})".format(x, y))

    def on_click(x, y, button, pressed):
        if pressed:
            print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

    def on_scroll(x, y, dx, dy):
        print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
        logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

    # ', on_move=on_move'
    # outputs per pixel mouse movements
    with MouseListener(on_click=on_click, on_scroll=on_scroll, on_move=on_move) as listener:
        with KeyboardListener(on_press=on_press) as listener:
            listener.join()




# import AllWINDOWS as wins
# wins.whereMouseClicks()

"""
Left ... mouse.Button.left ... x,y: 1485,117
right ... mouse.Button.right ... x,y: 1523,116
Left ... mouse.Button.left ... x,y: 1505,118
Left ... mouse.Button.left ... x,y: 1621,157
Left ... mouse.Button.left ... x,y: 1621,157
"""

#mouse - on click - print where it clicked
def whereMouseClicks():#keylogger_mouse.txt
    import os
    import time
    import re
    from pynput import mouse
    from pynput.keyboard import Key, Listener
    f = open('keylogger_mouse.txt', 'a')

    inc = 1
    f.write('<mouse_new>\n')

    def on_click(x, y, button, pressed):
        f = open('keylogger_mouse.txt', 'a')
        if button == mouse.Button.left:
            if pressed == False: #False= Done clicking, on release - mouseUp #it triggers this 2 times, for press and release
                print (f'Left ... mouse.Button.left ... x,y: {x},{y}')
                f.write(f'left  ... x,y: {x},{y}\n')

        if button == mouse.Button.right:
            if pressed==False: #False= Done clicking, on release - mouseUp #it triggers this 2 times, for press and release
                print (f'right ... mouse.Button.right ... x,y: {x},{y}')
                f.write(f'right  ... x,y: {x},{y}\n')
        if button == mouse.Button.middle:
            if pressed==False: #False= Done clicking, on release - mouseUp #it triggers this 2 times, for press and release
                print (f'middle ... mouse.Button.middle ... x,y: {x},{y}')
                f.write(f'middle  ... x,y: {x},{y}\n')

    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except Exception as e:
            print('Done'.format(e.args[0]))




# import AllWINDOWS as wins
# wins.moveMouseTO(500,50,"FAST")
def moveMouseTO(x,y,speed="FAST"):
    speed_in_seconds = {'FAST2': .25, 'FAST1': 1, 'FAST': 1, 'MEDIUM': 2, 'SLOW': 4,}
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    print(f"moving mouse to (x,y): {x,y} in {speed_in_seconds[speed]} seconds")
    pg.moveTo(x,y,speed_in_seconds[speed])




# import AllWINDOWS as wins
# wins.mousePositionLOOP()

def mousePositionLOOP():
    import time
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    idx = 1
    while True:
        mouse = pg.position() # Point(x=1495, y=231)
        print(f"{idx}) mouse:")
        print(mouse)
        #return mouse
        time.sleep(1)
        idx += 1



# import AllWINDOWS as wins
# wins.mousePosition()

# pyautogui
def mousePosition():
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    mouse = pg.position() # Point(x=1495, y=231)
    print("mouse:")
    print(mouse)
    return mouse



def mouseClick(x=100,y=20):
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    mouse = x,y = pg.position() # Point(x=1495, y=231)
    #print("mouse:")
    #print(mouse)
    return (x,y)
#Size(width=1920, height=1080)



# import AllWINDOWS as wins
# res = wins.screenSize2() # The screen resolution is: (1536, 864) - ctypes
# wins.screenSize() # OS Window Size: # Size(width=1920, height=1080) - pyautogui

# ctypes
def screenSize2(): #top left is 0,0
    import ctypes
    user32 = ctypes.windll.user32

    # get screen resolution of primary monitor
    res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    print(f"The screen resolution is: {res}")
    return res



# import AllWINDOWS as wins
# OSwidth, OSheight = wins.screenSizeOS() # OS Window Size: # Size(width=1920, height=1080) - pyautogui
# res = wins.screenSize2() # The screen resolution is: (1536, 864) - ctypes

# mousePosition() - pyautogui
# pyautogui
def screenSizeOS(): # top left is 0,0
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    os_window_size = pg.size() #Size(width=1920, height=1080)
    #width, height = pg.size()
    print("OS Window Size:")
    print(os_window_size)
    return os_window_size


# import AllWINDOWS as wins
# wins.screenSizeOSheight()
def screenSizeOSheight(): # top left is 0,0
    import pyautogui as pg  # pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    # pg.size()  # Size(width=1920, height=1080)
    width, height = pg.size()
    print("OS height is: "+height)
    return height

# import AllWINDOWS as wins
# wins.screenSizeOSwidth()
def screenSizeOSwidth(): # top left is 0,0
    import pyautogui as pg  # pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    # pg.size()  # Size(width=1920, height=1080)
    width, height = pg.size()
    print("OS width is: "+width)
    return width



# import AllWINDOWS as wins
# wins.getWindowsBoxPixels('Untitled - Notepad2')

#ctypes
def getWindowsBoxPixels(windowName='Untitled - Notepad2'):
    import ctypes
    from ctypes import wintypes
    user32 = ctypes.windll.user32
    handle = user32.FindWindowW(None, windowName)
    rect = wintypes.RECT()
    ff=ctypes.windll.user32.GetWindowRect(handle, ctypes.pointer(rect))
    # print(ff) # 1
    string = f"Window Name: {windowName} --- left: {rect.left}, top:{rect.top}, right: {rect.right}, bottom:{rect.bottom}"
    print(string) #153 188 1214 1157
    return string



def WindowRect():
    import ctypes
    from ctypes import wintypes
    user32 = ctypes.windll.user32
    handle = user32.FindWindowW(None, 'Untitled - Notepad2')
    rect = wintypes.RECT()
    ff=ctypes.windll.user32.GetWindowRect(handle, ctypes.pointer(rect))
    string = rect.left,rect.top,rect.right,rect.bottom
    print() #153 188 1214 1157
    #print(ff)

# import AllWINDOWS as wins
# wins.moveWindowsByName("Untitled - Notepad2") #exact

# moves an untitled Notepad2 window
# uses ctypes
def moveWindowsByName(windowName="Untitled - Notepad2"):
    import ctypes
    import pyautogui
    user32 = ctypes.windll.user32

    # get screen resolution of primary monitor
    res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    # res is (2293, 960) for 3440x1440 display at 150% scaling
    user32.SetProcessDPIAware()
    res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    # res is now (3440, 1440) for 3440x1440 display at 150% scaling

    # get handle for Notepad window
    # non-zero value for handle should mean it found a window that matches
    # handle = user32.FindWindowW(u'Notepad', None)
    handle = user32.FindWindowW(None, windowName) #exact window name

    # meaning of 2nd parameter defined here
    # https://msdn.microsoft.com/en-us/library/windows/desktop/ms633548(v=vs.85).aspx
    # minimize window using handle
    user32.ShowWindow(handle, 6)
    # maximize window using handle
    user32.ShowWindow(handle, 9)

    # move window using handle
    # MoveWindow(handle, x, y, height, width, repaint(bool))
    user32.MoveWindow(handle, 100, 100, 400, 400, True)

    #at the end, the focus is on the typing for Notepad2
    #sendkeys("some message")
    # Search for Firefox in the menu search
    pyautogui.typewrite('\n')
    pyautogui.typewrite('\n')
    pyautogui.typewrite('hello world')
    pyautogui.typewrite('\n')
    pyautogui.typewrite('\n')


#----------------

#PIDs and Window Titles:

# import AllWINDOWS as wins
# wins.allWindowsPIDsAndTitles()

#prints all Process IDs and Windows
#ctypes
def allWindowsPIDsAndTitles():
    #from __future__ import print_function  # *show this line to run*

    import ctypes
    from ctypes import wintypes
    from collections import namedtuple

    user32 = ctypes.WinDLL('user32', use_last_error=True)

    def check_zero(result, func, args):
        if not result:
            err = ctypes.get_last_error()
            if err:
                raise ctypes.WinError(err)
        return args

    if not hasattr(wintypes, 'LPDWORD'):  # PY2
        wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

    WindowInfo = namedtuple('WindowInfo', 'pid title')

    WNDENUMPROC = ctypes.WINFUNCTYPE(
        wintypes.BOOL,
        wintypes.HWND,  # _In_ hWnd
        wintypes.LPARAM, )  # _In_ lParam

    user32.EnumWindows.errcheck = check_zero
    user32.EnumWindows.argtypes = (
        WNDENUMPROC,  # _In_ lpEnumFunc
        wintypes.LPARAM,)  # _In_ lParam

    user32.IsWindowVisible.argtypes = (
        wintypes.HWND,)  # _In_ hWnd

    user32.GetWindowThreadProcessId.restype = wintypes.DWORD
    user32.GetWindowThreadProcessId.argtypes = (
        wintypes.HWND,  # _In_      hWnd
        wintypes.LPDWORD,)  # _Out_opt_ lpdwProcessId

    user32.GetWindowTextLengthW.errcheck = check_zero
    user32.GetWindowTextLengthW.argtypes = (
        wintypes.HWND,)  # _In_ hWnd

    user32.GetWindowTextW.errcheck = check_zero
    user32.GetWindowTextW.argtypes = (
        wintypes.HWND,  # _In_  hWnd
        wintypes.LPWSTR,  # _Out_ lpString
        ctypes.c_int,)  # _In_  nMaxCount

    def list_windows():
        '''Return a sorted list of visible windows.'''
        result = []

        @WNDENUMPROC
        def enum_proc(hWnd, lParam):
            if user32.IsWindowVisible(hWnd):
                pid = wintypes.DWORD()
                tid = user32.GetWindowThreadProcessId(
                    hWnd, ctypes.byref(pid))
                length = user32.GetWindowTextLengthW(hWnd) + 1
                title = ctypes.create_unicode_buffer(length)
                user32.GetWindowTextW(hWnd, title, length)
                result.append(WindowInfo(pid.value, title.value))
            return True

        user32.EnumWindows(enum_proc, 0)
        return sorted(result)

    psapi = ctypes.WinDLL('psapi', use_last_error=True)

    psapi.EnumProcesses.errcheck = check_zero
    psapi.EnumProcesses.argtypes = (
        wintypes.LPDWORD,  # _Out_ pProcessIds
        wintypes.DWORD,  # _In_  cb
        wintypes.LPDWORD,)  # _Out_ pBytesReturned

    def list_pids():
        '''Return sorted list of process IDs.'''
        length = 4096
        PID_SIZE = ctypes.sizeof(wintypes.DWORD)
        while True:
            pids = (wintypes.DWORD * length)()
            cb = ctypes.sizeof(pids)
            cbret = wintypes.DWORD()
            psapi.EnumProcesses(pids, cb, ctypes.byref(cbret))
            if cbret.value < cb:
                length = cbret.value // PID_SIZE
                return sorted(pids[:length])
            length *= 2

    # if __name__ == '__main__':
    print('Process IDs:')
    print(*list_pids(), sep='\n')
    print('\nWindows:')
    print(*list_windows(), sep='\n')



#------------------------


# v1

"""
import AllWINDOWS as wins
windows = wins.arrayOfWindows()
print("windows:")
print(windows)
print("---windows---")
"""

# python windows get window dimensions - of active window, of a draggable area - maybe menu area
# python windows mouse drag


#windows (12):
#['pythonProject – AllWINDOWS.py',
# "Win32 Python: Getting all window titles | Johannes Sasongko's (abandoned) blog - Brave",
# 'Malwarebytes Tray Application',
# 'C:\\Users\\myvor\\PycharmProjects\\pythonProject',
# 'Task Manager', 'Changing the Background Image - Window Title',
# 'Microsoft Text Input Application',
# 'Calculator',
# 'Calculator',
# 'Settings',
# 'Settings',
# 'Program Manager']



# import AllWINDOWS as wins
# windows = wins.arrayOfWindowsVisible()

# -------------
# ctypes only
# -------------
def arrayOfWindowsVisible():
    import ctypes

    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            title = buff.value
            if len(title)>0:
                titles.append(buff.value)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    print(titles)
    return titles


# 10
# windows:
# [{'x': 1314, 'y': 120, 'w': 207, 'h': 42, 'name': 'FastStone Capture'},
# {'x': 338, 'y': 151, 'w': 1180, 'h': 656, 'name': 'pythonProject – AllWINDOWS.py'},
# {'x': 376, 'y': 51, 'w': 1103, 'h': 678, 'name': "Does Python have a string 'contains' substring method? - Stack Overflow - Brave"},
# {'x': 34, 'y': 78, 'w': 334, 'h': 540, 'name': 'Calculator'},
# {'x': 179, 'y': 179, 'w': 895, 'h': 518, 'name': 'C:\\Windows\\system32\\cmd.exe'},
# {'x': 478, 'y': 73, 'w': 1038, 'h': 712, 'name': 'Settings'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'Documents'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'C:\\Users\\myvor\\PycharmProjects\\pythonProject\\z-IMAGES_1\\0.cool'},
# {'x': 128, 'y': 128, 'w': 1152, 'h': 598, 'name': 'MS_WebcheckMonitor'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'DWM Notification Window'}]

# windows:
# [{'x': 836, 'y': 650, 'w': 266, 'h': 20, 'name': ''},
# {'x': 1248, 'y': 744, 'w': 120, 'h': 80, 'name': ''},
# {'x': 1314, 'y': 120, 'w': 207, 'h': 42, 'name': 'FastStone Capture'},
# {'x': 338, 'y': 151, 'w': 1180, 'h': 656, 'name': 'pythonProject – main.py'},
# {'x': 26, 'y': 26, 'w': 473, 'h': 66, 'name': ' '},
# {'x': -1, 'y': -1, 'w': 109, 'h': 31, 'name': 'theAwtToolkitWindow'},
# {'x': 34, 'y': 78, 'w': 334, 'h': 540, 'name': 'Calculator'},
# {'x': 179, 'y': 179, 'w': 895, 'h': 518, 'name': 'C:\\Windows\\system32\\cmd.exe'},
# {'x': 154, 'y': 154, 'w': 1152, 'h': 598, 'name': ''},
# {'x': 478, 'y': 73, 'w': 1038, 'h': 712, 'name': 'Settings'},
# {'x': 77, 'y': 77, 'w': 1152, 'h': 598, 'name': 'QTrayIconMessageWindow'},
# {'x': 505, 'y': 190, 'w': 526, 'h': 422, 'name': 'mbamtray'},
# {'x': 26, 'y': 26, 'w': 1152, 'h': 598, 'name': 'QTrayIconMessageWindow'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'Documents'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'C:\\Users\\myvor\\PycharmProjects\\pythonProject\\z-IMAGES_1\\0.cool'},
# {'x': 128, 'y': 128, 'w': 1152, 'h': 598, 'name': 'MS_WebcheckMonitor'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'DWM Notification Window'},
# {'x': -25600, 'y': -25600, 'w': 159, 'h': 27, 'name': 'macos - Using Mouse and Keyboard Listeners Together in Python - Stack Overflow - Brave'}]

#
#global variable for - arrayOfWindows()
windows = []

# print array of all open windows: window location, and window size
def arrayOfWindows():
    import win32gui

    def callback(hwnd, extra):
        global windows
        rect = win32gui.GetWindowRect(hwnd)
        title = win32gui.GetWindowText(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y

        dict = {'x': x, 'y': y, 'w': w, 'h': h, 'name': title}
        if w > 0 and h > 0 and len(title)>2 and "tray" not in title and "Tray" not in title and x > 0 or x==(-25600) and y > 0 or y==(-25600): #if it's a window with a width and height-movable
            windows.append(dict)
            #print("rect:")
            #print(rect)
            #print("Window %s:" % title)
            #print("\tLocation: (%d, %d)" % (x, y))
            #print("\t    Size: (%d, %d)" % (w, h))

    win32gui.EnumWindows(callback, None)
    #print("windows:")
    print(len(windows))
    #print(windows)
    #print("---windows---")

    return windows


