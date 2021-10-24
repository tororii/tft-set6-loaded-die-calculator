#This code takes in the unit that you want to hit and your level, and returns the odds of hitting the champ if you use a loaded die on each unit that shares a synergy.
#Made by Troy Costew; League ign: tuburn


#number of units in each synergy, and the levels of the units in said synergy
#example formatting: adept = ["Adept", 3, [0,0,1,1,1]]

#origins
academy = ["Academy", 7, [2,1,1,2,1]]
chemtech = ["Chemtech", 8, [2,2,1,2,1]]
clockwork = ["Clockwork", 4, [1,2,0,2,0]]
cuddly = ["Cuddly", 1, [0,0,0,0,1]]
enforcer = ["Enforcer", 4, [1,1,0,1,1]]
glutton = ["Glutton", 1, [0,0,0,0,1]]
imperial = ["Imperial", 4, [1,2,0,1,0]]
mercenary = ["Mercenary", 5, [1,1,2,0,1]]
mutant = ["Mutant", 6, [1,1,2,1,1]]
scrap = ["Scrap", 7, [2,2,1,1,1]]
sister = ["Sister", 2, [0,1,0,0,1]]
socialite = ["Socialite", 3, [0,0,1,1,1]]
syndicate = ["Syndicate", 6, [2,1,1,1,1]]
yordle = ["Yordle", 6, [2,2,2,0,0]]

#types
arcanist = ["Arcanist", 7, [2,1,2,1,1]]
assassin = ["Assassin", 6, [1,2,2,0,1]]
bruiser = ["Bruiser", 7, [1,2,2,1,1]]
bodyguard = ["Bodyguard", 6, [2,1,1,1,1]]
colossus = ["Colossus", 3, [0,0,1,1,1]]
challenger = ["Challenger", 7, [1,2,1,2,1]]
enchanter = ["Enchanter", 4, [0,1,1,2,0]]
innovator = ["Innovator", 6, [2,1,1,1,1]]
protector = ["Protector", 4, [2,1,0,1,0]]
scholar = ["Scholar", 5, [0,1,2,1,1]]
sniper = ["Sniper", 5, [1,2,1,1,0]]
twinshot = ["Twinshot", 5, [1,1,1,1,1]]
transformer = ["Transformer", 1, [0,0,0,0,1]]





#rerolling odds for each level [tier 1, tier 2, tier 3, tier 4, tier 5]
level1 = [1, 0, 0, 0, 0]
level2 = [1, 0, 0, 0, 0]
level3 = [.75, .25, 0, 0, 0]
level4 = [.55, .30, .15, 0, 0]
level5 = [.45, .33, .20, .2, 0]
level6 = [.35, .35, .25, .5, 0]
level7 = [.22, .35, .30, .12, .01]
level8 = [.15, .25, .35, .20, .05]
level9 = [.10, .15, .30, .30, .15]
level10 = [.5, .10, .20, .40, .25]
level11 = [.1, .2, .12, .5, .35]
allLevels = [[1, level1], [2, level2], [3, level3], [4, level4], [5, level5], [6, level6], [7, level7], [8, level8], [9, level9], [10, level10], [11, level11]]


#units [name, tier, [synergies]]
#example formatting: aatrox = ["Aatrox", 4, [cultist, vanguard]]
#1 cost
caitlyn = ["caitlyn", 1, [enforcer, sniper]]
camille = ["camille", 1, [clockwork, challenger]]
darius = ["darius", 1, [syndicate, bodyguard]]
ezreal = ["ezreal", 1, [scrap, innovator]]
garen = ["garen", 1, [academy, protector]]
graves = ["graves", 1, [academy, twinshot]]
illaoi = ["illaoi", 1, [mercenary, bruiser]]
kassadin = ["kassadin", 1, [mutant, protector]]
poppy = ["poppy", 1, [yordle, bodyguard]]
singed = ["singed", 1, [chemtech, innovator]]
twistedfate = ["twisted fate", 1, [syndicate, arcanist]]
twitch = ["twitch", 1, [chemtech, assassin]]
ziggs = ["ziggs", 1, [scrap, yordle, arcanist]]

#2 cost
blitzcrank = ["blitzcrank", 2, [scrap, protector, bodyguard]]
zyra = ["zyra", 2, [syndicate, scholar]]
katarina = ["katarina", 2, [academy, assassin]]
kogmaw = ["kogmaw", 2, [mutant, sniper, twinshot]]
quinn = ["quinn", 2, [mercenary, challenger]]
swain = ["swain", 2, [imperial, arcanist]]
talon = ["talon", 2, [imperial, assassin]]
tristana = ["tristana", 2, [yordle, sniper]]
warwick = ["warwick", 2, [chemtech, challenger]]
trundle = ["trundle", 2, [scrap, bruiser]]
lulu = ["lulu", 2, [yordle, enchanter]]
zilean = ["zilean", 2, [clockwork, innovator]]
vi = ["vi", 2, [enforcer, sister, bruiser]]

#3 cost
chogath = ["chogath", 3, [mutant, colossus, bruiser]]
ekko = ["ekko", 3, [scrap, assassin]]
gangplank = ["gangplank", 3, [mercenary, twinshot]]
heimerdinger = ["heimerdinger", 3, [yordle, scholar, innovator]]
leona = ["leona", 3, [academy, bodyguard]]
lissandra = ["lissandra", 3, [chemtech, scholar]]
malzahar = ["malzahar", 3, [mutant, arcanist]]
missfortune = ["miss fortune", 3, [mercenary, sniper]]
samira = ["samira", 3, [imperial, challenger]]
shaco = ["shaco", 3, [syndicate, assassin]]
taric = ["taric", 3, [socialite, enchanter]]
zac = ["zac", 3, [chemtech, bruiser]]
vex = ["vex", 3, [yordle, arcanist]]

#4 cost
braum = ["braum", 4, [syndicate, bodyguard]]
mundo = ["mundo", 4, [chemtech, mutant, bruiser]]
fiora = ["fiora", 4, [enforcer, challenger]]
janna = ["janna", 4, [scrap, enchanter, scholar]]
jhin = ["jhin", 4, [clockwork, sniper]]
lux = ["lux", 4, [academy, arcanist]]
orianna = ["orianna", 4, [clockwork, enchanter]]
seraphine = ["seraphine", 4, [socialite, innovator]]
sion = ["sion", 4, [imperial, protector, colossus]]
yone = ["yone", 4, [academy, challenger]]
urgot = ["urgot", 4, [chemtech, twinshot]]

#5 cost
akali = ["akali", 5, [syndicate, assassin]]
galio = ["galio", 5, [socialite, colossus, bodyguard]]
jayce = ["jayce", 5, [enforcer, transformer, innovator]]
jinx = ["jinx", 5, [sister, scrap, twinshot]]
kaisa = ["kaisa", 5, [mutant, challenger]]
tahmkench = ["tahm kench", 5, [mercenary, glutton, bruiser]]
viktor = ["viktor", 5, [chemtech, arcanist]]
yuumi = ["yuumi", 3, [academy, cuddly, scholar]]


units = [caitlyn, camille, darius, ezreal, garen, graves, illaoi, kassadin, poppy, singed, twistedfate, twitch, ziggs,
blitzcrank, zyra, katarina, kogmaw, quinn, swain, talon, tristana, warwick, trundle, lulu, zilean, vi, 
chogath, ekko, gangplank, heimerdinger, leona, lissandra, malzahar, missfortune, samira, shaco, taric, zac, vex,
braum, mundo, fiora, janna, jhin, lux, orianna, seraphine, sion, yone, urgot,
akali, galio, jayce, jinx, kaisa, tahmkench, viktor, yuumi
]



#main program- input is unit you want, output are the odds of other possible units



def loadedDieCalc(unitIndex, levelIndex):
    
    #gettign an array of all champs with the same traits as the chosen unit
    
    sameTraits = []

    for unit in range(len(units)):
        for trait in range(len(units[unit][2])):
            for unitTrait in range(len(units[unitIndex][2])):
                if units[unitIndex][2][unitTrait] == units[unit][2][trait]:
                    sameTraits.append(units[unit])

    sameTraitsReal = []
    for sameTrait in sameTraits:
        if sameTrait not in sameTraitsReal:
            sameTraitsReal.append(sameTrait)


    #Actual calculations and returning the odds of hitting the unit for each unit that shares a synergtgy 

    rollOdds = allLevels[levelIndex][1]

    unitLevel = units[unitIndex][1]
    
    finalOdds = 0

    count = [0, 0, 0, 0, 0]


    for unit in range(len(sameTraitsReal)):
        count = [0, 0, 0, 0, 0]
        finalOdds = 0
        for trait in range(len(sameTraitsReal[unit][2])):
            for unitCount in range(len(sameTraitsReal[unit][2][trait][2])):
                count[unitCount] = count[unitCount] + sameTraitsReal[unit][2][trait][2][unitCount]
        
        if (sameTraitsReal[unit][0] == units[unitIndex][0]):
            count[unitLevel -1 ] = count[unitLevel -1] - 1
        
        finalOdds = rollOdds[unitLevel -1] * (1/count[unitLevel -1]) 
        
        print("Using the loaded die on " + sameTraitsReal[unit][0] + " has a roughly " + str(round(finalOdds*100, 4)) + "%" + " chance of hitting " +  units[unitIndex][0])

while True: 
    unit = input("What unit do you want to hit: ")
    unit = unit.lower()

    match = False
    uIndex = 0

    for i in range(len(units)):
        if unit == units[i][0]:
            uIndex = i
            match = True

    if match == False:
        print("invalid entry")
        break



    level = input("What level are you at: ")
    level = int(level)

    match2 = False

    lIndex = 0

    for j in range(len(allLevels)):
        if level == allLevels[j][0]:
            lIndex = j
            match2 = True

    if match2 == False:
        print("invalid entry")
        break
    
    loadedDieCalc(uIndex, lIndex)






        




    
    

        



            

 

    



    
    


    
            


