#import ClipboardTEXT as ctxt
#ctxt.clipboard()

def clipboard():
  import win32clipboard

  # get clipboard data
  win32clipboard.OpenClipboard()
  data = win32clipboard.GetClipboardData()
  win32clipboard.CloseClipboard()
  print(data)
  return data
