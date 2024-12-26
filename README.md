# Sanaetsin
Ohjelma joka mahdollistaa sanojen etsimisen ja rajaamisen wildcardeilla

Tämän ohjelman avulla voit etsiä suomenkielisiä sanoja jotka täyttävät halutut hakuehdot.

Esimerkiksi jos halutaan tietää kaikki 5 merkkiset sanat jotka alkavat kirjaimilla "ko" ja loppuvan kirjaimeen "a". Ohjelma tulostaa kaikki suomenkielet sanat jotka täyttävät ehdot ja lisäksi se voi ehdottaa myös suosituinta kirjainta, joka voi olla hyvä veikkaus esimerkiksi hirsipuu tyylisessä pelissä.

## Käyttö

1. Lataa kaikki tiedostot
2. Muuta asetuksia main.py tiedoston sisältä tarpeen mukaan. (mode voi olla joko 0 tai 1, laaja puolestaan indikoi laajempaa substantiivien yhdistely etsintää)
3. Aja ```main.py``` tiedosto.
4. Ohjelma kysyy seuraavaksi sanaa. Kirjoita tähän sana ja jätä nk. "wildcard" kirjaimet kysymysmerkeiksi (Eli kirjaimet jotka voivat olla mitä vain)
5. Ohjelma kysyy seuraavaksi vääräksi tiedettyjä kirjaimia. (Kirjaimia jotka eivät voi olla minkään kysymysmerkin kohdalla) Kirjoita siis tähän kohtaan kaikki sellaiset kirjaimet joita ei saa käyttää PELKÄLLÄ PILKULLA EROTELTUNA. Jos kaikki kirjaimet käyvät kysymysmerkkien kohdalle älä kirjoita mitään vaan paina enter.
6. Nauti.

## Esimerkki
  tulossa pian en jaksa keksiä

## Ongelmia?
Jos yhtään ehtoihin sopivaa sanaa ei ole kotimaisten kielten keskuksen sanalistalla kertoo ohjelma tämän. Tällöin etsitty sana voi olla sellainen yhdyssana jota ei ole jostainsyystä listalla. Ohjelman ollessa laajassa etsintätilassa yrittää se kuitenkin yhdistellä sopivia substantiiveja ja löytää sitä kautta mahdollisen sanan. Kuitenkin tämä onnistuu ainoastaan jos mahdollisia substantiiveja on vähän. Muulloin ohjelma ilmoittaa tarvitsevansa lisää tietoa. Lisäksi viestin jälkeen suluissa lukee mahdollisten substantiivejen määrä. Tämä tulisi saada alle kahteen tuhanteen mm. lisäämällä vääriksi tiedettyjä kirjaimia.
Lisäksi voit koittaa päivittää ```allwords.txt``` tiedostoa mukana tulevan ```cvstotxt.py``` tiedoston avulla. Tähän tarvitset uudemman nykysuomen sanalistan kotukselta. 
