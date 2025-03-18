
#scrivete un programma per tradurre da 1 a 7 nei nomi della settimana
giorno_scelto=int(input("dammi un numero tra 1 e 7: "))

GIORNI=  ("lunedi   ",#09
          "martedi  ",#18
          "mercoledi",#27
          "giovedi  ",#36
          "venerdi  ",#45
          "sabato   ",#54
          "domenica ")#63

p= (giorno_scelto-1)*9

print(GIORNI[p],GIORNI[p+1],GIORNI[p+2],GIORNI[p+3],GIORNI[p+4],GIORNI[p+5],GIORNI[p+6],GIORNI[p+7],GIORNI[p+8],GIORNI[p+9])
