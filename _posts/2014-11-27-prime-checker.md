---
title: "Prime Checker"
layout: post
published: true
categories: showcase bertie
---

> Another short Python program by Bertie, to find the factorial of a certain number.
> You can download it [here](/files/showcase/Bertie/prime-checker.py).
> Take a look at the code:

    num=int(raw_input("What number do you want to test?"))
    ran=2
    add=0
    
    while num > ran:
        ran = ran + 1
        if num % ran == 0:
            add = add + 1
    if add == 1:
        print("OMG Its Prime!")
    else:
        print("Not Prime!")