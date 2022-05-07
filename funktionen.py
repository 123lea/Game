#counters
false_counter = 0
skip_counter = 0

def level_allg(level):
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    print(f"{level['einführung']}")
    while not done:
        antwort = (input(f"{level['frage']}"))
        antwort = antwort.lower()
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
        print("Toll, du weisst jetzt schon einiges über deinen Vater und hast bestimmt schon gemerkt, dass es nicht der Mann deiner Mutter ist.\nIm letzten Level kannst du dir die Telefonnummer erarbeiten und ihn anschliessend anrufen.")
        done = False
        false_counter = 0
        while not done:
            antwort_7 = (input("Hoffentlich hast du meinen Tipp zu beginn des Spieles ernst genommen und dir die Hinweise gemerkt.\nDeine letzte Aufgabe ist es, die richtige Person auszuwählen.\nGib dazu bloss 'a' , 'b' oder 'c' ein:\na) Roland wohnt aktuell am Nil\nb) Roland ist klein und ein Weltenbummler\nc) Er spielt sowohl Fussball als auch Klavier.\n"))
            if antwort_7 == "b":
                print("Richtig, dies ist tatsächlich dein Vater.")
                print("Gratuliere! Hier die Handynummer: xxx xxx xx xx\nDanke fürs Mitspielen!")
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













