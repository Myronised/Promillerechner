import os
from colorama import Fore

drinkVolumes = []
drinkIndexes = []
alcAmounts = []

def readFile(filePath, targetList):
    with open(filePath, 'r') as fp:  # r = read, fp = file pointer, Selektion des Textdokuments
        targetList.extend(line.strip() for line in fp) # Erweitert die angesprochene Liste um alle Zeilen der Datei

def writeFile(filePath, dataList):
    with open(filePath, 'w') as fp: # w = write
        for item in dataList: # Selektiert den/die Inhalt/e aus der angesprochenen Liste
            fp.write(f"{item}\n") # Schreibt die selektierten Inhalte Zeile für Zeile in die Datei

def addDrink():
    # INITIALISE
    drinkName = input('Name des Drinks: ')
    drinkVolume = int(input('alc. % vol: '))
    drinkIndex = drinkName + ', ' + str(drinkVolume) + '%'

    print('Der Drink ' + drinkName + ' mit ' + str(drinkVolume) + '% Alc./Vol wurde erfolgreich gespeichert.')

    drinkVolumes.clear() # Löscht die Inhalte von drinkVolumes, um Duplikate zu vermeiden
    drinkIndexes.clear()

    drinkVolumes.append(drinkVolume) # Fügt den eingegebenen Wert von drinkVolume zur Liste drinkVolumes hinzu
    drinkIndexes.append(drinkIndex)

    # READ AND SAVE
    readFile('resources/drinkVolumes.txt', drinkVolumes) # Führt die Funktion readFile aus
    readFile('resources/drinkIndex.txt', drinkIndexes)

    # WRITE
    writeFile('resources/drinkVolumes.txt', drinkVolumes) # Führt die Funktion writeFile aus
    writeFile('resources/drinkIndex.txt', drinkIndexes)

    addDrinkLoop() # Führt die Funktion addDrinkLoop aus

def addDrinkLoop():
    aDQ = input('Möchtest du einen weiteren Drink hinzufügen? (Y/n) ')
    if aDQ in ('Y', 'y', 'J', 'j'):
        addDrink()
    if aDQ in ('N', 'n'):
        chooseAction()

def removeDrink():
    drinkVolumes.clear()  # Löscht die Inhalte von drinkVolumes, um Duplikate zu vermeiden
    drinkIndexes.clear()
    readFile('resources/drinkVolumes.txt', drinkVolumes)  # Führt die Funktion readFile aus
    readFile('resources/drinkIndex.txt', drinkIndexes)
    if not drinkIndexes == []:
        indexDrinks()
        rD = int(input('Welchen Drink möchtest du entfernen? (Index-Ziffer angeben) '))
        drinkVolumes.pop(rD)
        drinkIndexes.pop(rD)
        writeFile('resources/drinkVolumes.txt', drinkVolumes)  # Führt die Funktion writeFile aus
        writeFile('resources/drinkIndex.txt', drinkIndexes)
        print('Der Eintrag wurde erfolgreich entfernt.')

        removeDrinkLoop()
    else:
        print(Fore.RED + 'Du hast noch keinen Drink hinzugefügt.' + Fore.RESET)
        chooseAction()

def removeDrinkLoop():
    rDQ = input('Möchtest du einen weiteren Drink entfernen? (Y/n) ')
    if rDQ in ('Y', 'y', 'J', 'j'):
        removeDrink()
    if rDQ in ('N', 'n'):
        chooseAction()

def editDrink():
    drinkVolumes.clear()  # Löscht die Inhalte von drinkVolumes, um Duplikate zu vermeiden
    drinkIndexes.clear()
    readFile('resources/drinkVolumes.txt', drinkVolumes)  # Führt die Funktion readFile aus
    readFile('resources/drinkIndex.txt', drinkIndexes)
    if not drinkIndexes == []:
        indexDrinks()
        eD = int(input('Welchen Eintrag möchtest du verändern? (Index-Ziffer angeben) '))
        newDrinkName = input('Neuer Name: ')
        newDrinkVolume = int(input('Neues alc. % vol: '))
        drinkVolumes[eD] = newDrinkVolume
        drinkIndexes[eD] = newDrinkName + ', ' + str(newDrinkVolume) + '%'
        writeFile('resources/drinkVolumes.txt', drinkVolumes)  # Führt die Funktion writeFile aus
        writeFile('resources/drinkIndex.txt', drinkIndexes)
        print('Der Eintrag wurde erfolgreich zu [' + newDrinkName + ', ' + str(newDrinkVolume) + '%' + '] geändert.')
        editDrinkLoop()
    else:
        print(Fore.RED + 'Du hast noch keinen Drink hinzugefügt.' + Fore.RESET)
        chooseAction()

def editDrinkLoop():
    eDQ = input('Möchtest du einen weiteren Eintrag bearbeiten? (Y/n) ')
    if eDQ in ('Y', 'y', 'J', 'j'):
        editDrink()
    if eDQ in ('N', 'n'):
        chooseAction()

def chooseAction():
    roaDQ = int(input('Möchtest du einen neuen Eintrag hinzufügen (1), einen bereits existierenden Eintrag bearbeiten (2), entfernen (3) oder die Liste nicht verändern (4)? '))
    if roaDQ == 1:
        addDrink()
    if roaDQ == 2:
        editDrink()
    if roaDQ == 3:
        removeDrink()
    if roaDQ == 4:
        pass
    if not roaDQ in (1, 2, 3, 4):
        print(Fore.RED + 'Du hast eine ungültige Zahl eingegeben.' + Fore.RESET)
        chooseAction()

def indexDrinks():
    # INITIATE
    drinkIndexes.clear()
    readFile('resources/drinkIndex.txt', drinkIndexes)
    # INDEX
    for i in range(len(drinkIndexes)):  # i steht hier für den Loop, in dem die Inhalte aus der Liste abgerufen werden
        print(f"[{i}] {drinkIndexes[i]}")  # Gibt einen Index von der Liste aus

def chooseDrink():
    readFile('resources/drinkVolumes.txt', drinkVolumes)  # Führt die Funktion readFile aus
    indexDrinks()
    cDQ = int(input('Wähle einen Drink aus der Liste (Index-Zahl angeben): '))
    mlDrink = int(input('Wie viele Milliliter dieses Drinks hast du konsumiert? '))
    alcohol = mlDrink * (int(drinkVolumes[cDQ]) / 100) * 0.8
    alcAmounts.append(alcohol)
    chooseDrinkLoop()

def chooseDrinkLoop():
    if len(drinkIndexes) > 1:
        cDLQ = input('Hast du noch einen weiteren Drink konsumiert? (Y/n) ')
        if cDLQ in ('Y', 'y', 'J', 'j'):
            chooseDrink()
