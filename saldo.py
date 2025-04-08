#scrivete una funzione che calcoli il saldo di un conto bancario dopo che siano trascorsi un dato numero di anni,
#a partire da un dato saldo iniziale un dato tasso di interesse annuo, accreditando gli interessi annualmente

def saldo(saldo_iniziale,tasso, numero_anni) :
    if numero_anni == "none":
        for i in range(20):
             saldo_iniziale=(saldo_iniziale* tasso)+ saldo_iniziale
             print ('il tuo saldo_totale sarà: ', saldo_iniziale)

    else:
            numero= int(numero_anni)
            for i in (range(numero)):
             saldo_iniziale=(saldo_iniziale* tasso)+ saldo_iniziale
             print ('il tuo saldo_totale sarà: ', saldo_iniziale)
            

saldo_parziale=0
saldo_totale=0
ricavi=0
saldo_iniziale=int(input("inserisci un saldo iniziale: "))
tasso = 0.25
numero_anni= (input ( "per quanto anni vuoi investire? scrivi ? Oppure 'none' se non lo sai: " ))

saldo(saldo_iniziale,tasso, numero_anni)
