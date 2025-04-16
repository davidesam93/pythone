# ricevuti in input:
#1--un carattere da utilizzare#
#2-- l'ampiezza
#esercizio =  rappresentare l'albero

carattere= input("dammi un carattere: ")
ampiezza= int(input("dammi un  ampiezza :  "))


for i in range(1, ampiezza + 1, 2):  # i va da 1 a ampiezza con passo  2 (aumento di 2, in questo caso cioè solo numeri dispari)
    spazi = (ampiezza - i) // 2      # calcolo degli spazi a sinistra
    riga = " " * spazi + carattere * i
    print(riga)

                
                

        
   

