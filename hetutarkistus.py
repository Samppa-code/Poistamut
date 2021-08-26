# HENKILÖTUNNUKSEN TARKISTUSSOVELLUS  130728-478n

# Globaalit muuttujat
import datetime
nyt = datetime.datetime.now()

# Sanakirja, jossa vuosisatakoodit 
vuosisadat = {"+": 1800, "-": 1900, "A": 200}

# Sanakirja, jossa jakojäännösten koodit
tarkisteet = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
                    15: "F", 16: "H", 17: "J", 18: "K", 19: "L", 20: "M", 21: "N", 22: "P", 23: "R", 24: "S", 25: "T", 26: "U", 27: "V", 28: "W", 29: "X", 30: "Y"}

def tarkista_hetu(hetu):
    """[Tarkistaa, että suomalainen henkilötunnus on muodostettu oikein
    käyttäen modulo 31 tarkistetta]

    Args:
        hetu (string): Suomalainen henkilötunnus merkkijonona

    Returns:
        boolean: True, jos oikein, False, jos väärin
    """
    
    # Muutetaan hekilötunnus isoihin kirjaimiin
    hetu = hetu.upper()

    # Erotetaan päivä omaan muuttujaan
    paivat_str = hetu[0] + hetu[1]
    kuukaudet_str = hetu[2:4]
    vuodet_str = hetu[4:6]
    vuosisatakoodi_str = hetu[6]
    jarjestysnumero_str = hetu[7:10]
    tarkiste_str = hetu[10]

    # Yhdistetään kaikki numerot yhdeksi merkkijonoksi
    isoluku_str = paivat_str+kuukaudet_str+vuodet_str+jarjestysnumero_str

    # Muutetaan se luvuksi
    isoluku = int(isoluku_str)

    # Lasketaan jakojäännös 31:llä jaettuna (130728478 % 31) eli modulo 31
    jakojaannos = isoluku % 31

    # Haetaan jakojöönnöstä vastaava kirjain
    uudelleenlaskettu_tarkiste = tarkisteet[jakojaannos]

    # Tarkistetaan täsmääkö tarkiste
    if uudelleenlaskettu_tarkiste == tarkiste_str:
        oikein = True
        
    else:
        oikein = False
        
    return oikein

def tarkista_pituus(hetu):
    """Tarkistaa henkilötunnuksen pituuden po. 11 merkkiä

    Args:
        hetu (string): Henkilötunnus

    Returns:
        boolean: True, jos 11 merkkiä, False, jos jotain muuta
    """
    pituus = len(hetu)

    if pituus == 11:
        pituus_ok = True
    else:
        pituus_ok = False
    return pituus_ok

def selvita_sukupuoli(hetu):
    """Selvittää järjestysnumeron perusteella sukupuolen: parillinen -> nainen, pariton, -> mies

    Args:
        hetu (string): Henkilötunnus

    Returns:
        string: Nainen tai mies
    """
    # Otetaan hetusta järjestysnumero-osa
    jarjestysnumero_str = hetu[7:10]

    # Muutetaan järjestysnumero luvuksi
    jarjestysnumero = int(jarjestysnumero_str)

    # Lasketaan modulo 2
    if jarjestysnumero % 2 == 0:
        sukupuoli = "Nainen"
    if jarjestysnumero % 2 !=0:
        sukupuoli = "Mies"
    return sukupuoli

def syntymapaiva(hetu):
    """[summary]

    Args:
        hetu (string): Henkilötunnus

    Returns:
        [string]: Laskettu syntymäpäivä
    """
    paivat_str = hetu[0] + hetu[1]
    kuukaudet_str = hetu[2:4]
    vuodet_str = hetu[4:6]
    vuosisatakoodi_str = hetu[6]

    # Haetaan vuosisata sanakirjasta
    vuosisata = vuosisadat[vuosisatakoodi_str]

    # Yhdistetään Vuosisata ja vuosi
    syntymavuosi = vuosisata + int(vuodet_str)

    # Muunnetaan syntymävuosi merkkijonoksi
    syntymävuosi_str = str(syntymavuosi)

    # Yhdistetään päivät, kuukaudet, ja syntymävuosi
    syntymaaaika = paivat_str + "." + kuukaudet_str + "." + syntymävuosi_str
    return syntymaaaika


def laske_ika(hetu):
    """Muuttaa syntymäpäivän merkkijonosta datetime muotoon.

    Args:
        hetu (string): Henkilötunnus

    Returns:
        datetime: Syntymäpäivä
    """
    paivat_str = hetu[0] + hetu[1]
    kuukaudet_str = hetu[2:4]
    vuodet_str = hetu[4:6]
    vuosisatakoodi_str = hetu[6]

    # Haetaan vuosisata sanakirjasta
    vuosisata = vuosisadat[vuosisatakoodi_str]

    # Yhdistetään Vuosisata ja vuosi
    syntymavuosi = vuosisata + int(vuodet_str)
    paivat = int(paivat_str)
    kuukaudet =int(kuukaudet_str)

    syntymapaiva_datetime = datetime.datetime(syntymavuosi,kuukaudet,paivat)

    paivien_ero = nyt - syntymapaiva_datetime

    return round(paivien_ero.days / 365)
if __name__ == '__main__':
    print(nyt)
    print("Ikä on ", laske_ika("281092-201B"))