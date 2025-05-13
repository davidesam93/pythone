""" esercizio R2.13 PAGINA 89
    

x= input("inserisci una parola: ")
utente=len(x)

if utente %2 !=0:
    m=str(x)
    print(m[0], m[utente//2], m[-1])

else :
    m=str(x)
    print(m[0], m[utente//2-1], m[-1])
    """

""" esercizio R2.14 PAGINA 89
    


lista     = []
utente    = input('Inserisci nome completo : ')

x= list(utente[utente.find(" ")])
print(x)"""

def fattoriale (n) :
    if n==1 :
        return 1
    else :
        return n* fattoriale (n-1)



fattoriale(10)





