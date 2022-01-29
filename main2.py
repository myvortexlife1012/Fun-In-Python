import mymodule
mymodule.greeting("Mike")



import GuiAPPs as guiApps
guiApps.guiBGchangeShow()
# guiApps.GuiWindowLAYOUTSshow()
# guiApps.GuiWithImageBUTTONSshow()




import ImageSAVER as study1
study1.ImgSaverSTUDY()


import ImagePathSEER as ips
ips.imagePathSeer("z-IMAGES_1/0.cool")

"""
import GuiGAMEsudoku as gui_game
gui_game.play()
"""


"""
import GuiAPPwithButtons as guiApp
guiApp.show()

import GuiGAMEpong as gui_game
gui_game.play()



import GuiWindowLAYOUTS as guiLayouts
guiLayouts.show()
"""


"""
import GuiSplashSCREEN as guiSplash
guiSplash.show()
"""

#Change the background automatically
import listAllFILES as lfs
folder_path="z-IMAGES_1/0.cool"
array = lfs.listAllFILES(folder_path)
length = array[0]
pics = array[1]

import BackgroundChooseRANDOM as bgcrand
bgcrand.BackgroundChooseRANDOM(array)




"""

import GuiHTMLlike as guiDesign
guiDesign.show()


import GuiWEATHER as guiWeather
guiWeather.show()

import GuiDATE as guiDate
guiDate.show()

import GuiImagesGALLERY as guiPhotoGallery
guiPhotoGallery.show()
"""


"""
import GuiWithImageBUTTONS as gui_images_first_try
gui_images_first_try.run()
"""

#import ImageSAVER as is1
#is1.imageSaver("premium wallpapers ready to eat chef prepared meals")


"""
import ProgressBAR as pb
pb.ProgressBAR(.1)
"""

"""
import RepeatSoOFTEN as repeat
repeat.RepeatSoOFTEN()
"""

"""
import ImageSAVER as is1
is1.imageSaver("premium wallpapers great snowy mountains",30)
is1.imageSaver("premium wallpapers green lush hills",30)
is1.imageSaver("premium wallpapers great mountains",30)
is1.imageSaver("premium wallpapers epic countrysides",30)
is1.imageSaver("premium wallpapers white clean apartment",30)
is1.imageSaver("premium wallpapers modern smart house",30)
"""


"""
#https://en.wikipedia.org/wiki/Insect_ecology
#https://en.wikipedia.org/wiki/Brewing
import PlainTextFromWikipediaURL as ptxt
text = ptxt.PlainTextFromWikipediaURL("https://en.wikipedia.org/wiki/Insect_ecology",True,False)
#text = ptxt.PlainTextFromURL("https://en.wikipedia.org/wiki/Brewing",False,False)
print(text)

import sayTHIS as st
st.sayTHIS(text) #defaults to "Hello World"
"""


