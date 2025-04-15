""" pagina 601 esercizio 9.5

Realizzate una classe , SodaCan, che rappresenti una lattina di bibita (quindi in forma cilindrica),
dotata dei metodi getsSurfaceArea e getVolume, che calcolano rispettivamente l'area superficiale e il volume della lattina.
 La classe deve avere un costruttore che accetta il raggio della base e l'altezza della lattina come argomenti."""

from math import pi

class SodaCan:
    def __init__(self, altezza, raggio):
        self._altezza= altezza
        self._raggio = raggio

    def getSurfaceArea(self):
          #circonferenza= 2*math.pi *self._raggio
          return ( 2*pi*self._raggio**2 + 2*pi*self._raggio*self._altezza)
    
    def getVolume (self):
         return ( pi *(self._raggio **2) *self._altezza )
    
mini_lattina=SodaCan(8,2)
lattina=SodaCan(9.24,3.37)

print(mini_lattina.getSurfaceArea())
print(lattina.getSurfaceArea())
        