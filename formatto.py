
""" Inizializzare una lista con i reciproci  dei primi 10 interi naturali
stampare i FLOAT risultati in modo da visualizzare 8 decimali """

lista= list(range(11))
print (lista)
lista1=list()


for i in lista:
     i = round(float(i), 8)
     lista1.append(i)

for num in lista1:
    print(f"{num:.8f}")




