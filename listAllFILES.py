print("Going to list all files!")

"""
lists all files
- relative to (from WITHIN) the python project folder
"""
def listAllFILES(folder_name):
    import os, sys
    project_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    #print("Hello, here is the project_path: " + project_path)
    #print("Hello, here is the folder_path: " + folder_path)
    paths_joined = os.path.join(project_path, folder_name)
    #print("Hello, here is the paths_joined: " + paths_joined)
    #print("\n------------------------------\n")

    pics = [] #empty list
    for path, subdirs, files in os.walk(paths_joined):
        for name in files:
            pic = os.path.join(path, name)
            #print(pic)
            pics.append(pic)
    #print("Files LIST:")
    #print("Number of files in the list = ", len(pics))
    #print(pics)
    return [len(pics), pics]


