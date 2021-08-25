# Pääohjelma

# Moduulien ja kirjastojen lataikset
import hetutarkistus as ht

# Kysytän käyttäjältä henkilötunnus
kysytty_hetu = input("Anna henkilötunniste ")
# Tarkistetaan onko hetu oikein
oli_oikein = ht.tarkista_hetu(kysytty_hetu)

if oli_oikein == True:
    print("Henkilötunniste oikein!")
else:
    print("Henkilötunniste on virheellinen!")
