---
title: "Shell Chat"
layout: post
published: true
categories: showcase shivam
---

> Chat with this Python program written by Shivam. It doesn't use a GUI, so you'll get to use the shell!

> The file can be downloaded [here](/files/showcase/Shivam/python_shell_chat.py)

> You can see the code that went into it below:

    import time
    print('hello what is your name')
    answer1=raw_input()
    print('hello ' + answer1)
    time.sleep(1)
    print('Hi im bob nice to meet you')
    time.sleep(2)
    print('What is you favourite subject?')
    answer=raw_input()
    print('hey i like ' +answer)
    time.sleep(1.5)
    print('why do you like it')
    answer=raw_input()
    time.sleep(1)
    if answer=='im good at it':
        print('wow thats the same for me :)')
    else:
        print('well my reason is definitely not ' +answer)
        time.sleep(2.5)
        print('i like it because i am good at it :)')
        time.sleep(2.5)
        
    print('do you like video games' +answer1)
    answer=raw_input()
    if answer =='yes':
        print('me too, people use my type of software to make them;)')
    
    else:
        print('i dont that much, but people do use me too make them hahahaha')
        time.sleep(2)
    
    print('shall we play naughts and crosses ' + answer1)
    
    answer=raw_input()
    if answer=="yes":
        print('ok')
        import Python_naughts_and_crosses.py
    else:
        print('ok then be like that...')
        time.sleep(1)
        print('just kidding')
        time.sleep(1)
    
    print('shall we play my version of rock paper scissors?')
    
    answer=raw_input()
    if answer=='yes':
        print('ok')
        import Python_BLUE_RED_GREEN.py
    else:
        print('alright then')
