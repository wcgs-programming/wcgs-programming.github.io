while 1:
    def e():
        

            string = raw_input("What do you want to encode? ")
            alphabet =  "abcdefghijklmnopqrstuvwxyz "
            calphabet = "qwertyuiopasdfghjklzxcvbnm/"
            ualphabet =  alphabet.upper()
            ucalphabet = calphabet.upper()
            estring = ""
            for i in string:
                k = ""
                j = 0
                while j<27:
                    if i == alphabet[j]:
                        k = calphabet[j]
                    if i == ualphabet[j]:
                        k = ucalphabet[j]
                    j = j+1
                estring = estring + k
            print estring

    def d():
        string = raw_input("What do you want to decode? ")
        alphabet =  "qwertyuiopasdfghjklzxcvbnm/"
        calphabet = "abcdefghijklmnopqrstuvwxys "
        ualphabet =  alphabet.upper()
        ucalphabet = calphabet.upper()
        estring = ""
        for i in string:
            k = ""
            j = 0
            while j<27:
                if i == alphabet[j]:
                    k = calphabet[j]
                if i == ualphabet[j]:
                    k = ucalphabet[j]
                j = j+1
            estring = estring + k
        print estring


    selection = raw_input("Encode or Decode. e/d ")
    if selection == "e":
        e()
    else:
        d()
