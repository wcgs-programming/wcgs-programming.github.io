---
title: "Single Password Program"
layout: post
published: true
categories: showcase aaryan
---

> Only one person may enter this computer... and only if they know the correct password.

> If you look carefully at the code, you might be able to guess what the password is!

    import time

    username = raw_input("username: ")
    if username == "bob":
        print("Correct. Now type in your password.")
        password = raw_input("password: ")
        if password == "awesome":
            print("Correct. You may enter this computer.")
        else:
            print("Incorrect. Prepare for immediate destruction.")
    else:
        print("Incorrect. Prepare for immediate destruction.")

    time.sleep(5)

