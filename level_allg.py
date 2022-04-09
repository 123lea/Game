def level_allg(level):
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
                        done = True
                        exit() 
                        
            else:
                print("Falsch, versuch nocheinmal")



#Parameter
#allg. Parameter
falsch= "Falsch! Versuhe noch einmal"
gameover = "gameover!"
skip= "Skip zum nächsten Level"

#Level_1_Parameter
einführung1 = "Willkommen zum ersten Level"
frage1= "1+1=?"
antwort1="2"
richtig1= "Richtig! Hier der erste Hinweis: Dein Vater ist 65 Jahre alt."
tipp1= " Du erhälst nun einen Tipp: ?=2+0 "

#Level_2_Parameter
einführung2 = "Hier das nächste Level:"
frage2 = "2+2=?"
antwort2 = "4"
richtig2 = "Richtig! Hier der zweite Hinweis: Dein Vater hat braun-graue Haare, blaue Augen, trägt einen Bart und ist eher klein."
tipp2 = "Du erhälst nun einen Tipp: ?=4+0"

#Level_3_Parameter
einführung3 = "Erarbeite die hier deinen nächsten Hinweis"
frage3 = "3+3=?"
antwort3 = "6"
richtig3 = "Richtig! Hier der dritte Hinweis: Der Name deines Vaters ist Roland Müller"
tipp3 = "Du erhälst nun einen Tipp: ?=6+0"

#Level_4_Parameter
einführung4 = "level4"
frage4 = "4+4=?"
antwort4 = "8"
richtig4 = "Bravo! Durch deine Mühe erfährst du den nächsten Hinweis: Roland war der Arbeitskollege deiner Mutter."
tipp4 = "Du erhälst nun einen Tipp: ?=7+0"

#Level_5_Parameter
einführung5 = "finde in Level fünf den Wohnort deines Vaters heraus!"
frage5 = "5+5=?"
antwort5 = "10"
richtig5 = "Richtig! Hier der dritte Hinweis: Roland wohnt im moment in Berlin"
tipp5 = "Du erhälst nun einen Tipp: ?=8+0"

#Level_6_Parameter
einführung6 = "Endspurt! Erarbeite dir hier den letzen wichtigen Hinweis!"
frage6 = "6+6=?"
antwort6 = "12"
richtig6 = "Richtig! Hier der dritte Hinweis: Beruflich ist er als Informtiker tätig"
tipp6 = "Du erhälst nun einen Tipp: ?=9+0"



levels = [
    #LEVEL 1    
    {
        "level": "Willkommen zum ersten Level",
        "frage":"1+1=?",
        "antwort": "2",
        "richtig": "Richtig! Hier der erste Hinweis: Dein Vater ist 65 Jahre alt.",
        "tipp":"Du erhälst nun einen Tipp: ?=2+0"
    },

    # LEVEL 2
    {
        "level": "Hier das nächste Level:",
        "frage":"2+2=?",
        "antwort": "4",
        "richtig": "Richtig! Hier der zweite Hinweis: Dein Vater hat braun-graue Haare, blaue Augen, trägt einen Bart und ist eher klein.",
        "tipp":"Du erhälst nun einen Tipp: ?=4+0"
    },

    # LEVEL 3
    {
        "level": "Erarbeite die hier deinen nächsten Hinweis",
        "frage":"3+3=?",
        "antwort": "6",
        "richtig": "Richtig! Hier der dritte Hinweis: Der Name deines Vaters ist Roland Müller",
        "tipp":"Du erhälst nun einen Tipp: ?=6+0"
    }, 

    # LEVEL 4
    {
        "level": "evel4",
        "frage":"4+4=?",
        "antwort": "8",
        "richtig": "Bravo! Durch deine Mühe erfährst du den nächsten Hinweis: Roland war der Arbeitskollege deiner Mutter.",
        "tipp":"Du erhälst nun einen Tipp: ?=8+0"
    },

    # LEVEL 5
     {
        "level": "finde in Level fünf den Wohnort deines Vaters heraus!",
        "frage":"5+5=?",
        "antwort": "10",
        "richtig": "Richtig! Hier der dritte Hinweis: Roland wohnt im moment in Berlin",
        "tipp":"Du erhälst nun einen Tipp: ?=10+0"
    },

    # LEVEL 6
    {
        "level": "Endspurt! Erarbeite dir hier den letzen wichtigen Hinweis!",
        "frage":"6+6=?",
        "antwort": "12",
        "richtig": "Richtig! Hier der dritte Hinweis: Beruflich ist er als Informtiker tätig",
        "tipp":"Du erhälst nun einen Tipp: ?=12+0"
    }
]


for level in levels:
    level_allg(level)