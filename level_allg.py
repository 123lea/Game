#counters
false_counter = 0
skip_counter = 0

def level_allg(level):
    print(f"{level['level']}")
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
            if false_counter == 2:
                print(f"{level['tipp']}")
            elif false_counter == 3:
                    if skip_counter == 0:
                        print("Skip zum nächsten Level")
                        skip_counter = skip_counter +1
                        done= True
                    else:
                        print ("GAME OVER")
                        exit 
                        done = True
            else:
                print("Falsch, versuch nocheinmal")


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



level_allg (levels[0])
level_allg (levels[1])
level_allg (levels[2])
level_allg (levels[3])
level_allg (levels[4])
level_allg (levels[5])
