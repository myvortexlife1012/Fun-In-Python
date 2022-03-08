#v6
"""
import ImagePathSEER as ips
ips.imagePathSeer("z-IMAGES_1/0.cool")
"""

def imagePathSeer(path=""):
    import os
    path = "z-IMAGES_1/0.cool"
    folders = os.listdir(path)
    print("\nfolders:")
    print(folders)

    print("\ndoing a loop\n")

    for folder in folders:
        path1 = path + "/" + folder
        print("folder: " + path1 + "/")
        print("--get-directory-contents--")
        folders1 = os.listdir(path1)
        # print("\nfolders1:")
        # print(folders1)
        for file in folders1:
            path2 = path1 + "/" + file
            print("path2: " + path2)

    print("end of file directory list")