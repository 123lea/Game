#import re
#print("Willkommen zum Game!")

#print("Du befindest dich in der grossen Halle. Wo möchtest du hingehen?")
#print("1 Links, 2 Rechts")

#zahlen_pattern = re.compile("[0-9]+")

#eingabe = input(">")
#print(type(eingabe))
#if zahlen_pattern.match(eingabe):
#    eingabe = int(eingabe)
#    if eingabe == 1:
#        print("Wir gehen nach links")
#    elif eingabe == 2:
#        print("Wir gehen nach rechts")
#    else:
#        print("falsche Antwort")
#else:
 #   print("keine Zahl")


##zweite Variante
#print("Willkommen zum Game!")

#print("""Du befindest dich in der grossen Halle. Wo möchtest du hingehen? 
#[L]inks, [R]echts""")

#done = False
#while not done:
    #eingabe = input(">")
    #if eingabe == "l":
        #print("Wir gehen nach links")
        #done = True
    #elif eingabe == "r":
        #print("Wir gehen nach rechts")
        #done = True
    #else:
        #print("nochmals")


#Einleitung
#name = input("""Willkommen zu "Wo ist mein Vater", wie heisst du?""")
#print(f"Hallo {name}!")

#print("""Du ziehst von den Eltern weg und mistest den Estrich aus. Plötzlich fällt dir eine Kiste in der dunklen Ecke auf. 
#Du entscheidest dich einen der vielen Briefe in der Kiste zu lesen und dabei erfährst du, dass dein Vater womöglich nicht dein biologischer Vater ist. Du bist völlig neben der Spur und nimmst die Kiste mit. 
#Du öffnest nach und nach mehr Briefe und erfährst immer mehr, bis du schlussendlich auf die Suche nach deinem Vater gehst.
#-	Nach jedem erfüllten Level erhältst du den Richtigen Brief, mit einer relevanten Information. Es gibt insgesamt 6 Rätsel, bei denen du Informationen sammeln kannst. Hast du 5 davon gesammelt, so kommst du zu unserem «Abschlussrätsel».
#-	Hast du bereits ein Rätsel geskippt und ein weiteres zum dritten Mal falsch, so schliesst sich die Kiste und das Game ist «over».
#""")
#

print("Beginnen wir mit dem ersten Rätsel!")

#1. Level
false_counter = 0
skip_counter = 0
done = False
while not done:
    antwort_1 = (input("Was gibt 2 + 2?"))
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
false_counter = 0

# Level 2
print("Level Nr.2")
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
                exit
                done = True
        else:
            print("Falsch, versuch nocheinmal")
false_counter = 0


            

print (false_counter)
print(skip_counter)
# wenn man jetzt einmal falsch geantwortet hat "1"/ die print counter sind aktuell nur zum überprüfen


#eine Textdatei mit den fragen z.B fragen.py -> diese würde man mit import fragen
