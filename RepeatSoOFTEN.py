#v1

#--- add in a way so it only gets a new background if the right arrow is pressed
# python if right arrow is pressed
#
#repeat every 5 minutes, or other timeframe
#put what you want it to do in - the - repeating_function()

# import RepeatSoOFTEN as repeat
# repeat.RepeatSoOFTEN() #runs what is in the module file

def RepeatSoOFTEN(): # 60*5 #60x#=#minutes ... #2 #60
    import sched, time
    schedule = sched.scheduler(time.time, time.sleep)
    # SET THE SECONDS TO REPEAT IT - **HERE** (1 of 2):
    every_so_many_seconds = 2 #set this below as well - 2 places


    def timestamp():
        import time # using time module
        ts = time.time() # ts stores the time in seconds
        #print() # print the current timestamp
        print(f"Current Timestamp: {ts}")

    #SET THE SECONDS TO REPEAT IT - **HERE** (2 of 2):
    def repeating_function(schedule,every_so_many_seconds=5):  #set this above as well - 2 places
        # registers or schedules - this function as the function
        schedule.enter(every_so_many_seconds, 1, repeating_function, (schedule,))
        #print("\nStarting the Repeating Function")
        #print(f"\nScheduling it to Repeat Every -{every_so_many_seconds}- second(s):")
        timestamp()

#if -------
        # Change the background automatically
        import listAllFILES as lfs
        folder_path = "z-IMAGES_1/0.cool"
        array = lfs.listAllFILES(folder_path)
        length = array[0]
        pics = array[1]

        import BackgroundChooseRANDOM as bgcrand
        bgcrand.BackgroundChooseRANDOM(array)

    #calls the repeating_function() function
    schedule.enter(every_so_many_seconds, 1, repeating_function, (schedule,every_so_many_seconds,))
    schedule.run()
