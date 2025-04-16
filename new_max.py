""" 
    Scrivere un programma python che acquisisce tutte le righe di un file di testo (chiedi il nome all'utente) .
    il file si suppone contenere un numero per ogni riga (anche con decimali--> float)
    Calcolare la media ed indicare il valore massimo comprensivo della riga in cui è stato trovato il file

     
    """


"""from os import getcwd
name= getcwd()
print(name)"""

utente=input('Dimmi che file vuoi aprire : ') + ".txt"  # chiede il nome file
dascrivere= open(utente)                                 #apre il file e lo salva in lista
lista=list(dascrivere)

valore_max=0
sommatotale=0
contatore=0


lista2= list()

for i in lista:                      # elimina "/n" e lo converte in intero
    lista2.append (int(i[0:-1])) 
   

for j in lista2 :                    # trova valore max
      if j > valore_max :
            valore_max= j



for n in lista2 :                    # calcola media
     sommatotale += n
     contatore+=1

media= float(sommatotale / contatore)

print(f'Il tuo file continee {contatore} righe, il valore massimo del tuo file di testo è il {valore_max} mentre la somma dei tuoi numeri è {sommatotale} e la media è {media}')











 




