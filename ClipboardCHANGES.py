#v1

#NOTE: this is a loop
#when the clipboard changes
#it prints it in the console

#import ClipboardCHANGES as cchanges
#cchanges.ClipboardCHANGES()

# Required for Linux - 1 of:
# sudo apt-get install xsel
# sudo apt-get install xclip
# pip install gtk
# pip install PyQt4

def ClipboardCHANGES():
  import platform
  pl = platform.system()

  if pl == 'Windows' or pl == 'Linux':
    import time
    import sys
    import os
    sys.path.append(os.path.abspath("SO_site-packages"))

    import pyperclip

    recent_value = ""
    while True:
      tmp_value = pyperclip.paste()
      if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value changed: %s" % str(recent_value))
        #print("Value changed: %s" % str(recent_value)[:20]) #just 20 chars
      time.sleep(0.1)

