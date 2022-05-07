import funktionen
import texte
import colorama
from colorama import Fore

print(Fore.BLACK + texte.einleitung["text"])
for level in range(0,6):
    funktionen.level_allg(texte.levels[level])
funktionen.level_7()

