
# import ImageSAVER as saver

# saver.resizeAllPhotosInPath(folderPath="z-IMAGES_1\\!new")
# saver.resizeAsThumbnailsOfPhotosInPath(folderPath="z-IMAGES_1\\!new")

# saver.imageResize(imageFilePath, width = 1920, jpgQuality=70)
# saver.imageResizeExact(imageFilePath, width=32, height=32, jpgQuality=70)

# saver.unsplashPersonsPage(id="@borisbaldinger")
# saver.unsplashImagesFromSearch(q="sunrise",perPage=60)
# saver.imageSaverStudy1(q="Study Topic", qty=30)
# saver.ImageSaver2(q="premium wallpapers", qty=30)
# saver.ImgSaverSTUDY()

# import ImageSAVER as saver
# saver.download(imgUrl="http://", savePath="z-IMAGES_1/!new/test_search_query", imgFilename="long_file_name.jpg")

#-------------------------------------------------



# import ImageSAVER as s
# s.createThumbsForPdnaBank()
def createThumbsForPdnaBank():
    folderPath = "mycosmicdna/pics"
    print(f"createThumbsForPdnaBank: {folderPath}")
    print(f"going to create thumbnails for images in this folder:\n{folderPath}\n")
    import FUNCTIONS as f
    import listAllFILES as f
    pics = f.listAllImages(folderPath) #IT USES THE ONLY IMAGES - file list
    #print(f"\npics: \n\n")
    #print(f"\npics: \n{pics}\n\n")
    count=1
    for pic in pics:
        #print(f"\n\n --{count})--  pic: {pic}")

        #print(f"renaming filepath - to a thumbnails folder")
        p = pic.split("/")
        imgName = p[len(p)-1]
        #print(f"imgName: {imgName}")
        # set up the new thumbnail filename
        folderpathThumbs = pic.replace(imgName,"") + "thumbnails"
        #print(f"folderpathThumbs: {folderpathThumbs}")
        filename2 = imgName[:-4] + "__thumbnail" + imgName[-4:]
        thumbnailFilename = folderpathThumbs + "/" + filename2
        #print(f"thumbnailFilename: {thumbnailFilename}")

        #print(f"resizing into thumbnail")
        count += 1

        #no need to do it again
        status = f.fileExists(pic)
        if status==False:
            imageToThumbnailPdnaBank(imageFilePath=pic, width=50, jpgQuality=70, height=50)




# import ImageSAVER as s
# s.imageToThumbnailPdnaBank(imageFilePath="C:\\Users\\myvor\\Desktop\\Backgrounds\\unsplash_green.jpg", width=250, jpgQuality=70, height=200)

# resize into thumbnails
#it goes off of height
def imageToThumbnailPdnaBank(imageFilePath="c:/file.jpg", width=50, jpgQuality=70, height=50):
    import os
    if "\\" in imageFilePath:
        path = imageFilePath.split("\\")
    elif "/" in imageFilePath:
        path = imageFilePath.split("/")

    #print(f"path-len: {len(path)} ... is it zero? - split above better")
    filename = path[len(path) - 1]
    print(f"\nfilename: {filename}")
    #set up the new thumbnail filename
    folderpathThumbs = imageFilePath[:-1*len(filename)]+"thumbnails"
    folderpathThumbs = folderpathThumbs.replace("\\","/")
    print(f"folderpathThumbs: {folderpathThumbs}")
    filename2 = filename[:-4]+"__thumbnail"+filename[-4:]
    filename2Thumb = folderpathThumbs+"\\"+filename2
    filename2Thumb = filename2Thumb.replace("\\", "/")
    print(f"filename2Thumb: {filename2Thumb}")
    #--------------------------
    #does path exist - if not make it
    isExist = os.path.exists(folderpathThumbs)
    if not isExist:
        #create the folder
        os.makedirs(folderpathThumbs)
        print(f"The new directory is created! - {folderpathThumbs}")
    # --------------------------
    import cv2  # pip install opencv-python
    import imutils
    img = cv2.imread(imageFilePath, cv2.IMREAD_COLOR)
    img = imutils.resize(img, height=height)  # 1920 #, width=width
    # save IN THE THUMBNAIL FOLDER:
    cv2.imwrite(filename2Thumb, img, [int(cv2.IMWRITE_JPEG_QUALITY), jpgQuality])
    # cv2.imshow('image' , img)







#----------------------------
# import ImageSAVER as saver
# width, height = saver.imageWidthHeight(filename)

def imageWidthHeight(filename):
    from PIL import Image

    # get image
    filepath = "geeksforgeeks.png"
    img = Image.open(filepath)

    # get width and height
    width, height = img.size

    # display width and height
    print("The height of the image is: ", height)
    print("The width of the image is: ", width)
    return width, height

# import ImageSAVER as saver
# saver.resizeAllPhotosInPath(folderPath="z-IMAGES_1\\!new")

# resize all of the new images
def resizeAllPhotosInPath(folderPath="z-IMAGES_1\\!new"):
    import listAllFILES as lfs
    import ImageSAVER as saver
    # folder_path="z-IMAGES_1\\!new"
    array = lfs.listAllFILES(folderPath)
    length = array[0]
    pics = array[1]
    print(f"image files to be resized: {length}")
    for imageFilePath in pics:
        print(f"imageFilePath: {imageFilePath}")
        # resizes and replaces the image
        print("going to resize here")
        saver.imageResize(imageFilePath, width=1920,
                          jpgQuality=80)  # if they were portrait, they saved larger-since I was going off just the width


#----------------------------------------

"""
# EXAMPLE OF HOW TO USE IT:

import listAllFILES as filelist
folderPath = "z-IMAGES_1" #"z-IMAGES_1/0.cool/!new1/sunrise_waterfront"
print(f"folderPath: {folderPath}")
files = filelist.listAllImages(folderPath)
print(f"only images: ({len(files)})")
print(files)

import ImageSAVER as saver
saver.createThumbsForImageFolder(folderPath)
"""

#do I really want to create thumbnails - I would need to update the background tool - to avoid the thumbnails
# import ImageSAVER as saver
# saver.createThumbsForImageFolder(folderPath = "z-IMAGES_1/0.cool/!new1/beach_palm_trees")
#"C:\\Users\\myvor\\Desktop\\Backgrounds\\"
#
#resize into thumbnails
#--TODO: if it's portrait - resize it down to the height of the landscape
#---
def createThumbsForImageFolder(folderPath = "z-IMAGES_1/0.cool"):
    print(f"createThumbsForImageFolder(folderPath): {folderPath}")
    print(f"going to create thumbnails for images in this folder:\n{folderPath}\n")
    import FUNCTIONS as f
    import listAllFILES as filelist
    pics = filelist.listAllImages(folderPath) #IT USES THE ONLY IMAGES - file list
    print(f"\npics: \n\n")
    #print(f"\npics: \n{pics}\n\n")
    count=1
    for pic in pics:
        print(f"\n\n --{count})--  pic: {pic}")
        print(f"resizing into thumbnail")
        count += 1

        #no need to do it again
        #status = f.fileExists(pic)
        #if status:
        imageToThumbnail(imageFilePath=pic, width=250, jpgQuality=70, height=200)





# import ImageSAVER as saver
# saver.imageToThumbnail(imageFilePath="C:\\Users\\myvor\\Desktop\\Backgrounds\\unsplash_green.jpg", width=250, jpgQuality=70, height=200)

# resize into thumbnails
#it goes off of height
def imageToThumbnail(imageFilePath="c:\\file.jpg", width=250, jpgQuality=70, height=200):
    import os
    path = imageFilePath.split("\\")
    print(f"path-len: {len(path)} ... is it zero? - split above better")
    filename = path[len(path) - 1]
    print(f"\nfilename: {filename}")
    #set up the new thumbnail filename
    folderpathThumbs = imageFilePath[:-1*len(filename)]+"thumbnails"
    folderpathThumbs = folderpathThumbs.replace("\\","/")
    print(f"folderpathThumbs: {folderpathThumbs}")
    filename2 = filename[:-4]+"__thumbnail"+filename[-4:]
    filename2Thumb = folderpathThumbs+"\\"+filename2
    filename2Thumb = filename2Thumb.replace("\\", "/")
    print(f"filename2Thumb: {filename2Thumb}")
    #--------------------------
    #does path exist - if not make it
    isExist = os.path.exists(folderpathThumbs)
    if not isExist:
        #create the folder
        os.makedirs(folderpathThumbs)
        print(f"The new directory is created! - {folderpathThumbs}")
    # --------------------------
    import cv2  # pip install opencv-python
    import imutils
    img = cv2.imread(imageFilePath, cv2.IMREAD_COLOR)
    img = imutils.resize(img, height=height)  # 1920 #, width=width
    # save IN THE THUMBNAIL FOLDER:
    cv2.imwrite(filename2Thumb, img, [int(cv2.IMWRITE_JPEG_QUALITY), jpgQuality])
    # cv2.imshow('image' , img)






#resize images
# import ImageSAVER as saver
# saver.imageResize(imageFilePath, width = 1920, jpgQuality=70)

#overwrites the file
def imageResize(imageFilePath="", width=1920, jpgQuality=70):
    import cv2  # pip install opencv-python
    import imutils
    img = cv2.imread(imageFilePath , cv2.IMREAD_COLOR)
    img = imutils.resize(img, width=width) # 1920
    #cv2.imshow('image' , img)
    #save:
    cv2.imwrite(imageFilePath, img, [int(cv2.IMWRITE_JPEG_QUALITY), jpgQuality])

"""
filename = "C:/Users/myvor/PycharmProjects/pythonProject/z-Frames/beach_with_rocks"
filename += "/!frame.jpg"
print("filename:")
print(filename)
imageResize(filename, width=1920, jpgQuality=70)
"""



# import ImageSAVER as saver
# saver.imageResizeExact(imageFilePath, width=32, height=32, jpgQuality=70)

#overwrites the file
def imageResizeExact(imageFilePath, width=100, height=100, jpgQuality=70):
    import cv2  # pip install opencv-python
    img = cv2.resize(imageFilePath, (width, height), interpolation=cv2.INTER_AREA)
    cv2.imwrite(imageFilePath, img, [int(cv2.IMWRITE_JPEG_QUALITY), jpgQuality])




#-------------------------

#saver.download(
#    imgUrl="https://unsplash.com/photos/ZUJ6uPPnTGY/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjQzNzQzNzEx&force=true",
#    savePath="z-IMAGES_1/!new/test_search_query",
#    imgFilename="sunset_mountains_1.jpg"
#)

# import ImageSAVER as saver
# saver.download(imgUrl="http://", savePath="z-IMAGES_1/!new/test_search_query", imgFilename="long_file_name.jpg")

def download(imgUrl="http://url", savePath="z-IMAGES_1/!new/test_search_query", imgFilename="long_file_name_1.jpg"):
    import os
    import urllib.request

    # Download original images

    # add the path
    imgFilename = savePath + "/" + imgFilename
    print("Going to Download image to: imgFilename:")
    print(imgFilename)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
    urllib.request.install_opener(opener)

    # make the folder if not exists yet
    isExist = os.path.exists(savePath)
    if not isExist:
        os.mkdir(savePath)

    # it keeps going if it encounters an error:
    try:
        urllib.request.urlretrieve(imgUrl, imgFilename)
    except:
        pass


#-------------------------------
# simple thinking:
# def scraping():
    # Search for all ‘a’ tags.
    # Filter the tags having title = “Download photo”.
    # Save the links in a text file


#-------------------------------
# OTHER FREE IMAGE SITES
# https://rigorousthemes.com/blog/best-unsplash-alternatives/


#-------------------------------
# UNSPLASH IMAGES
#

# import ImageSAVER as saver
# saver.unsplashPersonsPage(id="@borisbaldinger")

# unsplash @person pages - parse
def unsplashPersonsPage(id="@borisbaldinger"):
    import requests
    from bs4 import BeautifulSoup
    import random
    from os.path import exists

    # unsplash @person pages - parse

    # get images first
    id = "@borisbaldinger"
    url = "https://unsplash.com/" + id  # @borisbaldinger

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}
    params = {}
    html = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')

    images = soup.select('img.YVj9w')  # chooses the images - that have sizes on them - in the long 'srcset' attribute
    print(f"len of images: {len(images)}")
    # print(images)

    # loop through each iteration
    counter = 0
    for image in images:
        saveImage = True
        src = image.attrs['src']
        # print the result
        # print("\n src: \n")
        # print(f"\n {src} \n")

        # srcset = image.attrs['srcset']
        # print("\n srcset: \n")
        # print(f"\n\n\n {srcset} \n\n\n")
        attribute = image.attrs
        # print(f"{counter})  {attribute}") #prints all attributes!

        srcset = image.attrs['srcset'].split(', ')  # seperate the list of src - width sizes
        # get the last one
        # print("\n srcset: \n")
        # print(f"\n\n\n {srcset} \n\n\n")

        # get the alt name as well
        try:  # it was erroring on 'alt'
            alt = image.attrs['alt'].replace(" ", "_")
            # fix if alt is too long:  # 39_aerial_photography_of_green_field_near_lake_viewing_mountain_under_blue_and_white_sky_during_daytime.jpg
            #filename = f"{counter}_{alt}.jpg"
            filename = f"{alt}.jpg"
        except: #don't save this file - it has no alt
            numRand4 = random.randint(1111, 9999)
            filename = f"image_{counter}__{numRand4}.jpg"
            saveImage = False

        url = srcset[len(srcset) - 1].split(" ")[
            0]  # select the last url - the largest image #remove the - space width size at the end
        print(f"\n\n{counter}) filename: {filename}")
        print(f"full url: {url}")

        #if filename does not exist yet- in that location: download it

        savePath = f"z-IMAGES_1/!new/{id}/{filename}"

        file_exists = exists(savePath)

        if file_exists:
            print("file is there")
        else:
            print("file is not there yet")

            if saveImage==True: #if it's not going to skip it # no alt info - probably repeats
                download(
                    imgUrl=url,
                    savePath="z-IMAGES_1/!new/" + id,
                    imgFilename=filename
                )

        counter += 1


# import ImageSAVER as saver
# saver.unsplashImagesFromSearch(q="beach sunrise",perPage=60)

def unsplashImagesFromSearch(q="sunrise",perPage=60):
    # https://unsplash.com/napi/search?query=sunrise&xp=&per_page=20
    # returns JSON

    import requests
    #perPage = 60 # 20
    #q = "sunrise"
    url = f"https://unsplash.com/napi/search?query={q}&xp=&per_page={perPage}"  # returns JSON format
    headers = {
        'authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'
    }
    response = requests.get(url, headers=headers)
    jsonData = response.text  # dict
    # print("jsonData:")
    # print(jsonData)

    import json

    json_data = jsonData  # dict

    # json_object = json.loads(json_data)
    # PRETTY in terminal
    # json_formatted_str = json.dumps(json_object, indent=2)
    # print("json_formatted_str:")
    # print(json_formatted_str) #PRETTY in terminal

    json_object = json.loads(json_data)
    photosJson = json_object['photos']['results']
    json_formatted_str = d = json.dumps(photosJson, indent=2)
    # print("photosJson:")
    # print(photosJson)

    # loop through a complicated dictionary
    imgs_json = []
    for x in json_object.keys():  # photos
        if x == 'photos':
            # print(f"--{x}--")
            pass
        for y in json_object[x]:  # results
            if y == 'results':
                # print(y)
                for z in json_object[x][y]:
                    imgs_json.append(z)
                    # print(z) #{'id': 'xg8z_KhSorQ', 'created_at': '2017-11-15T17:26:45-05:00', 'updated_at': '2022-01-31T17:02:19-05:00', 'promoted_at': '2017-11-16T09:12:14-05:00', 'width': 6000, 'height': 4000, 'color': '#260c0c', 'blur_hash': 'LuGk:;axEMay%$j@WBa|1Nj[xZfk', 'description': 'Day’s like this..', 'alt_description': 'silhouette of plant during sunset', 'urls': {'raw': 'https://images.unsplash.com/photo-1510784722466-f2aa9c52fff6?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz&ixlib=rb-1.2.1', 'full': 'https://images.unsplash.com/photo-1510784722466-f2aa9c52fff6?crop=entropy&cs=srgb&fm=jpg&ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz&ixlib=rb-1.2.1&q=85', 'regular': 'https://images.unsplash.com/photo-1510784722466-f2aa9c52fff6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz&ixlib=rb-1.2.1&q=80&w=1080', 'small': 'https://images.unsplash.com/photo-1510784722466-f2aa9c52fff6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz&ixlib=rb-1.2.1&q=80&w=400', 'thumb': 'https://images.unsplash.com/photo-1510784722466-f2aa9c52fff6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz&ixlib=rb-1.2.1&q=80&w=200'}, 'links': {'self': 'https://api.unsplash.com/photos/xg8z_KhSorQ', 'html': 'https://unsplash.com/photos/xg8z_KhSorQ', 'download': 'https://unsplash.com/photos/xg8z_KhSorQ/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz', 'download_location': 'https://api.unsplash.com/photos/xg8z_KhSorQ/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8c3VucmlzZXx8MHx8fHwxNjQzNjczODAz'}, 'categories': [], 'likes': 995, 'liked_by_user': False, 'current_user_collections': [], 'sponsorship': None, 'topic_submissions': {}, 'user': {'id': '6RdZJvQjxlQ', 'updated_at': '2022-01-31T13:52:40-05:00', 'username': 'ocvisual', 'name': 'OC Gonzalez', 'first_name': 'OC', 'last_name': 'Gonzalez', 'twitter_username': 'ocvisuals', 'portfolio_url': 'http://ocvisual.com', 'bio': 'Please credit my instagram account at @OCVISUAL if you repost any of my images on your social network.\r\n\r\nPlease email me if you are considering using my work for any paid products or commissions.\r\n\r\nThank you.', 'location': 'Santa Barbara, CA', 'links': {'self': 'https://api.unsplash.com/users/ocvisual', 'html': 'https://unsplash.com/@ocvisual', 'photos': 'https://api.unsplash.com/users/ocvisual/photos', 'likes': 'https://api.unsplash.com/users/ocvisual/likes', 'portfolio': 'https://api.unsplash.com/users/ocvisual/portfolio', 'following': 'https://api.unsplash.com/users/ocvisual/following', 'followers': 'https://api.unsplash.com/users/ocvisual/followers'}, 'profile_image': {'small': 'https://images.unsplash.com/profile-1608066024966-7dd0e41aad4dimage?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32', 'medium': 'https://images.unsplash.com/profile-1608066024966-7dd0e41aad4dimage?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64', 'large': 'https://images.unsplash.com/profile-1608066024966-7dd0e41aad4dimage?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128'}, 'instagram_username': 'ocvisual', 'total_collections': 0, 'total_likes': 3, 'total_photos': 57, 'accepted_tos': True, 'for_hire': True, 'social': {'instagram_username': 'ocvisual', 'portfolio_url': 'http://ocvisual.com', 'twitter_username': 'ocvisuals', 'paypal_email': None}}, 'tags_preview': [{'type': 'search', 'title': 'sunrise'}, {'type': 'search', 'title': 'santa barbara'}, {'type': 'landing_page', 'title': 'blue', 'source': {'ancestry': {'type': {'slug': 'wallpapers', 'pretty_slug': 'HD Wallpapers'}, 'category': {'slug': 'colors', 'pretty_slug': 'Color'}, 'subcategory': {'slug': 'blue', 'pretty_slug': 'Blue'}}, 'title': 'HD Blue Wallpapers', 'subtitle': 'Download Free Blue Wallpapers', 'description': 'Choose from a curated selection of blue wallpapers for your mobile and desktop screens. Always free on Unsplash.', 'meta_title': 'Blue Wallpapers: Free HD Download [500+ HQ] | Unsplash', 'meta_description': 'Choose from hundreds of free blue wallpapers. Download HD wallpapers for free on Unsplash.', 'cover_photo': {'id': 'DbwYNr8RPbg', 'created_at': '2018-03-30T16:31:32-04:00', 'updated_at': '2022-01-28T06:04:01-05:00', 'promoted_at': '2018-03-31T22:25:27-04:00', 'width': 4433, 'height': 7880, 'color': '#0c8ca6', 'blur_hash': 'LrErCEM|R*WC~VNGWBWV-pWCWVj[', 'description': 'AQUA', 'alt_description': 'white clouds and blue skies', 'urls': {'raw': 'https://images.unsplash.com/photo-1522441815192-d9f04eb0615c?ixlib=rb-1.2.1', 'full': 'https://images.unsplash.com/photo-1522441815192-d9f04eb0615c?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb', 'regular': 'https://images.unsplash.com/photo-1522441815192-d9f04eb0615c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max', 'small': 'https://images.unsplash.com/photo-1522441815192-d9f04eb0615c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max', 'thumb': 'https://images.unsplash.com/photo-1522441815192-d9f04eb0615c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max'}, 'links': {'self': 'https://api.unsplash.com/photos/DbwYNr8RPbg', 'html': 'https://unsplash.com/photos/DbwYNr8RPbg', 'download': 'https://unsplash.com/photos/DbwYNr8RPbg/download', 'download_location': 'https://api.unsplash.com/photos/DbwYNr8RPbg/download'}, 'categories': [], 'likes': 4979, 'liked_by_user': False, 'current_user_collections': [], 'sponsorship': None, 'topic_submissions': {'textures-patterns': {'status': 'approved', 'approved_on': '2020-06-12T09:12:52-04:00'}}, 'user': {'id': 'BrQR9ZNLFVg', 'updated_at': '2022-01-28T15:14:32-05:00', 'username': 'resul', 'name': 'Resul Mentes', 'first_name': 'Resul', 'last_name': 'Mentes', 'twitter_username': 'resulmentess', 'portfolio_url': 'http://resulmentes.com', 'bio': '.', 'location': 'Sakarya,Türkiye', 'links': {'self': 'https://api.unsplash.com/users/resul', 'html': 'https://unsplash.com/@resul', 'photos': 'https://api.unsplash.com/users/resul/photos', 'likes': 'https://api.unsplash.com/users/resul/likes', 'portfolio': 'https://api.unsplash.com/users/resul/portfolio', 'following': 'https://api.unsplash.com/users/resul/following', 'followers': 'https://api.unsplash.com/users/resul/followers'}, 'profile_image': {'small': 'https://images.unsplash.com/profile-1579609671436-8ac276f87e50image?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=32&w=32', 'medium': 'https://images.unsplash.com/profile-1579609671436-8ac276f87e50image?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=64&w=64', 'large': 'https://images.unsplash.com/profile-1579609671436-8ac276f87e50image?ixlib=rb-1.2.1&q=80&fm=jpg&crop=faces&cs=tinysrgb&fit=crop&h=128&w=128'}, 'instagram_username': 'resulmentes2', 'total_collections': 2, 'total_likes': 22, 'total_photos': 48, 'accepted_tos': True, 'for_hire': True, 'social': {'instagram_username': 'resulmentes2', 'portfolio_url': 'http://resulmentes.com', 'twitter_username': 'resulmentess', 'paypal_email': None}}}}}]}
    print(f"imgs_json ({len(imgs_json)}):")
    # print(imgs_json)
    # print(f"imgs_json ({len(imgs_json)}):")
    print("imgs_json[0]")
    print(imgs_json[0])
    print(imgs_json[0]['urls']['full'])

    for i in range(perPage):  # 20
        print(i)
        name = imgs_json[i]['alt_description']
        if not name:
            import random
            numRand4 = random.randint(1111, 9999)
            name = q + "_image_" + str(i) + "_" + str(numRand4)
        filename = name.replace(" ", "_") + ".jpg"
        print(filename)
        url = imgs_json[i]['urls']['full']
        #
        download(
            imgUrl=url,
            savePath="z-IMAGES_1/!new/" + q.replace(" ","_"),
            imgFilename=filename
        )


    """
    keys in json_object:
        photos
        collections
        users
        related_searches
        meta
    """
    # for x in json_object.keys():
    # print(x)

    # full":"https://images.unsplash.com/photo-1526379095098-d400fd0bf935?crop=entropy\u0026cs=srgb\u0026fm=jpg\u0026ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8cHl0aG9ufHwwfHx8fDE2NDM2NzMzNzk\u0026ixlib=rb-1.2.1\u0026q=85



#--------------------------------------
# GOOGLE IMAGES below
#
#provide subjects:

# import ImageSAVER as saver
# saver.ImgSaverSTUDY()

def ImgSaverSTUDY():
    # save in different folder
    subjects = ["linux", "linux commands", "linux terminal", ]
    for subject in subjects:
        imageSaverStudy1("quick reference " + subject)
        imageSaverStudy1("quick start " + subject)
        imageSaverStudy1("cheat sheet " + subject)



"""
import ImageSAVER as saver
saver.imageSaver("premium wallpapers great snowy mountains",30)
saver.imageSaver("premium wallpapers green lush hills",30)
saver.imageSaver("premium wallpapers great mountains",30)
saver.imageSaver("premium wallpapers epic countrysides",30)
saver.imageSaver("premium wallpapers white clean apartment",30)
saver.imageSaver("premium wallpapers modern smart house",30)
"""


"""
# it takes the study topic and adds those 3, one of each
# and downloads your study graphics
# 90 images total in this one

import ImageSAVER as saver
saver.imageSaverStudy1(q="Study Topic", qty=30)
"""

def imageSaverStudy1(q="Study Topic...", save_num_images=30):
  #for ever one, it downloads 30 for 3:
  #Quick Reference, Quick Start, and Cheat Sheet
  import os
  import requests, lxml, re, json, urllib.request, datetime
  from bs4 import BeautifulSoup

  headers = {
      "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
  }

  params = {
      "tbm": "isch",
      "ijn": "0",
      "q": q,
      "qty": save_num_images,
  }

  html = requests.get("https://www.google.com/search", params=params, headers=headers)
  soup = BeautifulSoup(html.text, 'lxml')

  def get_google_images_data2():
      code1 = soup.select('.isv-r.PNCib.MSM1fd.BUooTd')
      print(f"len of code1: {len(code1)} ... {code1}")

  def get_google_images_data():
      # print('\nGoogle Images Metadata:')
      for google_image in soup.select('.isv-r.PNCib.MSM1fd.BUooTd'):
          title = google_image.select_one('.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['title']
          source = google_image.select_one('.fxgdke').text
          link = google_image.select_one('.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['href']
          # print(f'{title}\n{source}\n{link}\n')

      # this steps could be refactored to a more compact
      all_script_tags = soup.select('script')

      matched_images_data = ''.join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

      # if you try to json.loads() without json.dumps() it will throw an error:
      # "Expecting property name enclosed in double quotes"
      matched_images_data_fix = json.dumps(matched_images_data)
      matched_images_data_json = json.loads(matched_images_data_fix)

      matched_google_image_data = re.findall(r'\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",',
                                             matched_images_data_json)

      matched_google_images_thumbnails = ', '.join(
          re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                     str(matched_google_image_data))).split(', ')

      # print('Google Image Thumbnails:')  # in order
      for fixed_google_image_thumbnail in matched_google_images_thumbnails:
          google_image_thumbnail_not_fixed = bytes(fixed_google_image_thumbnail, 'ascii').decode('unicode-escape')

          # after first decoding, Unicode characters are still present. After the second iteration, they were decoded.
          google_image_thumbnail = bytes(google_image_thumbnail_not_fixed, 'ascii').decode('unicode-escape')
          # print(google_image_thumbnail)

      # removing previously matched thumbnails for easier full resolution image matches.
      removed_matched_google_images_thumbnails = re.sub(
          r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', '', str(matched_google_image_data))

      matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
                                                         removed_matched_google_images_thumbnails)
      import ProgressBAR as pb
      # pb.ProgressBAR(.1)

      # print('\nFull Resolution Images:')  # in order
      for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
          #print("index: ")
          print(index+1) #the image number - out of max 30

          #PROGRESS BAR - in terminal console - watch it
          #pb.ProgressBAR((index+1)/30) #pb.ProgressBAR(.1)

          original_size_img_not_fixed = bytes(fixed_full_res_image, 'ascii').decode('unicode-escape')
          original_size_img = bytes(original_size_img_not_fixed, 'ascii').decode('unicode-escape')
          #print(original_size_img)

          # ------------------------------------------------
          # Download original images

          # print(f'Downloading {index} image...')

          opener = urllib.request.build_opener()
          opener.addheaders = [('User-Agent',
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
          urllib.request.install_opener(opener)

          #print("urllib.request.urlretrieve(original_size_img, 'image1.jpg')")
          #print("original_size_img")
          #
          # THE LINK - in blue - in the console
          #print(original_size_img) #THE LINK - in blue - in the console

          image_search_query = params['q']
          quantity = params['qty']

          #print("folder_name")
          #print(folder_name)

          img_folder_path = "z-IMAGES-study/"+image_search_query.replace(" ","_")+"/"
          #print("img_folder_path")
          #print(img_folder_path)

          #make the folder if not exists yet
          isExist = os.path.exists(img_folder_path)
          if not isExist:
              os.mkdir(img_folder_path)

          img_num = index+1
          image_name = img_folder_path+image_search_query.replace(" ","_")+"_"+str(img_num)+".jpg"

          #it keeps going if it encounters an error:
          try:
              urllib.request.urlretrieve(original_size_img, image_name.replace(" ","_"))
          except:
              pass

          if index == quantity-1:
              break
              #exit()


  get_google_images_data()









# import ImageSAVER as saver
# saver.ImageSaver2(q="premium wallpapers", qty=30)

def ImageSaver2(q="premium wallpapers", save_num_images=30):
  import os
  import requests, lxml, re, json, urllib.request, datetime
  from bs4 import BeautifulSoup

  headers = {
      "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
  }

  params = {
      "tbm": "isch",
      "ijn": "0",
      "q": q,
      "qty": save_num_images,
  }

  html = requests.get("https://www.google.com/search", params=params, headers=headers)
  soup = BeautifulSoup(html.text, 'lxml')

  def get_google_images_data2():
      code1 = soup.select('.isv-r.PNCib.MSM1fd.BUooTd')
      print(f"len of code1: {len(code1)} ... {code1}")

  def get_google_images_data():
      # print('\nGoogle Images Metadata:')
      for google_image in soup.select('.isv-r.PNCib.MSM1fd.BUooTd'):
          title = google_image.select_one('.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['title']
          source = google_image.select_one('.fxgdke').text
          link = google_image.select_one('.VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb')['href']
          # print(f'{title}\n{source}\n{link}\n')

      # this steps could be refactored to a more compact
      all_script_tags = soup.select('script')

      matched_images_data = ''.join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

      # if you try to json.loads() without json.dumps() it will throw an error:
      # "Expecting property name enclosed in double quotes"
      matched_images_data_fix = json.dumps(matched_images_data)
      matched_images_data_json = json.loads(matched_images_data_fix)

      matched_google_image_data = re.findall(r'\[\"GRID_STATE0\",null,\[\[1,\[0,\".*?\",(.*),\"All\",',
                                             matched_images_data_json)

      matched_google_images_thumbnails = ', '.join(
          re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
                     str(matched_google_image_data))).split(', ')

      # print('Google Image Thumbnails:')  # in order
      for fixed_google_image_thumbnail in matched_google_images_thumbnails:
          google_image_thumbnail_not_fixed = bytes(fixed_google_image_thumbnail, 'ascii').decode('unicode-escape')

          # after first decoding, Unicode characters are still present. After the second iteration, they were decoded.
          google_image_thumbnail = bytes(google_image_thumbnail_not_fixed, 'ascii').decode('unicode-escape')
          # print(google_image_thumbnail)

      # removing previously matched thumbnails for easier full resolution image matches.
      removed_matched_google_images_thumbnails = re.sub(
          r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', '', str(matched_google_image_data))

      matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
                                                         removed_matched_google_images_thumbnails)
      import ProgressBAR as pb
      # pb.ProgressBAR(.1)

      # print('\nFull Resolution Images:')  # in order
      for index, fixed_full_res_image in enumerate(matched_google_full_resolution_images):
          #print("index: ")
          # print(index+1) #the image number - out of max 30

          #PROGRESS BAR - in terminal console - watch it
          pb.ProgressBAR((index+1)/30) #pb.ProgressBAR(.1)

          original_size_img_not_fixed = bytes(fixed_full_res_image, 'ascii').decode('unicode-escape')
          original_size_img = bytes(original_size_img_not_fixed, 'ascii').decode('unicode-escape')
          #print(original_size_img)

          # ------------------------------------------------
          # Download original images

          # print(f'Downloading {index} image...')

          opener = urllib.request.build_opener()
          opener.addheaders = [('User-Agent',
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
          urllib.request.install_opener(opener)

          #print("urllib.request.urlretrieve(original_size_img, 'image1.jpg')")
          #print("original_size_img")
          #
          # THE LINK - in blue - in the console
          #print(original_size_img) #THE LINK - in blue - in the console

          image_search_query = params['q']
          quantity = params['qty']

          #print("folder_name")
          #print(folder_name)

          img_folder_path = "z-IMAGES_1/"+image_search_query.replace(" ","_")+"/"
          #print("img_folder_path")
          #print(img_folder_path)

          #make the folder if not exists yet
          isExist = os.path.exists(img_folder_path)
          if not isExist:
              os.mkdir(img_folder_path)

          img_num = index+1
          image_name = img_folder_path+image_search_query.replace(" ","_")+"_"+str(img_num)+".jpg"

          #it keeps going if it encounters an error:
          try:
              urllib.request.urlretrieve(original_size_img, image_name.replace(" ","_"))
          except:
              pass

          if index == quantity-1:
              break
              #exit()


  get_google_images_data()

