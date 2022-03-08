
# import ClipboardChangesREAD as clipboard
# clipboard.getClipboardTEXT()
# clipboard.ClipboardChangesREAD()
# clipboard.ClipboardCHANGES()



#-------------


# import ClipboardCHANGES as clipboard
# clipboard.getClipboardTEXT()

def getClipboardTEXT():
  import win32clipboard

  # get clipboard data
  win32clipboard.OpenClipboard()
  data = win32clipboard.GetClipboardData()
  win32clipboard.CloseClipboard()
  print(data)
  return data




#v1
#import ClipboardCHANGES as clipboard
#clipboard.ClipboardCHANGES()

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



#v1
#import ClipboardCHANGES as clipboard
#clipboard.ClipboardChangesREAD()

# Required:
# pip install pyperclip, pyttsx3

# Required for Linux - 1 of:
# sudo apt-get install xsel
# sudo apt-get install xclip
# pip install gtk
# pip install PyQt4

def ClipboardChangesREAD():
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
      import sayTHIS as st
      st.sayTHIS(recent_value)# st.sayTHIS("Hello World")
      #print("Value changed: %s" % str(recent_value)[:20]) #just 20 chars
    time.sleep(0.1)




