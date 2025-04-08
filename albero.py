# ricevuti in input:
#1--un carattere da utilizzare#
#2-- l'ampiezza
#esercizio =  rappresentare l'albero

carattere= input("dammi un carattere: ")
ampiezza= int(input("dammi un  ampiezza :  "))



if ampiezza %2 == 0 :
        while ampiezza!=0 :
                for i in ampiezza :
                        print (" " * ((ampiezza//2)-1) + carattere + " "*((ampiezza//2)-1))
                        ampiezza-1

                
                

        
   

