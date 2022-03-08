# import ProgressBAR as pb
# pb.ProgressBAR2(.1)
# pb.ProgressBAR(.1)



#-----------------



#v1
"""
# import ProgressBAR as pb
# pb.ProgressBAR(.1)

Required:
pip install update_progress  # gives you a text moving percentage, each time you run it
"""

def ProgressBAR(num=.1):
    import time, sys

    # update_progress() : Displays or updates a console progress bar
    ## Accepts a float between 0 and 1. Any int will be converted to a float.
    ## A value under 0 represents a 'halt'.
    ## A value at 1 or bigger represents 100%
    def update_progress(progress):
        barLength = 10  # Modify this to change the length of the progress bar
        status = ""
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
            status = "error: progress var must be float\r\n"
        if progress < 0:
            progress = 0
            status = "Halt...\r\n"
        if progress >= 1:
            progress = 1
            status = "Done...\r\n"
        block = int(round(barLength * progress))
        text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block), progress * 100, status)
        sys.stdout.write(text)
        sys.stdout.flush()

    #The Progress Bar - text - in console - updates for you
    print("")
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    update_progress(num)

    #print("progress : 0->1")
    """
    update_progress(0 / 100.0)
    time.sleep(0.2)
    update_progress(10 / 100.0)
    time.sleep(0.4)
    update_progress(25 / 100.0)
    time.sleep(0.4)
    update_progress(50 / 100.0)
    time.sleep(0.4)
    update_progress(75 / 100.0)
    time.sleep(0.4)
    update_progress(90 / 100.0)
    time.sleep(0.4)
    update_progress(100 / 100.0)
"""




#v1
"""
# import ProgressBAR as pb
# pb.ProgressBAR2(.1)

Required:
pip install update_progress  # gives you a text moving percentage, each time you run it --- broken
"""

def ProgressBAR2(num=.1):
    # !/usr/bin/env python
    import sys
    import PySimpleGUI as sg

    def MachineLearningGUI():
        sg.set_options(text_justification='right')

        flags = [[sg.CB('Normalize', size=(12, 1), default=True), sg.CB('Verbose', size=(20, 1))],
                 [sg.CB('Cluster', size=(12, 1)), sg.CB(
                     'Flush Output', size=(20, 1), default=True)],
                 [sg.CB('Write Results', size=(12, 1)), sg.CB(
                     'Keep Intermediate Data', size=(20, 1))],
                 [sg.CB('Normalize', size=(12, 1), default=True),
                  sg.CB('Verbose', size=(20, 1))],
                 [sg.CB('Cluster', size=(12, 1)), sg.CB(
                     'Flush Output', size=(20, 1), default=True)],
                 [sg.CB('Write Results', size=(12, 1)), sg.CB('Keep Intermediate Data', size=(20, 1))], ]

        loss_functions = [
            [sg.Rad('Cross-Entropy', 'loss', size=(12, 1)), sg.Rad('Logistic', 'loss', default=True, size=(12, 1))],
            [sg.Rad('Hinge', 'loss', size=(12, 1)),
             sg.Rad('Huber', 'loss', size=(12, 1))],
            [sg.Rad('Kullerback', 'loss', size=(12, 1)),
             sg.Rad('MAE(L1)', 'loss', size=(12, 1))],
            [sg.Rad('MSE(L2)', 'loss', size=(12, 1)), sg.Rad('MB(L0)', 'loss', size=(12, 1))], ]

        command_line_parms = [
            [sg.Text('Passes', size=(8, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),
             sg.Text('Steps', size=(8, 1), pad=((7, 3))),
             sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],
            [sg.Text('ooa', size=(8, 1)), sg.Input(default_text='6', size=(8, 1)), sg.Text('nn', size=(8, 1)),
             sg.Input(default_text='10', size=(10, 1))],
            [sg.Text('q', size=(8, 1)), sg.Input(default_text='ff', size=(8, 1)), sg.Text('ngram', size=(8, 1)),
             sg.Input(default_text='5', size=(10, 1))],
            [sg.Text('l', size=(8, 1)), sg.Input(default_text='0.4', size=(8, 1)), sg.Text('Layers', size=(8, 1)),
             sg.Drop(values=('BatchNorm', 'other'))], ]

        layout = [[sg.Frame('Command Line Parameteres', command_line_parms, title_color='green', font='Any 12')],
                  [sg.Frame('Flags', flags, font='Any 12', title_color='blue')],
                  [sg.Frame('Loss Functions', loss_functions,
                            font='Any 12', title_color='red')],
                  [sg.Submit(), sg.Cancel()]]

        sg.set_options(text_justification='left')

        window = sg.Window('Machine Learning Front End',
                           layout, font=("Helvetica", 12))
        button, values = window.read()
        window.close()
        print(button, values)

    def CustomMeter():
        # layout the form
        layout = [[sg.Text('A custom progress meter')],
                  [sg.ProgressBar(1000, orientation='h',
                                  size=(20, 20), key='progress')],
                  [sg.Cancel()]]

        # create the form`
        window = sg.Window('Custom Progress Meter', layout)
        progress_bar = window['progress']
        # loop that would normally do something useful
        for i in range(1000):
            # check to see if the cancel button was clicked and exit loop if clicked
            event, values = window.read(timeout=0, timeout_key='timeout')
            if event == 'Cancel' or event == None:
                break
            # update bar with loop value +1 so that bar eventually reaches the maximum
            progress_bar.update_bar(i + 1)
        # done with loop... need to destroy the window as it's still open
        window.CloseNonBlocking()

    #if __name__ == '__main__':
    CustomMeter()
    MachineLearningGUI()




