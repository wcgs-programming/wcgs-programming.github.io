---
title: "Factor/Multiple Checker"
layout: post
published: true
categories: showcase bertie
---

> This short Python program by Bertie checks whether one number is a multiple of another.
> You can download it [here](/files/showcase/Bertie/factor-multiple-checker.py).

> Take a look at the code:

    import time

    print("Multiple Finder  --  TM (r)(c) Bertie 2014")

    x = int(raw_input("x: "))
    y = int(raw_input("y: "))

    if y % x == 0:
        print("Y is a multiple of X")
        print("Copyright (c) Bertie Auricchio 2014 T&C's apply")
    else:
        print("Y is not a multiple of X")
        print("Copyright (c) Bertie Auricchio 2014 T&C's apply")

    time.sleep(3)
