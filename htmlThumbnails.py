#v1
"""
import htmlThumbnails as thumbnails
thumbnails.makeHTMLforImages(folder_name="premium_wallpapers_great_mountains")
"""
#it makes the html file - in the current directory - as absolute file links
#2nd version will make it relative links

def makeHTMLforImages(folder_name="premium_wallpapers_great_mountains"):
    # make html file for this

    # Change the background automatically
    import listAllFILES as lfs
    folder_path = "z-IMAGES_1/0.cool/"+ folder_name
    html_file = folder_path + "/!imageList.html"
    array = lfs.listAllFILES(folder_path)
    length = array[0]
    pics = array[1]  # pic paths

    html = "<div style='border:1px red dashed; width:800px; margin:100px; padding:20px;'>"
    for pic in pics:
        html += "\n <a href='" + pic + "'><img src='" + pic + "' height='100' width='100' /></a>"
    html += "</div>"

    print(f"pics - length({length}):")
    print(pics)

    print("html:")
    print(html)

    # Write HTML String to file.html
    with open(html_file, "w") as file:
        file.write(html)


