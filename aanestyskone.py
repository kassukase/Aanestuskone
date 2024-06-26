verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}

nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

def aanesta(sanakirja):
    try:
        aani = input("Anna äänesi, vaihtoehdot ovat: jaa, ei, eos\n > ").lower
    
    except ValueError:
        sanakirja["virhe"] += 1
        
    else:
        sanakirja[aani] += 1

def nayta_tulokset(sanakirja):
    print(sanakirja["jaa"] * "#")
    print(sanakirja["ei"] * "#")
    print(sanakirja["eos"] * "#")
    print(sanakirja["virhe"] * "#")
          

    
print("Suoritetaanko verouudistus?")
aanesta(verouudistus)
nayta_tulokset(verouudistus)

print("Nalle Puh presidentiksi?")
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)

