#import ClipboardTEXT as ctxt
#text = ctxt.ClipboardTEXT()

# Required for Linux - 1 of:
# sudo apt-get install xsel
# sudo apt-get install xclip
# pip install gtk
# pip install PyQt4

def ClipboardTEXT():
  import platform
  pl = platform.system()

  if pl == 'Linux':
    print("You're using Linux")
    import clipboard
    #clipboard.copy("abc")  # now the clipboard content will be string "abc"
    text = clipboard.paste()  # text will have the content of clipboard
    print("clipboard has:")
    print(text)
    return text

  if pl == 'Windows':
    import win32clipboard

    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print("clipboard has:")
    print(data)
    return data

