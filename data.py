import json
import os


def read(file):
    file = open(file,'r')
    data = json.load(file)
    file.close()
    return data

def getData(dataDirectory):
    jsonFiles = filter(lambda x: x.endswith(".json") and not x.startswith("enums") and not x.startswith("landscape"), os.listdir(dataDirectory))
    cardData = []
    for jsonFile in jsonFiles:
        setData = read(os.path.join(dataDirectory, jsonFile))
        cardData += setData
    return list(cardData)
    
def findMatchingCards(cardData, searchText):
    search=[]
    for row in cardData:
        if (searchText.startswith('"') and searchText.endswith('"')):
                if (searchText.replace('"',"").lower() == row[0].lower()):
                    search.append(row)

    for row in cardData:
        if searchText.lower() in row['name'].lower():
            search.append(row)
    return search

def convertCardTypeToString(cardType):
    if cardType == 0:
        return "Creature"
    elif cardType == 1:
        return "Spell"
    elif cardType == 2:
        return "Building"
    elif cardType == 3:
        return "Landscape"
    elif cardType == 4:
        return "Hero"
    elif cardType == 5:
        return "Teamwork"
    else:
        return ""
    
def convertLandscapeToString(landscape):
    if landscape == 0:
        return "Blue Plains"
    elif landscape == 1:
        return "Cornfield"
    elif landscape == 2:
        return "Useless Swamp"
    elif landscape == 3:
        return "SandyLands"
    elif landscape == 4:
        return "NiceLands"
    elif landscape == 5:
        return "IcyLands"
    elif landscape == 6:
        return "Rainbow"
    else:
        return ""
    
def convertSetToString(cardSet):
    if cardSet == 0:
        return "Finn Vs Jake Collectors Pack"
    elif cardSet == 1:
        return "BMO Vs Lady Rainicorn Collectors Pack"
    elif cardSet == 2:
        return "Princess Bubblegum Vs Lumpy Space Princess Collectors Pack"
    elif cardSet == 3:
        return "Ice King Vs Marceline Collectors Pack"
    elif cardSet == 4:
        return "Lemon Grab Vs Gunter Collectors Pack"
    elif cardSet == 5:
        return "Fionna Vs Cake Collectors Pack"
    elif cardSet == 6:
        return "Doubles Tournament Collector Set"
    elif cardSet == 7:
        return "Hero Pack #1"
    elif cardSet == 8:
        return "For The Glory Booster Pack"
    elif cardSet == 9:
        return "Promo"
    elif cardSet == 10:
        return "Kickstarter"
    elif cardSet == 11:
        return "Community Cards"
