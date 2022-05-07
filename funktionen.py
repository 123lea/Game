#counters
false_counter = 0
skip_counter = 0

import colorama
from colorama import Fore

def level_allg(level):
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    print(Fore.BLACK + f"{level['einführung']}")
    while not done:
        antwort = (input(Fore.BLACK + f"{level['frage']}"))
        antwort = antwort.lower()
        if antwort == (f"{level['antwort']}"):
            print(Fore.GREEN + f"{level['richtig']}")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 1:
                print(Fore.RED + f"{level['tipp']}")
            elif false_counter == 2:
                    if skip_counter == 0:
                        print(Fore.MAGENTA + "Skip zum nächsten Level. Achtung du kannst nun nicht mehr skippen!")
                        skip_counter = skip_counter +1
                        done= True
                    else:
                        print(Fore.RED + "GAME OVER")
                        print(Fore.BLACK + "")
                        done = True
                        exit()
          


def level_7():
    global false_counter
    global skip_counter
    if skip_counter >1:
        exit()
    else:  
        print(Fore.GREEN + "Toll, du weisst jetzt schon einiges über deinen Vater und hast bestimmt schon gemerkt, dass es nicht der Mann deiner Mutter ist.\nIm letzten Level kannst du dir die Telefonnummer erarbeiten und ihn anschliessend anrufen.")
        done = False
        false_counter = 0
        while not done:
            antwort_7 = (input(Fore.BLACK + "Hoffentlich hast du meinen Tipp zu beginn des Spieles ernst genommen und dir die Hinweise gemerkt.\nDeine letzte Aufgabe ist es, die richtige Person auszuwählen.\nDu hast nur einen Versuch!\nGib dazu bloss 'a' , 'b' oder 'c' ein:\na) Roland wohnt aktuell am Nil\nb) Roland ist klein und ein Weltenbummler\nc) Er spielt sowohl Fussball als auch Klavier.\n"))
            if antwort_7 == "b":
                print(Fore.GREEN + "Richtig, dies ist tatsächlich dein Vater.")
                print(Fore.GREEN + "Gratuliere! Hier die Handynummer: xxx xxx xx xx\nDanke fürs Mitspielen!")
                print(Fore.BLACK + "")
                done = True
                exit()
            else :
                false_counter = false_counter + 1
                if false_counter == 1:
                    print(Fore.RED + "Dies ist leider nicht dein Vater -> GAME OVER")
                    print(Fore.BLACK + "")
                    done = True  
                    exit()
                













