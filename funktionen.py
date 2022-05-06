#counters
false_counter = 0
skip_counter = 0

def level_allg(level):
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort = (input(f"{level['frage']}"))
        if antwort == (f"{level['antwort']}"):
            print(f"{level['richtig']}")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 1:
                print(f"{level['tipp']}")
            elif false_counter == 2:
                    if skip_counter == 0:
                        print("Skip zum nächsten Level")
                        skip_counter = skip_counter +1
                        done= True
                    else:
                        print ("GAME OVER")
                        done = True
                        exit()
            else:
                print("Falsch, versuch nocheinmal")


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
                if false_counter == 1:
                    print("Dies ist leider nicht dein Vater -> GAME OVER")
                    done = True  
                    exit()
                    
                else:
                    print("Falsch, versuch nocheinmal")














