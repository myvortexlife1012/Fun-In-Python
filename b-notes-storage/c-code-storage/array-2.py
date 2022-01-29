#now I get an .input()
#and then it will check to see if that string is present
#-and then output the response
#--if it is a function--it will run the function


#------------

import datetime

convos = {

    'convo-1': [{

        1: [({1: 'hello', 2: 'hi', }), ('hello'), ],
        2: [({1: 'how are you', 2: 'how are you doing', }), ('I am fine'), ],
        3: [({1: 'your day going well', 2: 'yes, very well, thank you', }), ('yes, very well, thank you'), ],
    }],

    'convo-2': [{
        1: [({1: 'Jarvis'}), ('Yes, what can I do?'), ],
        2: [({1: 'hey Jarvis'}), ('Yes, what is it?'), ],
        3: [({1: "I'm talking to you Jarvis"}), ("I know, I'm right here"), ],
        4: [({1: 'your day going well', 2: 'yes, very well, thank you', }), ('yes, very well, thank you'), ],
    }],

    'convo-3': [{
        1: [({1: 'who are you', 2: 'who are you jarvis', 3: 'tell me about yourself',
              4: 'tell me about yourself jarvis'}),
            ("Hello, I am Jarvis Your AI Asisstant. I am smallish in size. I am logical. I'm here for you."), ],
    }],

    'convo-4': [{
        1: [({1: 'I did say chocolate', }), ('I thought you did. Do you like it?'), ],
        2: [({1: 'I like chocolate', 2: 'yea I like chocolate', 3: 'do you like chocolate'}),
            ('did you say chocolate?'), ],
        3: [({1: 'yea i said chocolate'}), ('do you like chocolate?'), ],
        4: [({1: 'what type of chocolate'}), ('The good kinds.'), ],
        5: [({1: 'you like chocolate'}), ('did you say chocolate? I could go for some right now'), ],
        6: [({1: 'did you say chocolate'}), ("Yes I said it. it's good."), ],
        7: [({1: 'do you like chocolate or do i like chocolate'}), ('We both might like it'), ],
        8: [({1: 'favorite food', 2: 'what is your favorite food'}), ('I like chocolate'), ],
        9: [({1: 'are you sure'}), ('Yes, I like chocolate'), ],
        10: [({1: 'how sure are you'}), ('Quite a bit actually, chocolate is really good'), ],
        11: [({1: 'how many ways do you like chocolate'}),
             ('too many to count, but we will start with 17 - chocolate is just so good'), ],
    }],

    # look up a map
    'convo-5': [{
        1: [({1: 'Where is...'}), ('You want me to pull up a google map?'), ],
    }],

    # look up info on a subject
    # '...' means - it removes those words, and processes after
    # '...' means it notices the first part - and processes the function - on the rest of the sentence
    # --------
    'convo-6': [{
        1: [({1: 'What is...', 2: 'Look up info on...'}), ('You want me to pull up wikipedia?'), ],
    }],

    # time
    'convo-7': [{
        1: [({1: 'what time is it'}), ('_function', 'time1()',), ],
    }],

    # date
    'convo-8': [{
        1: [(
            {1: 'what day is it', 2: 'what day of the week is it', 3: "what's the date today", 4: "what's today's date",
             5: "what's the date", 6: 'what date is it'}), ('_function', 'date1()',), ],
    }],

    # close program
    'convo-9': [{
        1: [({1: 'turn off', 2: 'exit', 3: 'close', 4: 'close program', 5: 'close it down', 6: 'close please',
              7: 'close it', 8: 'shutdown please', 9: 'shutdown', 10: 'shut down', 11: 'shut it down',
              12: "Ok I'm done right now", 13: "Ok I'm done for now", 14: "Ok I'm done", 15: "I'm done",
              16: "I'm done for now", 17: "I'm done right now"}),
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
    print(str(x)+") convos['"+index_name+"'] =>")
    array_small = convos[index_name]
    print(array_small) #name of the entry - is convo-8


