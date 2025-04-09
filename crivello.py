



"""
def crivello(n):
    naturali = set(range(2, n+1))
    
    for j in range(2, int(n ** (1/2))):
        for i in [x * j for x in range(2, n//2 + 1)]:
            naturali.discard(i)
  
    print(naturali)
    print(len(naturali))
crivello(int(input("Scegli un numero: ")))
"""

n=100

insieme= set(range(n+1))
insieme2=list()
insieme3=list()
set_finale= set(insieme3)

for i in insieme:
    if i==2 or i%2!=0: # togli numeri pari
       insieme2.append(i)

print(insieme2)
 

for c in insieme2:
    if c==3 or c%3!=0: #togli numeri divisibili per 3
       insieme3.append(c)

set_finale= set(insieme3)
print(set_finale)
