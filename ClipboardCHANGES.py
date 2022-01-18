
#import ClipboardCHANGES as cchanges
#cchanges.ClipboardCHANGES()

def ClipboardCHANGES():
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