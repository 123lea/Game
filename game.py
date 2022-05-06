import funktionen
import texte

print(texte.einleitung["text"])

for level in range(0,6):
    funktionen.level_allg(texte.levels[level])
#die zwei Funktionieren noch nicht
funktionen.level_7()

"""
Sonstiges:
- mit regex die Eingabemöglichkeiten überarbeiten/anpassen an unsere Fragen

Ziel:
- sinvolle Namen
- möglichstwenige Wiederholungen
"""