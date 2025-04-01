
reddito= int(input ("inserisci il tuo reddito: "))
aliquota1= 0.23
aliquota2=0.35
aliquota3=0.43

SCAGLIONE1=28000
SCAGLIONE2=50000

VA1=int (6440)
VA2= int (14140)
imposta=0
importo=0


if reddito <= SCAGLIONE1 :
    imposta= (reddito* aliquota1)
    print ("devi pagare " , imposta)
else :
    if reddito <=SCAGLIONE2 and reddito> SCAGLIONE1:
        imposta= (reddito - SCAGLIONE1)* aliquota2
        importo= imposta + VA1
        print ( "devi pagare " , importo)
    else : 
     if reddito > SCAGLIONE2 :
        imposta = (reddito - SCAGLIONE2 )*aliquota3
        importo=  imposta + VA2
     print (  "devi pagare " , importo )
