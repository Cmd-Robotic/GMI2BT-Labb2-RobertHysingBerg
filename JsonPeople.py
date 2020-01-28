import json

def StartUpLoad():
    try:
        File = open('JsonPeople.json', 'r', encoding='UTF-8')
        Data = json.load(File)
        File.close()
    except FileNotFoundError:
        Data = ResetChanges()
    return Data

def Menu(LoadedData):
    while(True):
        UserChoice = input('Welcome to the menu :-)\nYour options are as following:\n1. Delete the currently loaded info and load in the default data from the source file\n2. Display the currently saved config in the Json file\n3. Add a person the the current config\n4. Remove a person from the current config\n5. Save the current config\n6. Exit the script\n\n')
        if (UserChoice):
            if (UserChoice == '1'):
                UserChoice = input('Are you sure you want to reset to the default file\'s data? Y/N\n')
                if (UserChoice.upper() == 'Y' or UserChoice.upper() == 'YES'):
                    LoadedData = ResetChanges()
            elif (UserChoice == '2'):
                ShowJson(LoadedData)
            elif (UserChoice == '3'):
                AddPerson(LoadedData)
            elif (UserChoice == '4'):
                DelPerson(LoadedData)
            elif (UserChoice == '5'):
                UserChoice = input('Are you sure you want to save the currently loaded data to the save file\'s data? Y/N\n')
                if (UserChoice.upper() == 'Y' or UserChoice.upper() == 'YES'):
                    SaveToFile(LoadedData)
            elif (UserChoice == '6'):
                return
            else:
                print('Please enter one of the numbers above by itself.\n')

def ResetChanges():
    PeopleList = []
    DefaultData = open('personer.csv', 'r', encoding='UTF-8')
    for Dat in DefaultData:
        Dat.replace('[', '').replace(']', '').replace('\'', '').replace('\\n', '')
        DatList = Dat.split(';')
        DatDict = {}
        DatDict['Name'] = DatList[0]
        DatDict['Last Name'] = DatList[1]
        DatDict['UserName'] = DatList[2]
        DatDict['e-mail'] = DatList[3]
        PeopleList.append(DatDict)
    DefaultData.close()
    return PeopleList

def ShowJson(Data):
    try:
        File = open('JsonPeople.json', 'r', encoding='UTF-8')
        JsonData = json.load(File)
        input(f'The Json file contains:\n{JsonData}')
        File.close()
    except FileNotFoundError as err:
        print(f'Looks like an "{err}" exception was thrown, try saving a file before loading it')
    print('And the currently loaded data is:\n')
    for Dat in Data:
        print(f'{Dat}')
    input('')

def AddPerson(Data):
    DatDict = {}
    DatList = []
    UserInput = input('Please enter the name, last name, username and e-mail separated by the "-" sign\n')
    DatList = UserInput.split('-')
    try:
        DatDict['Name'] = DatList[0]
        DatDict['Last Name'] = DatList[1]
        DatDict['UserName'] = DatList[2]
        DatDict['e-mail'] = DatList[3]
        Data.append(DatDict)
    except IndexError as err:
        input(f'An "{err}" exception was thrown, you wouldn\'t know about would you?')

def DelPerson(Data):
    Counter = 1
    input('The currently loaded people ar as follows:\n')
    for Dat in Data:
        print(f'{Counter} {Dat}')
        Counter += 1
    try:
        Deleter = int(input('Enter the corresponding number to the entry you want gone:\n'))
        UserChoice = input(f'Are you sure you want to delete entry nr.{Deleter}? Y/N\n')
        if ((UserChoice.upper() == 'Y' or UserChoice.upper() == 'YES') and Deleter != 0):
            Data.pop(Deleter - 1)
    except ValueError as err:
        input(f'It would seem an "{err}" exception was thrown, enter only numbers next time please.')
    except IndexError as err:
        input(f'It would seem that an "{err}" exception was thrown, next time make sure you enter a valid number')

def SaveToFile(Data):
    File = open('JsonPeople.json', 'w', encoding='UTF-8')
    json.dump(Data, File)
    File.close()
    input('Saved!')