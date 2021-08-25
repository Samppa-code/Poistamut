    # HENKILÖTUNNUKSEN TARKISTUSSOVELLUS  130728-478n

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

    # Sanakirja vuosisatakoodin selvittämiseen
    vuosisadat = {"+": 1800, "-": 1900, "A": 200}

    # Sanakirja tarkisteiden hakemiseen
    tarkisteet = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
                    15: "F", 16: "H", 17: "J", 18: "K", 19: "L", 20: "M", 21: "N", 22: "P", 23: "R", 24: "S", 25: "T", 26: "U", 27: "V", 28: "W", 29: "X", 30: "Y"}

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
    # print("Jakojäännös ", jakojaannos)

    # Haetaan jakojöönnöstä vastaava kirjain
    uudelleenlaskettu_tarkiste = tarkisteet[jakojaannos]
    # print("uusi tarkiste", uudelleenlaskettu_tarkiste)

    # Tarkistetaan täsmääkö tarkiste
    if uudelleenlaskettu_tarkiste == tarkiste_str:
        oikein = True
        
    else:
        oikein = False
        
    return oikein