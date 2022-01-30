
# import OpenAFileOrFolder as opn
# filepath = r"C:\Users\myvor\Pictures\0.animals\beautiful tiger wallpapers\!image18.jpg"
# opn.openFileWithDefaultProgram(filepath)

def openFileWithDefaultProgram(filepath=""):
    #this opens a file - like Double-Clicking on it
    #it opens with the default program
    if filepath=="":
        filepath = r"C:\Users\myvor\Pictures\0.animals\beautiful tiger wallpapers\!image18.jpg"
    print(filepath)
    import subprocess, os, platform
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))





"""
working with python and paths:
----------
you can use always:

'C:/mydir'
this works both in linux and windows. Other posibility is

'C:\\mydir'
if you have problems with some names you can also try raw string literals:

r'C:\mydir'
however best practice is to use the os.path module functions that always select the correct configuration for your OS:

os.path.join(mydir, myfile)
From python 3.4 you can also use the pathlib module. This is equivelent to the above:

pathlib.Path(mydir, myfile)

https://stackoverflow.com/questions/2953834/windows-path-in-python

"""