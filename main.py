# Pääohjelma

# Moduulien ja kirjastojen lataikset
import hetutarkistus as ht
import datetime
nyt= datetime.datetime.now()


hetu_jarkevä = False

while  hetu_jarkevä == False:
    # Kysytän käyttäjältä henkilötunnus
    kysytty_hetu = input("Anna henkilötunniste ")

    # Tarkistetaan onko hetu oikean pituinen
    pituus_oikein = ht.tarkista_pituus(kysytty_hetu)

    if pituus_oikein == True:
     # Tarkistetaan onko hetu oikein
        try:
            oli_oikein = ht.tarkista_hetu(kysytty_hetu)

            # Ilmoittaa käyttäjälle oliko hetu oikein
            if oli_oikein == True:
                print("Henkilötunniste oikein!")
                print("Sukupuoli:",ht.selvita_sukupuoli(kysytty_hetu))
                print("Syntymäpäivä oli", ht.syntymapaiva((kysytty_hetu)))
                print("Ikä on", ht.laske_ika(kysytty_hetu))
                
                hetu_jarkevä = True
        
            else:
                print("Henkilötunniste on virheellinen!")
                hetu_jarkevä = False
        except:
            print("Tapahtui virhe")
            hetu_jarkevä= False
    else:
        print("Henkilötunnuksen pituus väärä")
        hetu_jarkevä = False