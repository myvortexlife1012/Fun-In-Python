#v3
#import sayTHIS as st
#st.sayTHIS() #defaults to "Hello World"

# Required:
# pip install pyttsx3

# Required First - Linux Only: (for voices to be available and this to work)
"""
sudo apt install espeak
sudo apt install libespeak1
"""

def sayTHIS(audio="Hello World"):
   print("Going to Say Something!")
   import pyttsx3
   engine = pyttsx3.init()
   engine.say(audio)
   engine.runAndWait()

def say(audio="Hello World"):
   sayTHIS(audio)

def talk(audio="Hello World"):
   sayTHIS(audio)

def speak(audio="Hello World"):
   sayTHIS(audio)
