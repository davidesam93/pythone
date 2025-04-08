#acquisire tramite input() una sequenza di valori numerici fino a che l utente non scriva exit#
# in tal caso stampare la media dei valori letti#

sommaparziale= 0
numero="a"
conteggio=0

while numero!="exit":
    
    numero= (input("dammi una serie di numeri o scrivi exit per interrompere: "))
    sommaparziale+= float(numero)
    conteggio+=1

    

print ("la tua media è ", sommaparziale / conteggio)




