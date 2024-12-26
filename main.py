sana = input("Anna sana (esim. ko??a):\n")
vaaratKirjaimet = input("Anna väärät kirjaimet PELKÄSTÄÄN PILKULLA EROTETTUNA (esim. i,r):\n")
vaaratKirjaimet = vaaratKirjaimet.split(',')

mode = 0   #0=jos on joku kirjain tiedetään niin se ei voi olla muuallam, 1=voi olla vielä jo tiedettyjä kirjaimia muualla

laaja = True # Laajempi etsintä jolloin mahdollisesti yhdistellään substantiiveja

letters = []
correctWords = []
for letter in sana:
    if letter != '?': letters.append(letter)

s = []
lyhinS = 999999
def checkWord(word):
    isCorrect = True
    for i in range(0, len(sana), 1):
        if word[i] in vaaratKirjaimet:
            isCorrect = False
        if word[i] != sana[i] and sana[i] != "?":
            isCorrect = False
        if (sana[i] == "?" and word[i] in letters):
            if (mode == 0):
                isCorrect = False
    if isCorrect:
        correctWords.append(word)
with open("allwords.txt", "r", encoding='UTF-8') as f:
    for line in f:
        word = line.replace("\n", "")

        subPossible = False
        possible = True
        
        if "(s)" in word:
            word = word.replace("(s)", "")
            subPossible = True
        

        if len(word) > len(sana): # jos pidempi kun etsittävä niin ei voi olla
            continue

        if len(word) != len(sana):# jos eripituinen kun etsittävä niin voi olla ainoastaan substantiivi kombossa
            possible = False

        if (len(word) + 1) == len(sana):# jos vain yhden lyhempi kun etsittävä niin ei voi olla substantiivi kombossa
            subPossible = False 

        if ((not possible) and (not subPossible)): #jos eripituinen ja vain yhden lyhempi niin ei voi olla mitenkään
            continue

        
        if possible:
            checkWord(word)

        elif subPossible and laaja:
            mahd = True
            for merkki in vaaratKirjaimet:
                if merkki in word:
                    mahd = False
            
            if mode == 0:
                lkm = 0
                for mask in range(0, len(sana) - len(word) + 1, 1):
                    mahdmsk = True
                    for i in range(0, len(word), 1):
                        if sana[mask + i] != '?':
                            if sana[mask + i] != word[i]:
                                mahdmsk = False
                    if mahdmsk:
                        lkm += 1
                if lkm == 0:
                    mahd = False
            
            if mahd:
                if len(word) < lyhinS:
                    lyhinS = len(word)
                s.append(word)

if len(s) <= 2000:
    for sana1 in s:
        if len(sana1) + lyhinS > len(sana):
            continue
        for sana2 in s:
            if sana1 != sana2:
                if len(sana1 + sana2) == len(sana):
                    checkWord(sana1 + sana2)
else:
    print(f'Lisätietoa tarvitaan laajaan hakuun ({len(s)})')
    if len(correctWords) == 0:
        stats = {}
        for sana in s:
            kirjaimet = list(sana)
            kirjaimet = list(dict.fromkeys(kirjaimet))
            for kirjain in kirjaimet:
                if kirjain in stats:
                    stats[kirjain] += 1
                else: 
                    stats.update({kirjain: 1})

        for key, value in stats.items():
            stats[key] = abs((len(s) / 2) - value)
        
        best = min(stats, key=stats.get)

        print(f'Paras veikkaus: {best}')


guess = {}
howManyShown = 0
for correct in correctWords:
    for i in range(0, len(correct), 1):
        if str(correct[i]) in guess:
            guess[str(correct[i])] += 1
        elif correct[i] not in letters:
            guess[str(correct[i])] = 1
    #if howManyShown > 13: continue
    print(correct)
    #if howManyShown == 13: print(f".. (+{len(correctWords) - 14})")
    howManyShown += 1
print(len(correctWords))
bestGuess = sorted(guess.items(), key=lambda x:x[1], reverse=True)
if len(correctWords) > 2:
    print(f"Parhaat veikkaukset: {str(bestGuess[0][0]).upper()}, {str(bestGuess[1][0]).upper()} ja {str(bestGuess[2][0]).upper()}.")
if len(correctWords) == 0:
    print("Ei yhtään sopivaa sanaa.")
       