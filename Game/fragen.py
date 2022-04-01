# Counters
false_counter = 0
skip_counter = 0

# LEVEL 1
def Level_1 ():
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

#Level_1()
#print(f"Du hast bisher {skip_counter}-mal geskippt.")
"""
def Level_2():
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
                    else: 
                        print ("GAME OVER")
                        exit #Marco hat gesagt, bei Game Over exit
                        done = True
            else:
                print("Falsch, versuch nocheinmal")



#Level_2()
#print(f"Du hast schon {skip_counter}-mal geskipped!")
"""
#möglichst wenige Wiederholungen
#Variabelnamen--> wie aussagekräftig, verständlich, sinnvoll

def Level_allg(falsch, gameover, skip, level1, frage1, antwort1, richtig1, tipp1, level2, frage2, antwort2, richtig2, tipp2, level3, frage3, antwort3, richtig3, tipp3, level4, frage4, antwort4, richtig4, tipp4, level5, frage5, antwort5, richtig5, tipp5, level6, frage6, antwort6, richtig6, tipp6):
    print("Willkommen zu Level Nr.")
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
                print("Du bekommst einen Tipp: 5+1")
            elif false_counter == 3:
                    if skip_counter == 0: 
                        print("Skip zu Level Nr. 3")
                        skip_counter = skip_counter +1
                    else: 
                        print ("GAME OVER")
                        exit #Marco hat gesagt, bei Game Over exit
                        done = True
            else:
                print("Falsch, versuch nocheinmal")

#Parameter
#allg. Parameter
falsch= "Falsch! Versuhe noch einmal"
gameover = "gameover!"
skip= "Skip zum nächsten Level"

#Level_1_Parameter
level1 = "Willkommen zum ersten Level"
frage1= "1+1=?"
antwort1="2"
richtig1= "Richtig! Hier der erste Hinweis: Dein Vater ist 65 Jahre alt."
tipp1= " Du erhälst nun einen Tipp: ?=2+0 "

#Level_2_Parameter
level2 = "Hier das nächste Level:"
frage2 = "2+2=?"
antwort2 = "4"
richtig2 = "Richtig! Hier der zweite Hinweis: Dein Vater hat braun-graue Haare, blaue Augen, trägt einen Bart und ist eher klein."
tipp2 = "Du erhälst nun einen Tipp: ?=4+0"

#Level_3_Parameter
level3 = "Erarbeite die hier deinen nächsten Hinweis"
frage3 = "3+3=?"
antwort3 = "6"
richtig3 = "Richtig! Hier der dritte Hinweis: Der Name deines Vaters ist Roland Müller"
tipp3 = "Du erhälst nun einen Tipp: ?=6+0"

#Level_4_Parameter
level4 = "level4"
frage4 = "4+4=?"
antwort4 = "8"
richtig4 = "Bravo! Durch deine Mühe erfährst du den nächsten Hinweis: Roland war der Arbeitskollege deiner Mutter."
tipp4 = "Du erhälst nun einen Tipp: ?=7+0"

#Level_5_Parameter
level5 = "finde in Level fünf den Wohnort deines Vaters heraus!"
frage5 = "5+5=?"
antwort5 = "10"
richtig5 = "Richtig! Hier der dritte Hinweis: Roland wohnt im moment in Berlin"
tipp5 = "Du erhälst nun einen Tipp: ?=8+0"

#Level_6_Parameter
level6 = "Endspurt! Erarbeite dir hier den letzen wichtigen Hinweis!"
frage6 = "6+6=?"
antwort6 = "12"
richtig6 = "Richtig! Hier der dritte Hinweis: Beruflich ist er als Informtiker tätig"
tipp6 = "Du erhälst nun einen Tipp: ?=9+0"






def Level_7():
    print("Level Nr.7")
    global false_counter
    global skip_counter
    done = False
    false_counter = 0
    while not done:
        antwort_7 = (input("Wer ist dein Vater, wähle zwischen diesen Optionen aus? a) gross, blond b)klein blond...?")) 
        if antwort_7 == "a":
            print("Richtig, dies ist tatsächlich dein Vater")
            done = True
        else :
            false_counter = false_counter + 1
            if false_counter == 2:
                print("Dies ist leider nicht dein Vater -> GAME OVER")
                exit
                done = True    
            else:
                print("Falsch, versuch nocheinmal")









    

