def hallo():
    print("Ciao")

hallo()

def Level_1 ():
    done = False
    while not done:
        antwort_1 = int(input("Was gibt 2 + 2?")) 
        if antwort_1 == 4:
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
        false_counter = 0

Level_1 ()







    

