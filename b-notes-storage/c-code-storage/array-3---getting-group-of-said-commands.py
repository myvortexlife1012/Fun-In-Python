#now I get an .input()
#and then it will check to see if that string is present
#-and then output the response
#--if it is a function--it will run the function


#------------

import datetime

convos = {

    'convo-1': [{

        0: [({0: 'hello', 1: 'hi', }), ('hello'), ],
        1: [({0: 'how are you', 1: 'how are you doing', }), ('I am fine'), ],
        2: [({0: 'your day going well', 1: 'yes, very well, thank you', }), ('yes, very well, thank you'), ],
    }],

    'convo-2': [{
        0: [({0: 'Jarvis'}), ('Yes, what can I do?'), ],
        1: [({0: 'hey Jarvis'}), ('Yes, what is it?'), ],
        2: [({0: "I'm talking to you Jarvis"}), ("I know, I'm right here"), ],
        3: [({0: 'your day going well', 1: 'yes, very well, thank you', }), ('yes, very well, thank you'), ],
    }],

    'convo-3': [{
        0: [({0: 'who are you', 1: 'who are you jarvis', 2: 'tell me about yourself',
              3: 'tell me about yourself jarvis'}),
            ("Hello, I am Jarvis Your AI Asisstant. I am smallish in size. I am logical. I'm here for you."), ],
    }],

    'convo-4': [{
        0: [({0: 'I did say chocolate', }), ('I thought you did. Do you like it?'), ],
        1: [({0: 'I like chocolate', 1: 'yea I like chocolate', 2: 'do you like chocolate'}),
            ('did you say chocolate?'), ],
        2: [({0: 'yea i said chocolate'}), ('do you like chocolate?'), ],
        3: [({0: 'what type of chocolate'}), ('The good kinds.'), ],
        4: [({0: 'you like chocolate'}), ('did you say chocolate? I could go for some right now'), ],
        5: [({0: 'did you say chocolate'}), ("Yes I said it. it's good."), ],
        6: [({0: 'do you like chocolate or do i like chocolate'}), ('We both might like it'), ],
        7: [({0: 'favorite food', 1: 'what is your favorite food'}), ('I like chocolate'), ],
        8: [({0: 'are you sure'}), ('Yes, I like chocolate'), ],
        9: [({0: 'how sure are you'}), ('Quite a bit actually, chocolate is really good'), ],
        10: [({0: 'how many ways do you like chocolate'}),
             ('too many to count, but we will start with 17 - chocolate is just so good'), ],
    }],

    # look up a map
    'convo-5': [{
        0: [({0: 'Where is...'}), ('You want me to pull up a google map?'), ],
    }],

    # look up info on a subject
    # '...' means - it removes those words, and processes after
    # '...' means it notices the first part - and processes the function - on the rest of the sentence
    # --------
    'convo-6': [{
        0: [({0: 'What is...', 1: 'Look up info on...'}), ('You want me to pull up wikipedia?'), ],
    }],

    # time
    'convo-7': [{
        0: [({0: 'what time is it'}), ('_function', 'time1()',), ],
    }],

    # date
    'convo-8': [{
        0: [(
            {0: 'what day is it', 1: 'what day of the week is it', 2: "what's the date today", 3: "what's today's date",
             4: "what's the date", 5: 'what date is it'}), ('_function', 'date1()',), ],
    }],

    # close program
    'convo-9': [{
        0: [({0: 'turn off', 1: 'exit', 2: 'close', 3: 'close program', 4: 'close it down', 5: 'close please',
              6: 'close it', 7: 'shutdown please', 8: 'shutdown', 9: 'shut down', 10: 'shut it down',
              11: "Ok I'm done right now", 12: "Ok I'm done for now", 13: "Ok I'm done", 14: "I'm done",
              15: "I'm done for now", 16: "I'm done right now"}),
            ('_function', 'exit()',), ],
    }],

}


# -----functions-----
def time1():
    import datetime
    str = datetime.datetime.now().strftime('%-I:%M %p')
    # 5:03 AM
    # talk(str)


def date1():
    date1 = datetime.datetime.now().strftime('%A, %B %d, %Y')
    time1 = datetime.datetime.now().strftime('%-I:%M %p')
    str = "It's " + date1 + ' and the time is ' + time1
    # It's Sunday, October 03, 2021 and the time is 5:01 AM
    # talk(str)
# -----functions-----



#input1 = input("Type a convo starter: ")
#print(input1)


#print(convos)


''' increase value of all items by 1
foreach ($array as $k => &$v) {
    $v++;
}
I know only this way, which is not so elegant:
'''
array_big = convos

#foreach($array_big as $x,$index_name=>$array_small)
for x, index_name in enumerate(array_big):
    #print("x: "+str(x))
    #print("index_name: "+index_name)
    print("\n\n\n"+str(x)+") convos['"+index_name+"'] =>")
    array_small = convos[index_name]

    said_commands_group = array_small[0][0][0] #use [0]-[10+] to access it
    print(said_commands_group)

    result_or_functions_group = array_small[0][0][1]  # use [0]-[10+] to access it
    print("---answer---")
    print(result_or_functions_group)

    length = len(said_commands_group)
    print(length)

    if len(said_commands_group)>1:
        print("listing single commands: ")
        for n in range(len(said_commands_group)):
            print("cmd: "+str(n))
            print(said_commands_group[n])

'''
    for n in range(len(said_commands_group)):
        cmd1 = said_commands_group[n] # always a string
        print(cmd1)
    #has the result ... if it's an answer, it's a string ... if it's an array - it's a function
    #print(array_small[0][1][1])

    #i got to the single - command - area
'''

