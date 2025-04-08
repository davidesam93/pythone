# ACQUISIRE UNA SERIE DI NUMERI INTERI ADOTTANDO UN VALORE SENTINELLA ("Q") PER TERMINARE LA LETURA ('INPUT')
# QUINDI, STAMPARE IL VALORE MASSIMO 

#funziona ma --senza lista
"""
lista=[]
utente = "a"
valore_max = 0

while utente != "q" :
        utente=(input("inserisci un numero o scrivi 'q' per terminare: "))
        if utente!= "q":
            valore_temporaneo= int(utente)
            if valore_temporaneo > valore_max :
                valore_max=valore_temporaneo
                

print(valore_max)
"""

lista=[]
utente = "a"
valore_max = 0

while utente != "q" :
        utente=(input("inserisci un numero o scrivi 'q' per terminare: "))
        if utente!= "q":
            valore_temporaneo= int(utente)
            lista.append(valore_temporaneo)
                

for i in lista :
      if i > valore_max :
            valore_max= i

print (valore_max)