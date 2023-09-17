# INITIATE
from colorama import Fore
import utils

drinkVolumes = []
drinkIndexes = []

# INTRODUCTION 1
print('Herzlich Willkommen im Promillerechner von Ben Clemenz.')
print('In den folgenden Schritten wirst du idiotensicher durch die Berechnung geleitet.')
print('#kenndeinlimit #maßvollgenießen\n')
print('Fangen wir mit deinen persönlichen Informationen an.')

# PERSON
gender = input('Dein Geschlecht (m/w): ')
if not gender in ('m', 'M', 'w', 'W'):
    print(Fore.RED + 'Du hast ein ungültiges Geschlecht angegeben. Bitte verwende nur den Buchstaben m oder w.' + Fore.RESET)
    gender = input('Dein Geschlecht (m/w): ')
    if not gender in ('m', 'M', 'w', 'W'):
        exit('Du hast mehrfach ein ungültiges Geschlecht angegeben.')
if gender in ('m', 'M'):
    age = int(input('Dein Alter (in Jahren): '))
    heigth = int(input('Deine Körpergröße (in cm): '))
    bodymass = int(input('Dein Gewicht (in kg): '))
    gkw = 2.447 - 0.09516 * age + 0.1074 * heigth + 0.3362 * bodymass
else:
    heigth = int(input('Deine Körpergröße (in cm): '))
    bodymass = int(input('Dein Gewicht (in kg): '))
    gkw = -2.097 + 0.1069 * heigth + 0.2466 * bodymass

# INTRODUCTION 2
print('\nAlles klar. Jetzt musst du mir einmal beichten, was du heute Abend schon getrunken hast. ;)')
print('In den nächsten Schritten kannst du die gespeicherten Spirituosen verwalten.\n')

# DRINK(S)
drinkIndexes.clear()
utils.readFile('resources/drinkIndex.txt', drinkIndexes)
if not drinkIndexes == []:
    print('Die folgenden Drinks befinden sich bereits auf der Liste:')
    drinkIndexes.clear()
    utils.indexDrinks()
    utils.chooseAction()
else:
    print('Du hast bisher noch keinen Drink hinzugefügt. Das ändern wir jetzt.')
    drinkIndexes.clear()
    utils.addDrink()

print('Perfekt. Jetzt kannst du die Drinks wählen, die du heute konsumiert hast.')
utils.chooseDrink()
alcAmount = sum(utils.alcAmounts)

bak = (0.8 * alcAmount) / gkw
bak = round(bak, 2)

lDQ = input('\nKlasse! Du hast alles beantwortet. Bist du nun bereit, deine ungefähre Blutalkoholkonzentration zu erfahren? (Y/n) ')
if lDQ in ('Y', 'y', 'J', 'j'):
    print('\n\nDie Konzentration des Alkohols in deinem Blut liegt bei ca. ' + Fore.RED + str(bak) + '‰' + Fore.RESET + '.')
    input('Drücke Enter um das Programm zu beenden! ')
else:
    lDQ = input('Bist du dir sicher, dass du das Programm beenden willst ohne deine BAK zu erfahren? (Y/n) ')
    if lDQ in ('Y', 'y', 'J', 'j'):
        exit('Alles klar. Bis zum nächsten Mal! :(')
    if lDQ in ('N', 'n'):
        print('Ich dachte schon, du willst mich verarschen! ;D Dann mach dich bereit:')
        print('\n\nDie Konzentration des Alkohols in deinem Blut liegt bei ca. ' + Fore.RED + str(bak) + '‰' + Fore.RESET + '.')
        input('Drücke Enter um das Programm zu beenden! ')
    else:
        exit('Ich nehm deinen Tippfehler mal als "ja". Dann bis zum nächsten Mal! :(')