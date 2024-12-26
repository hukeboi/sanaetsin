import csv

#Tällä ohjelmalla voidaan muuttaa kotimaisten kieleten keskukselta saatu nykysuomen sanalista pää-ohjelman ymmärtämään muotoon.
#hoks hoks että jostain syystä tuo sanalista vaikka onkin cvs-muodossa (comma-separated values) onkin ilmeisesti tabeilla erotettu eikä commalla!! jouduin siis itse muuttamaan sitä

uusinlista = "nykysuomensanalista2024.csv"
hakusana = "Hakusana"
sanaluokka = "Sanaluokka"


substantiivit = []
with open(uusinlista, newline='', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('allwords.txt', 'w', encoding='UTF-8') as allwords:
        for row in reader:
            a = ""
            if row[sanaluokka] == "substantiivi":
                a = "(s)"
            allwords.write(row[hakusana] + a +'\n')
        #print(row[hakusana])



print("Tehty!")