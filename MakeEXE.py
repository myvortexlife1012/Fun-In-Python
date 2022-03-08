
#-----------------------------

#FOR WINDOWS:

# make exe for the background change app

# (1)
# pip install auto-py-to-exe
# type 'auto-py-to-exe' in the console ... gui appears

#----------------------------

# (2)
# make exe for the background change app
# pip install pyinstaller
# pyinstaller --onefile hello.py # makes the exe file (in dist folder)
# pyinstaller --onefile reminders-on.py

#-----------------------------

#FOR LINUX:

"""
Just put this in the first line of your script :

#!/usr/bin/env python
Make the file executable with

chmod +x myfile.py
Execute with

./myfile.py


----

or

try  pyinstaller


"""