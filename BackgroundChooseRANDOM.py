# uses listAllFILES - to get full paths of all pics available
# v1

#import BackgroundChooseRANDOM
# BackgroundChooseRANDOM.BackgroundChooseRANDOM(listALlFILES_array)

def BackgroundChooseRANDOM(listALlFILES_array):
    length = listALlFILES_array[0]
    filenames = listALlFILES_array[1]

    import random
    rand_num = random.randint(0, length-1)
    print("random number chosen: ", rand_num)
    print("\ntotal is: ", length)
    filename = filenames[rand_num]
    print("\nfilename is: ", filename)

    import platform
    pl = platform.system()
    """
    print(pl)
    if pl=='Linux':
        print("You're using Linux")
    elif pl=='Windows':
        print("You're using Windows")
    """

    #for windows
    if platform.system() == 'Windows':
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filename, 0)

    #for UBUNTU Linux
    #current_background1 = "gsettings get org.gnome.desktop.background picture-uri"
    #current_background = os.system("gsettings get org.gnome.desktop.background picture-uri")

    #change the background
    #filename = filename (spaces = '%20')

    #from urllib.parse import quote
    #filename = quote(filename)
    #image_filename = "premium wallpapers sunrises (1).jpg"
    if pl=='Linux':
        string = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+filename
        print("\n\n"+string)
        import os
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+filename)

