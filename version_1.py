# Counters
false_counter = 0
skip_counter = 0

# Level 1
def level_1 ():
    print("Level Nr.1")
    global false_counter
    global skip_counter
    done = False
    while not done:
        antwort_1 = input("Was gibt 2 + 2?")
        if antwort_1 == "4":
            print("Richtig, den Hinweis, den du dir erarbeitet hast ist xxx.")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Du bekommst einen Tipp")
                print("Tipp: 5-1")
            elif false_counter == 3:
                    print("Skip zum nächsten Level Nr. 2")
                    skip_counter = skip_counter +1
                    done = True
            else:
                print("Falsch, versuch nocheinmal")

#level_1()

# Level 2
def level_2():
    print("Level Nr.2")
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort_2 = (input("Was gibt 3 + 3?")) 
        if antwort_2 == "6":
            print("Richtig, den Hinweis, den du dir erarbeitet hast ist xxx.")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Du bekommst einen Tipp")
                print("Tipp: 5+1")
            elif false_counter == 3:
                    if skip_counter == 0: 
                        print("Skip zu Level Nr. 3")
                        skip_counter = skip_counter +1
                        done = True
                    else: 
                        print ("GAME OVER")
                        done = True
                        exit() #Marco hat gesagt, bei Game Over exit
                        
            else:
                print("Falsch, versuch nocheinmal")

#level_2()

# Level 3
def level_3():
    print("Level Nr.3")
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort_3 = (input("Was gibt 4 + 4?")) 
        if antwort_3 == "8":
            print("Richtig, den Hinweis, den du dir erarbeitet hast ist xxx.")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Du bekommst einen Tipp")
                print("Tipp: 5+3")
            elif false_counter == 3:
                    if skip_counter == 0: 
                        print("Skip zu Level Nr. 4")
                        skip_counter = skip_counter +1
                        done = True
                    else: 
                        print ("GAME OVER")
                        done = True
                        exit() 
                        
            else:
                print("Falsch, versuch nocheinmal")
        
#level_3()

# Level 4
def level_4():
    print("Level Nr.4")
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort_4 = (input("Was gibt 5 + 5?")) 
        if antwort_4 == "10":
            print("Richtig, den Hinweis, den du dir erarbeitet hast ist xxx.")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Du bekommst einen Tipp")
                print("Tipp: 11-1")
            elif false_counter == 3:
                    if skip_counter == 0: 
                        print("Skip zu Level Nr. 5")
                        skip_counter = skip_counter +1
                        done = True
                    else: 
                        print ("GAME OVER")
                        done = True
                        exit() 
                        
            else:
                print("Falsch, versuch nocheinmal")

#level_4()

# Level 5
def level_5():
    print("Level Nr.5")
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort_5 = (input("Was gibt 6 + 6?")) 
        if antwort_5 == "12":
            print("Richtig, den Hinweis, den du dir erarbeitet hast ist xxx.")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Du bekommst einen Tipp")
                print("Tipp: 13-1")
            elif false_counter == 3:
                    if skip_counter == 0: 
                        print("Skip zu Level Nr. 6")
                        skip_counter = skip_counter +1
                        done = True
                    else: 
                        print ("GAME OVER")
                        done = True
                        exit() 
                        
            else:
                print("Falsch, versuch nocheinmal")

#level_4()

# Level 6
def level_6():
    print("Level Nr.6")
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort_6 = (input("Was gibt 7 + 7?")) 
        if antwort_6 == "14":
            print("Richtig, den Hinweis, den du dir erarbeitet hast ist xxx.")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Du bekommst einen Tipp")
                print("Tipp: 15-1")
            elif false_counter == 3:
                    if skip_counter == 0: 
                        print("Skip zu Level Nr. 7")
                        skip_counter = skip_counter +1
                        done = True
                    else: 
                        print ("GAME OVER")
                        done = True
                        exit() 
                        
            else:
                print("Falsch, versuch nocheinmal")

#level_6()

# Level 7
def level_7():
    global false_counter
    global skip_counter
    if skip_counter >1:
        exit()
    else:   
        print("Level Nr.7")
        done = False
        false_counter = 0
        while not done:
            antwort_7 = (input("Wer ist dein Vater, wähle zwischen diesen Optionen aus? a) gross, blond b)klein blond...?")) 
            if antwort_7 == "a":
                print("Richtig, dies ist tatsächlich dein Vater.")
                print("Das Game ist hier zu Ende, VIELEN DANK fürs spielen")
                done = True
                exit()
            else :
                false_counter = false_counter + 1
                if false_counter == 2:
                    print("Dies ist leider nicht dein Vater -> GAME OVER")
                    done = True  
                    exit()
                    
                else:
                    print("Falsch, versuch nocheinmal")

#level_7()


import levels
levels.level_1()
levels.level_2()
levels.level_3()
levels.level_4()
levels.level_5()
levels.level_6()
levels.level_7()