""" 
    Scrivere un programma python che acquisisce tutte le righe di un file di testo (chiedi il nome all'utente) .
    il file si suppone contenere un numero per ogni riga (anche con decimali--> float)
    Calcolare la media ed indicare il valore massimo comprensivo della riga in cui è stato trovato il file

     
    """


"""from os import getcwd
name= getcwd()
print(name)"""

valore_max = 0
sommatotale = 0
contatore = 0
contariga=0


utente = input('Dimmi che file vuoi aprire: ') + ".txt"
lista2= list()

with open(utente) as file:
    for riga in file:
        numero = int(riga.strip())  # Pulisce e converte
        lista2.append(numero)

for j in lista2:
    contatore += 1
    sommatotale += j
    if j > valore_max:
        valore_max = j
        
contariga= lista2.index(valore_max)
       
media = float(sommatotale / contatore)

print(f"Il tuo file contiene {contatore} righe, il valore più alto è il {valore_max}, e si trova alla riga {contariga + 1 }. la somma è {sommatotale}, e la media è {media}")











 




