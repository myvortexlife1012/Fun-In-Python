#v6


#provide subjects:

def ImgSaverSTUDY():
    # save in different folder
    subjects = ["linux", "linux commands", "linux terminal", ]
    for subject in subjects:
        imageSaverStudy1("quick reference " + subject)
        imageSaverStudy1("quick start " + subject)
        imageSaverStudy1("cheat sheet " + subject)


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
# it takes the study topic and adds those 3, one of each
# and downloads your study graphics
# 90 images total in this one

import ImageSAVER as is1
subject = "linux" # "linux commands"
is1.imageSaverStudy(q)
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







def ImageSaver2(q="beautiful wallpapers...", save_num_images=30):
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

