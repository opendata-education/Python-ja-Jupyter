# Data-analyysi Pythonilla

Tässä notebookissa käydään läpi esimerkki data-analyysista Pythonilla, jossa piirretään kuvaaja Helsingin kuukausittaisista keskilämpötiloista vuonna 2020. Tämän on tarkoitus olla lyhyt esimerkki, joka näyttää, mitä Jupyter Notebookeilla ja Pythonilla voi esimerkiksi tehdä. Katso myös [toinen esimerkki](https://mybinder.org/v2/gh/opendata-education/Python-ja-Jupyter/HEAD?filepath=materiaali%2Fharjoitukset%2Fdata-analyysi_esimerkki.ipynb), jossa pääset itse kirjoittamaan koodia ohjatusti! 

Ennenkuin mennään varsinaisesti asiaan, perehdytään pikaisesti itse Jupyter Notebook -alustaan.
Jupyter Notebook -muistio koostuu **soluista**, jotka voivat sisältää joko tekstiä tai koodia.
Tämä solu on tekstisolu, jota voi muokata kaksoisklikkaamalla tätä hiirellä.
Kokeile! Muokkaustilasta pääsee pois suorittamalla solun painamalla sivun ylälaidassa olevaa *Run*-painiketta.
Koodisolun suorittaminen tapahtuu myös *Run*-painikkeella. Tällöin solun sisällä oleva koodi suoritetaan ja mahdollinen tulos tulee näkyviin solun alapuolelle. Koodisolun tunnistat solun vasemmassa reunssa olevasta `In [ ]:`-tekstistä.

Mennään sitten itse data-analyysiesimerkin pariin!
Esimerkin koodit on valmiiksi kirjoitettu, joten voit suorittaa koodisolut sellaisenaan.
Voit myös vapaasti kirjoittaa itse koodia tai vaihtaa jotain valmiissa koodissa!

Yksinkertaisimmillaan voimme visualisoida lämpötiladatan muutamalla rivillä koodia. Tähän kuuluu tarvittavien pakettien ottaminen käyttöön import komennolla sekä datan lukeminen ja sen piirtäminen. Alla olevassa esimerkissä otetaan ensin käyttöön paketit matplotlib.pyplot kuvaajien piirtämistä varten ja pandas datan lukemista varten.

Paina alla olevaa koodisolua, jolloin se muuttuu aktiiviseksi. Tämän jälkeen paina sivun ylälaidassa olevaa *Run*-painiketta, jolloin solussa oleva koodi suoritetaan. Näytölle pitäisi nyt ilmestyä kuvaaja.

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('keskilampotila2020_Helsinki.csv')
plt.plot(data['Kk'], data['Keskilämpötila (°C)'])

Datan visualisoiminen käy siis varsin pienellä työmäärällä. Äsken piirtämäsi kuvaaja ei kuitenkaan kerro vielä kovin paljoa, joten otetaan esimerkki, jossa tehdään kuvaajasta hieman parempi.

Suorita (*Run*) alla olevat koodisolut yksi kerrallaan. Voit myös katsoa, mitä koodiin on kirjoitettu ja kokeilla, mitä tapahtuu jos muutat jotain parametrejä. Koodissa rivit, jotka alkavat #-merkillä ovat kommentteja, jotka eivät vaikuta itse koodiin, vaan niihin tyypillisesti kirjoitetaan mitä koodi tekee.

# Otetaan tarvittavat paketit käyttöön
import matplotlib.pyplot as plt
import pandas as pd

# Luetaan data tiedostosta 'keskilampotila2020_Helsinki.csv'
# ja tallennetaan tulos muuttujaan 'data'.
data = pd.read_csv('keskilampotila2020_Helsinki.csv')

# Tulostetaan näytölle datan muutama ensimmäinen rivi, jotta näemme miltä data näyttää.
data.head()

# Valitaan datasta 'Kk'-sarake ja 'Keskilämpötila (°C)'-sarake
# ja tallennetaan ne muuttujiin 'kuukaudet' ja 'lämpötilat'
kuukaudet = data['Kk']
lämpötilat = data['Keskilämpötila (°C)']

# piirretään kuvaaja, jossa x-akselille tulee kuukaudet ja y-akselille lämpötilat
# Kuvaajan piirretään punaisella viivalla ('r-') ja datapisteet merkitään kuvaajaan
plt.plot(kuukaudet, lämpötilat, 'r-', marker='o')

# Asetetaan x-akselin ja y-akselin otsikot
plt.xlabel('Kuukausi')
plt.ylabel('Lämpötila (°C)')

# Asetetaan kuvaajalle pääotsikko
plt.title('Keskilämpötila Helsingissä kuukausittain 2020')

# Tehdään lista x-akselille tulevista teksteistä.
labels = ['Tammikuu','Helmikuu','Maaliskuu','Huhtikuu','Toukokuu','Kesäkuu','Heinäkuu','Elokuu','Syyskuu','Lokakuu','Marraskuu','Joulukuu']

# Muutetaan x-aksella olevat numerot äsken määrittämiksi teksteiksi.
# range(1,13) luo listan, jossa on numerot 1-12.
# Seuraavaksi annetaan parametrina tekstit, jotka sijoitetaan numeroiden paikalle (tallennettu 'labels'-muuttujaan)
# Lopuksi vielä käännetään tekstejä, jotta ne eivät menisi päällekkäin.
plt.xticks(range(1,13), labels, rotation=60)

# Näytetään kuvaajan ruudukko
plt.grid()

# Tämä komento poistaa ylimääräiset tulosteet ja näyttää ainoastaan kuvan, kun solu suoritetaan.
plt.show()

Kuvaajien muokkaamiseen on paljon mahdollisuuksia, joita ei kaikkia pysty tässä mitenkään esittämään. Googlesta löytää kuitenkin yleensä ratkaisun siihen, millaisen kuvaajan ikinä haluatkaan piirtää.

Kokeile vielä muuttaa jotain aiemmissa koodeissa. Miten muuttaisit akseleiden otsikoita? Miten piirtäisit kuvaajan vihreällä katkoviivalla? 

## Histogrammi

Otetaan vielä toinen esimerkki datan visualisoinnista. Piirretään tällä kertaa histogrammi mitatuista lämpötiloista Helsingissä tammikuussa 2021. Tätä varten olemme jälleen hakeneet datan Ilmatieteenlaitoksen hakupalvelusta. Data koostuu 10 minuutin välein tehdyistä mittauksista, joten dataa on varsin paljon.

# Otetaan tarvittavat paketit käyttöön
import matplotlib.pyplot as plt
import pandas as pd

# Luetaan data tiedostosta 'lampotila_tammikuu2021_Helsinki.csv'
# ja tallennetaan tulos muuttujaan 'data'.
data = pd.read_csv('lampotila_tammikuu2021_Helsinki.csv')

# Tulostetaan näytölle datan muutama ensimmäinen rivi, jotta näemme miltä data näyttää.
data.head()

# Valitaan datasta 'Ilman lämpötila (degC)'-sarake
# ja tallennetaan se muuttujaan 'lämpötilat'
lämpötilat = data['Ilman lämpötila (degC)']

# piirretään histogrammi, ja valitaan alkuun pylväiden lukumääräksi 50
plt.hist(lämpötilat, bins=50)

# Asetetaan x-akselin ja y-akselin otsikot
plt.xlabel('Lämpötila (°C)')
plt.ylabel('Mittaustulokset per pylväs')

# Asetetaan kuvaajalle pääotsikko
plt.title('Lämpötilajakauma Helsingissä tammikuussa 2021')

# Tämä komento poistaa ylimääräiset tulosteet ja näyttää ainoastaan kuvan, kun solu suoritetaan.
plt.show()

Histogrammin piirtäminenkin siis onnistuu muutamalla yksinkertaisella komennolla. Tässäkin tapauksessa voisimme muokata kuvaajaa edelleen mielemme mukaan. Tehdään histogrammi uudelleen, mutta tällä kertaa siten, että pylväiden leveys on 1 degC.

# Piirretään histogrammi välillä -22 degC ... 4 degC, jolloin pylväitä tarvitaan 26
# fill=False poistaa värityksen kuvaajasta, jolloin pylväät erottuvat helpommin.
plt.hist(lämpötilat, bins=26, range=(-22,4), fill=False)

# Asetetaan vielä x-akselin rajat samoiksi kuin histogrammin
plt.xlim((-22,4))

plt.xlabel('Lämpötila (°C)')
plt.ylabel('Mittaukset/°C')
plt.title('Lämpötilajakauma Helsingissä tammikuussa 2021')


# Tämä komento poistaa ylimääräiset tulosteet ja näyttää ainoastaan kuvan, kun solu suoritetaan.
plt.show()

Äsken käsittelemässämme datassa oli lämpötilojen lisäksi muutakin dataa, kuten tuulen nopeus tai lumen syvyys. Kokeile piirtää jostakin toisesta sarakkeesta kuvaaja tai histogrammi.

Voit myös kokeilla etsiä itse jonkin datasetin netistä ja laittaa suoran linkin `read_csv`-työkalun parametriksi.