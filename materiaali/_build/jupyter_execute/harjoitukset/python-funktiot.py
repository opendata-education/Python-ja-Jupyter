# Funktiot Pythonissa

Funktiot ovat sellaista koodia, jota tyypillisesti tarvitaan usein ja jota voidaan uudelleenkäyttää helposti. Pythonissa on paljon [valmiita funktioita](https://docs.python.org/3/library/functions.html), esimerkiksi  [`print()`](https://docs.python.org/3/library/functions.html#print), jonka avulla tulostetaan tekstiä. `print()`-funktiolle kirjoitetaan sulkeiden sisään tulostettava teksti, kuten "Hello, World!". Tätä kutsutaan funktion parametriksi. Funktiosta riippuen parametreja voidaan tarvita useampiakin (tai ei yhtäkään).

Tutustutaan tässä harjoituksessa omien funktioiden tekemiseen Pythonilla.

Funktion määrittelemiseen käytetään **def**-komentoa. Seuraavassa esimerkissä määritellään funktio, nimeltä "tervehdys", joka tulostaa sanan "Terve!".

def tervehdys():
    print('Terve!')

Nyt tekemäämme funktiota voidaan käyttää seuraavasti:

tervehdys()

Tehdään seuraavaksi vastaava funktio, mutta siten, että funktiolle annetaan **parametrina** nimi, jota tervehditään. Kutsutaan tätä funktiota nimellä "tervehdi".

def tervehdi(nimi):
    print("Terve " + nimi + "!")

tervehdi("Pekka")

Funktio voi antaa myös **paluuarvon**. Tehdään esimerkkifunktio, joka ottaa kaksi lukua parametreina ja antaa paluuarvona näiden summan. Kutsutaan funktiota nimellä "summa". Paluuarvo annetaan funktiossa komennolla **return**. Tämän komennon jälkeen funktion suoritus päättyy, vaikka sen jälkeen olisikin kirjoitettu vielä koodia.

def summa(a, b):
    return a + b

summa(3,4)

Funktion paluuarvon voi tallentaa muuttujaan seuraavasti:

x = summa(1,3)

print(x)

<div class="alert alert-info">
    
**Funktiot**
    
- Funktion määrittely aloitetaan **def**-komennolla.
- Funktiolle voidaan antaa **parametreja**
- **Paluuarvo** määritellään **return**-komennolla
    
```python
def funktion_nimi(parametri1, parametri2):
    # Tehdään jotain parametreilla
    return paluuarvo
```
</div>

## Esimerkkejä

### Celsiukset Fahrenheiteiksi

Tehdään funktio, joka muuntaa celsiusasteet fahrenheiteiksi kaavalla $y = \frac{9}{5}x + 32$. Kutsutaan funktiota nimellä "CF_muunnos".

def CF_muunnos(celsius):
    fahrenheit = 9/5*celsius + 32
    return fahrenheit

CF_muunnos(20) # 20 celsiusastetta Fahrenheiteina

### Toisen asteen yhtälö

Tehdään funktio, joka antaa toisen asteen yhtälön $f(x)=x^2+2x+1$ arvon kohdassa x.

def f(x):
    return x**2 + 3*x + 1

f(3)

Yleisempi funktio, jolle voidaan antaa myös vapaavalintaiset parametrit $a, b, c$

def g(x, a, b, c):
    return a*x**2 + b*x + c

g(2, 1, 2, 3) # 2²+2*2+3