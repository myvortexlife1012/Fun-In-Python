
# import AllWINDOWS as wins
# wins.mouseAndKeysListen1()
# wins.mouseAndKeysListen2() #outputs per pixel mouse movements
# wins.moveMouseTO(500,50,"FAST")
# wins.screenSize()
# wins.moveWindowsByName()
  # take where window is and move it around a bit
  # take where window is, and it's width and height, and click a button on it
#needs win32gui - python 3.6 env
# windows = wins.arrayOfWindows() #returns array of the windows



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
# wins.mousePosition()

def mousePosition():
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    mouse = pg.position() # Point(x=1495, y=231)
    print("mouse:")
    print(mouse)
    return mouse



# import AllWINDOWS as wins
# wins.screenSize()

#top left is 0,0
def screenSize():
    import pyautogui as pg #pip install pyautogui # installs: PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.1.4 pyscreeze-0.1.28
    os_window_size = pg.size() #Size(width=1920, height=1080)
    print("OS Window Size:")
    print(os_window_size)
    return os_window_size





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


