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